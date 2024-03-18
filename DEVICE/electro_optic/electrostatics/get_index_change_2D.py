#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------
# Author: Georgios Gcharalampous (gcharalampous)
# Version: 1.0
# Description: This script performs electro-optic simulations and visualizes the results.
#----------------------------------------------------------------------------

"""
No user-inputs are required.
"""

import os
import lumapi
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
import shapely.ops as so
import shapely.geometry as sg

# Import user-defined modules
from DEVICE.electro_optic.user_inputs.user_simulation_parameters import *
from DEVICE.electro_optic.user_inputs.user_materials import *
from DEVICE.electro_optic.waveguide_render import waveguide_draw
from DEVICE.electro_optic.charge_region import add_charge_region
from config import *

# Define grid dimensions
N_x = 500
N_z = 1000


def index_permutation(Ex, Ez, wg_index_x, wg_index_z):
    
    if(wg_material == "AlGaAs (Aluminium Gallium Arsenide)"):
        r41 = 1.46e-12
        index_permutation_tri_x = 0.5*((wg_index_x)**3)*r41*Ez
        index_permutation_tri_z = 0 * Ex
    else:
        print('Non-linear material, not defined')
        index_permutation_tri_x = 0 * Ez
        index_permutation_tri_z = 0 * Ex
    
    return index_permutation_tri_x, index_permutation_tri_z     

   
        

def get_Efield_static_2D(device):
    """
    Retrieve electrostatic field data from the simulation.

    Parameters:
        device (lumapi.DEVICE): Lumerical DEVICE object.

    Returns:
        E (np.ndarray): Electric field data.
        x (np.ndarray): x-coordinate data.
        z (np.ndarray): z-coordinate data.
        tri: Triangulation data.
    """
    electrostatics_result = device.getresult("CHARGE::electric_monitor", "electrostatics")
    E = np.squeeze(electrostatics_result['E'])
    x = np.squeeze(electrostatics_result['x'])
    z = np.squeeze(electrostatics_result['z'])
    tri = device.getdata("CHARGE::electric_monitor", "electrostatics", "elements")
    return E, x, z, tri

if __name__ == "__main__":
    with lumapi.DEVICE(hide=True) as device:
        # Draw the waveguide structure using a custom function
        device.redrawoff()
        waveguide_draw(device)
        
        # Draw the simulation region
        add_charge_region(device)
        
        # Save and run the simulation
        device.save(EO_MODULATOR_DIRECTORY_WRITE_FILE + "\\eo_waveguide_simulation.ldev")
        device.run()
        
        # Get the electric field data
        E, x_tri, z_tri, tri = get_Efield_static_2D(device)
        E_2D = np.delete(E, 1, axis=1)  # Remove y-component
        


        
        # Extract x and z components of electric field
        Ex_tri, Ez_tri = E_2D[:, 0], E_2D[:, 1]
            
        index_permutation_tri_x, index_permutation_tri_z = index_permutation(
            Ex=Ex_tri, Ez=Ez_tri, wg_index_x=wg_index_x, wg_index_z=wg_index_z )

        
        # Define grid
        x = np.linspace(-2*wg_width, 2*wg_width, N_x)
        y = 0
        z = np.linspace(-0e-6, wg_thickness, N_z)
        X, Z = np.meshgrid(x, z)
        
        Dnx = np.zeros((N_x, N_z))
        Dnz = np.zeros((N_x, N_z))
        
        vt = np.zeros((len(x_tri), 2))
        vt[:, 0] = x_tri
        vt[:, 1] = z_tri
        
        Dnx[:, :] = device.interptri(tri, vt, index_permutation_tri_x, x, z)
        Dnz[:, :] = device.interptri(tri, vt, index_permutation_tri_z, x, z)
        
        # Cancel out the E-field in the cladding/box region to Perturbate the index
        # only in the Wavegudie Region
        if (slab_thickness>0):
            filter1 =  ((X<simulation_span_x/2) & (X>wg_width/2)) | ((X>-simulation_span_x/2) & (X<-wg_width/2))
            filter1 = filter1 & (Z<slab_thickness) & (Z>0)
            
            filter2 = ((X<wg_width/2) & (X>-wg_width/2))
            filter2 = filter2 & ((Z<wg_thickness) & (Z>0))
           
            filter = filter1 | filter2

        else:
            filter = (X<wg_width/2) & (X>-wg_width/2)
            filter = filter & (Z<wg_thickness) & (Z>0)


        # Apply the filter at the index
        Dnx = (Dnx) * np.transpose(filter)
        Dnz = (Dnz) * np.transpose(filter)
        
        # Plot the Index Change       
        plt.figure(1)
        plt.pcolormesh(X*1e6, Z*1e6, np.transpose(abs(Dnz)), shading='gouraud', cmap='jet')
        cbar = plt.colorbar()
        cbar.set_label('$\Delta n_z$')
        plt.xlabel('x [um]')
        plt.ylabel('y [um]')
        plt.title('Vertical Index Perturbation')
        
        plt.figure(2)
        plt.pcolormesh(X*1e6, Z*1e6, np.transpose(abs(Dnx)), shading='gouraud', cmap='jet')
        cbar = plt.colorbar()
        cbar.set_label('$\Delta n_x$')
        plt.xlabel('x [um]')
        plt.ylabel('y [um]')
        plt.title('Horizontal Index Perturbation')
        
        # Plot the waveguide and slab regions
        wg_xmin = device.getnamed("waveguide", "x min")
        wg_xmax = device.getnamed("waveguide", "x max")
        r1 = sg.box(wg_xmin*1e6, 0, wg_xmax*1e6, wg_thickness*1e6)
        
        if slab_thickness > 0:
            # Add the slab
            slab_xmin = device.getnamed("slab", "x min")
            slab_xmax = device.getnamed("slab", "x max")
            r2 = sg.box(min(x)*1e6, 0, max(x)*1e6, slab_thickness*1e6)

            # Merge shapes
            merged_shape = so.unary_union([r1, r2])

            # Plot merged shape
            xs, ys = merged_shape.exterior.xy
            for i in range(1, 3):
                plt.figure(i)
                plt.axis('equal')
                plt.fill(xs, ys, alpha=0.5, fc='none', ec='r')
                file_name_plot = os.path.join(EO_MODULATOR_DIRECTORY_WRITE[0], f"Efield_{i}.png")
                plt.savefig(file_name_plot)
        else:
            # Plot waveguide only
            xs, ys = r1.exterior.xy
            for i in range(1, 3):
                plt.axis('equal')
                plt.figure(i)
                plt.fill(xs, ys, alpha=0.5, fc='none', ec='r')
                file_name_plot = os.path.join(EO_MODULATOR_DIRECTORY_WRITE[0], f"Efield_{i}.png")
                plt.savefig(file_name_plot)
