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

def add_feem_region(device):

    # Add the mesh and the FDE regions
    device.addfeemsolver()
    device.addfeemmesh()
    device.addpec()

    
    
    configuration = (
        
     ("FEEM", 
              (("edges per wavelength", 4),
               ("wavelength", wavelength),
               ("number of trial modes", num_modes),
               ("polynomial order", 2))),
            
     
            
    ("simulation region",
             (("dimension", "2D Y-Normal"),
              ("x", 0.),
              ("z", 0.),
              ("y", 0.),
              ("x span", simulation_span_x),
              ("z min", simulation_min_z),
              ("z max", simulation_max_z),
              ("background material", background_material_e))),  
        
        
        
    ("FEEM::boundary conditions::PEC", 
             (("surface type", "simulation region"),
              ("x min", 1),
              ("x max", 1),
              ("y min", 1),
              ("y max", 1),
              ("z min", 1),
              ("z max", 1))),
           
    
    ("FEEM::mesh", 
             (("x", 0.),
              ("geometry type", "volume"),
              ("volume solid", "waveguide"),
              ("max edge length", max_edge_length_mesh_override),
              ("enabled", mesh_enable))),
           
    )
    
    

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               device.setnamed(obj, k, v)
               
               
               
               
if(__name__=="__main__"):
    with lumapi.DEVICE(hide=True) as device:
    
      # Draw the waveguide structure using a custom function
      device.redrawoff()
      waveguide_draw(device)
      
      # Draw the Simulation Region
      add_feem_region(device)


      device.save(EO_MODULATOR_DIRECTORY_WRITE_FILE + "\\eo_waveguide_render.ldev")


