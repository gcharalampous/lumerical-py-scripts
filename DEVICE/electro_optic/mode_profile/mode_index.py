#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The purpose of this script is to take the parameters from the 


"""
import lumapi
from config import *


#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from DEVICE.electro_optic.user_inputs.user_simulation_parameters import *  
from DEVICE.electro_optic.user_inputs.user_materials import *  
from DEVICE.electro_optic.waveguide_render import waveguide_draw
from DEVICE.electro_optic.feem_region import add_feem_region
from DEVICE.electro_optic.charge_region import add_charge_region
from DEVICE.electro_optic.electrostatics.get_index_change_2D import *
from scipy.io import savemat

def get_neff(device):
    # neff = np.zeros(num_modes)
    
    mode_result = device.getresult("FEEM","modeproperties")
    neff = mode_result['neff']
    
    return neff


def get_dneff(device):
    
    
    # Get the electric field data
    E, x_tri, z_tri, tri = get_Efield_static_2D(device)
    E_2D = np.delete(E, 1, axis=1)  # Remove y-component
    
    # Extract x and z components of electric field
    Ex_tri, Ez_tri = E_2D[:, 0], E_2D[:, 1]
        
    index_permutation_tri_x, index_permutation_tri_z = index_permutation(
        Ex=Ex_tri, Ez=Ez_tri, wg_index_x=wg_index, wg_index_z=wg_index )

    
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
    
    y_tri = np.zeros(len(z_tri))
    
    nkmaterial = device.unstructureddataset("nk import", x_tri, y_tri, z_tri, tri);

    device.select("FEEM::nk import")    
    device.importdataset(nkmaterial)    
    
    
    # Creating a single dictionary with all key-value pairs
    dn_tri = np.zeros((len(x_tri), 3))
    dn_tri[:, 0] = index_permutation_tri_x
    dn_tri[:, 1] = index_permutation_tri_x*0
    dn_tri[:, 2] = index_permutation_tri_z
    
    
    data = {
        'dn_tri': dn_tri,
        'x_tri': x_tri,
        'y_tri': y_tri,
        'z_tri': z_tri,
        'elements': tri
    }
    

    
    # Saving the data to a MATLAB file
    savemat(EO_MODULATOR_DIRECTORY_WRITE_FILE + '\\nk_region.mat', data)

    return Dnx, Dnz



if(__name__=="__main__"):
    with lumapi.DEVICE(hide=True) as device:
    
        # Draw the waveguide structure using a custom function
        device.redrawoff()
        waveguide_draw(device)
        
        # Draw the Simulation Region
        add_feem_region(device)
        add_charge_region(device)
      
    
    
          
        # Save and run the simulation
        device.save(EO_MODULATOR_DIRECTORY_WRITE_FILE + "\\eo_waveguide_simulation.ldev")
        
        # get the mode properties
        device.run("FEEM")
        neff_o  = get_neff(device)
      
        
      



        # device.switchtolayout()
        # device.addimportnk()

        # device.run("CHARGE")
        # Dnx, Dnz = get_dneff(device)

        # # get the dn
        # device.switchtolayout()
        # device.save(EO_MODULATOR_DIRECTORY_WRITE_FILE + "\\eo_waveguide_simulation.ldev")

        # # Add nk import

        # device.setnamed("FEEM::nk import","volume type","solid")
        # device.setnamed("FEEM::nk import","volume solid","waveguide")
        # device.feval(EO_MODULATOR_DIRECTORY_WRITE_FILE + '\\eo_waveguide_simulation.lsf')

      
      


      
      
      