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
import pandas as pd

# Define grid dimensions (Reduce for Quiver plot if necessary)
N_x = 100
N_z = 100

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
    with lumapi.DEVICE(hide=False) as device:
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
        
        # Define grid
        x = np.linspace(-simulation_span_x/2, simulation_span_x/2, N_x)
        y = 0
        z = np.linspace(simulation_min_z, simulation_max_z, N_z)
        X, Z = np.meshgrid(x, z)
        
        Ex = np.zeros((N_x, N_z))
        Ez = np.zeros((N_x, N_z))
        
        vt = np.zeros((len(x_tri), 2))
        vt[:, 0] = x_tri
        vt[:, 1] = z_tri
        
        Ex[:, :] = device.interptri(tri, vt, Ex_tri, x, z)
        Ez[:, :] = device.interptri(tri, vt, Ez_tri, x, z)
        
        # Plot the electric field
        plt.figure(1,figsize=(5.12,2.56))
        plt.quiver(X*1e6, Z*1e6, np.transpose(Ex), np.transpose(Ez))
        plt.xlabel('x [um]')
        plt.ylabel('z [um]')
        
        plt.figure(2,figsize=(5.12,2.56))
        plt.pcolormesh(X*1e6, Z*1e6, np.transpose(abs(Ez)*1e-3), shading='gouraud', cmap='jet', norm=LogNorm())
        cbar = plt.colorbar()
        cbar.set_label('E-field [kV/m]')
        plt.xlabel('x [um]')
        plt.ylabel('z [um]')
        plt.title('Vertical Component $|E_z|$')
        
        plt.figure(3,figsize=(5.12,2.56))
        plt.pcolormesh(X*1e6, Z*1e6, np.transpose(abs(Ex)*1e-3), shading='gouraud', cmap='jet', norm=LogNorm())
        cbar = plt.colorbar()
        cbar.set_label('E-field [kV/m]')
        plt.xlabel('x [um]')
        plt.ylabel('z [um]')
        plt.title('Horizontal Component $|E_x|$')
        
        # Plot the waveguide and slab regions
        wg_xmin = device.getnamed("waveguide", "x min")
        wg_xmax = device.getnamed("waveguide", "x max")
        r1 = sg.box(wg_xmin*1e6, 0, wg_xmax*1e6, wg_thickness*1e6)
        
        # Optionally set axis limits for all plots
        set_axis_limits = True  # Set to False if you don't want to define limits
        if set_axis_limits:
            xlim = (-2*wg_width*1e6, 2*wg_width*1e6)
            ylim = (-wg_thickness*1e6, wg_thickness*1e6)
            for i in range(1, 4):
                plt.figure(i)
                plt.axis('equal')
                plt.xlim(xlim)
                plt.ylim(ylim)
        
        if slab_thickness > 0:
            # Add the slab
            # slab_xmin = device.getnamed("slab", "x min")
            # slab_xmax = device.getnamed("slab", "x max")
            r2 = sg.box(min(x)*1e6, 0, max(x)*1e6, slab_thickness*1e6)

            # Merge shapes
            merged_shape = so.unary_union([r1, r2])

            # Plot merged shape
            xs, ys = merged_shape.exterior.xy
            for i in range(1, 4):
                plt.figure(i)
                plt.fill(xs, ys, alpha=0.5, fc='none', ec='k')
                file_name_plot = os.path.join(EO_MODULATOR_DIRECTORY_WRITE[0], f"Efield_{i}.png")
                plt.savefig(file_name_plot)
        else:
            # Plot waveguide only
            xs, ys = r1.exterior.xy
            for i in range(1, 4):
                plt.figure(i)
                plt.fill(xs, ys, alpha=0.5, fc='none', ec='k')
                file_name_plot = os.path.join(EO_MODULATOR_DIRECTORY_WRITE[0], f"Efield_{i}.png")
                plt.savefig(file_name_plot)

        # Export the data for the horizontal and vertical components |E_x| and |E_z| to a CSV file
        # Ex and Ez are already on the (x, z) meshgrid, matching X and Z.
        # Prepare data for CSV export
        # Save the full 2D arrays for Ex and Ez as CSV files
        np.savetxt(
            os.path.join(EO_MODULATOR_DIRECTORY_WRITE[0], f"Efield_Ex_v_signal_{v_signal}V.csv"),
            abs(Ex.T) * 1e-3,
            delimiter=","
        )
        np.savetxt(
            os.path.join(EO_MODULATOR_DIRECTORY_WRITE[0], f"Efield_Ez_v_signal_{v_signal}V.csv"),
            abs(Ez.T) * 1e-3,
            delimiter=",",
        )
        # df = pd.DataFrame(csv_data)
        # csv_file = os.path.join(EO_MODULATOR_DIRECTORY_WRITE[0], f"Efield_Ex_Ez_v_signal_{v_signal}V.csv")
        # df.to_csv(csv_file, index=False)