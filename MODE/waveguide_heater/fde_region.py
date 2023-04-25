#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The purpose of this script is to take the parameters from the 
'simulation_parameters.py' file and render the FDE region

                                   
                                ^ y-axis               
                                |                      
                                |                      
                                |                      
                                |                      
                                |                      
                              z o ------------- >  x-axis
                                                                                                                                      
                                                         
                     +---------------------------------+                                                                                 
                     |  +---------------------------+  |                                                                                 
                     |  ||-------------------------||  |                                                                                 
                     |  ||       Claddding         ||  |                                                                       
                     |  ||      +----------+       ||  |                                                                                 
                     |  ||      |          |       ||  |                                                                                 
                     |  ||      |   Core   |       ||  |                                                                                 
                     |  ||      |          |       ||  |                                                                                 
                     +--||-------------------------||--+                                                                                 
                     |  ||           Box           ||  |                                                                                 
                     +--||-------------------------||--+                                                                                 
                     |  ||                         ||  |                                                                                 
                     |  ||                     FDE ||  |                                                                                 
                     |  ||-------------------------||  |                                                                                 
                     |  +---------------------------+  |                                                                                 
                     |            Substrate            |                                                                                 
                     +---------------------------------+                                                                                 
                                                                                                                                       
The dimensions of the FDE and mesh region are defined from the 
'user_simulation_parameters.py'. 

Remember to leave enough space within your FDE region to allow
the modes to decay enough avoiding interfering with the simulation
boundaries.

"""
#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from MODE.waveguide_heater.user_inputs.user_simulation_parameters import *  
from MODE.waveguide_heater.user_inputs.user_materials import *

c = 299792458

def add_fde_region(mode):

    # Add the mesh and the FDE regions
    mode.addmesh()
    mode.addfde()

    # Gets the index of the core
    if(is_wg_index):
      n = wg_index
    else:
      n = mode.getindex(wg_material, c/wavelength)

    configuration = (
    ("mesh", (("dx", mesh_dx),
              ("dy", mesh_dy),
              ("x", 0.),
              ("y min", 0.),
              ("x span", wg_width),
              ("y max", wg_thickness))),    
    
    ("FDE", (("x", 0.),
             ("y", 0.),
             ("z", 0.),
             ("x span", simulation_span_x),
             ("y min", simulation_min_y),
             ("y max", simulation_max_y),
             ("mesh cells x", fde_mesh_cell_x),
             ("mesh cells y", fde_mesh_cell_y),
             ("solver type","2D Z normal"),
             ("wavelength",wavelength),
             ("number of trial modes",num_modes),
             ("use max index", False),
             ("search", "near n"),
             ("n", n),
             ("bent waveguide",bend_waveguide),
             ("bend radius",bend_radius),
             ("bend orientation",bend_orientation))),  
    )

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               mode.setnamed(obj, k, v)

