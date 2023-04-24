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
                     |  ||+----------------+       ||  |                                                                                 
                     |  ||                 |       ||  |                                                                                 
                     |  ||          Core   |       ||  |                                                                                 
                     |  ||                 |       ||  |                                                                                 
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

from MODE.disk_waveguide.user_inputs.user_simulation_parameters import *  


def add_fde_region(mode):

    # Add the mesh and the FDE regions
    mode.addmesh()
    mode.addfde()

    
    configuration = (
    ("mesh", (("dx", mesh_dx),
              ("dy", mesh_dy),
              ("x min", -simulation_span_x/2),
              ("x max", 0),
              ("y min", 0.),
              ("y max", wg_thickness))),    
    
    ("FDE", (("x", 0.),
             ("y", 0.),
             ("z", 0.),
             ("x span", simulation_span_x),
             ("y span", simulation_span_y),
             ("mesh cells x", fde_mesh_cell_x),
             ("mesh cells y", fde_mesh_cell_y),
             ("x min bc",bc_xmin),
             ("x max bc",bc_xmax),
             ("y min bc",bc_ymin),
             ("y max bc",bc_ymax),
             ("solver type","2D Z normal"),
             ("wavelength",wavelength),
             ("number of trial modes",num_modes),
             ("bent waveguide",bend_waveguide),
             ("bend radius",bend_radius),
             ("bend orientation",bend_orientation))),  
    )

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               mode.setnamed(obj, k, v)

