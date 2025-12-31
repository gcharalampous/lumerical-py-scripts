#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.


The purpose of this script is to take the parameters from the 'materials.py'
and 'simulation_parameters.py' and render the 3D structure below

----- 2D Cross-section
                                   
        ^ z-axis               
        |                      
        |                      
        |                      
        |                      
        |                      
      x o ------------- >  y-axis

        +--------------------------------+                          
        |           Claddding            |                          
        |                                |                        
        |         +-----------+          |                          
        |         |           |          |                          
        |         | waveguide |          |                          
        |         |           |          |                          
        +--------------------------------+                          
        |               Box              |                          
        +--------------------------------+                          
        |                                |                          
        |           Substrate            |                          
        |                                |                          
        +--------------------------------+                          
                                                                               
----- 2D Top-down View
                                                                               
        ^ y-axis               
        |                      
        |                      
        |                      
        |                      
        |                      
      z o ------------- >  x-axis

                                                                                                                                                              
      +----------------------------------------------------------------+                                                                                       
      |                                                                |                                                                                       
      |                            Cladding                            |                                                                                       
      |                                                                |                                                                                       
      |----------------------------------------------------------------|                                                                                       
      |                           Waveguide                            |                                                                                       
      |----------------------------------------------------------------|                                                                                       
      |                                                                |                                                                                       
      |                                                                |                                                                                       
      +----------------------------------------------------------------+       



----- 2D Side-View
                                                                               
        ^ z-axis               
        |                      
        |                      
        |                      
        |                      
        |                      
      y o ------------- >  x-axis

                                                                                                                                                              
      +----------------------------------------------------------------+                                                                                       
      |                                                                |                                                                                       
      |                            Cladding                            |                                                                                       
      |                                                                |                                                                                       
      |----------------------------------------------------------------|                                                                                       
      |                           Waveguide                            |                                                                                       
      |----------------------------------------------------------------|                                                                                       
      |                                                                |                                                                                       
      |                                                                |                                                                                       
      +----------------------------------------------------------------+       




"""


#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from user_inputs.user_simulation_parameters import *  
from user_inputs.user_materials import *

def waveguide_draw(fdtd):
    
    # Adds the four rectangulars shown above

    fdtd.addrect(name = "waveguide")
    fdtd.addrect(name = "cladding")
    fdtd.addrect(name = "box")
    fdtd.addrect(name = "substrate")



    # Set the parameters of each structure from the user file

    configuration = (
    ("waveguide", (("x min", -2*offset_x),
                   ("x max", wg_length + offset_x),
                   ("y", 0.),
                   ("y span", wg_width),
                   ("z min", 0.),
                   ("z max", wg_thickness),
                   ("index",wg_index),
                   ("material",wg_material),
                   ("override mesh order from material database",1),
                   ("mesh order",2))),
    
    
    ("cladding",  (("x min", -2*offset_x),
                   ("x max", wg_length + offset_x),
                   ("y", 0.),
                   ("y span", simulation_span_y),
                   ("z min", clad_min_z),
                   ("z max", clad_max_z),
                   ("index",clad_index),
                   ("material",clad_material),
                   ("override mesh order from material database",1),
                   ("mesh order",3),
                   ("render type","wireframe"))),
    
    ("box",       (("x min", -2*offset_x),
                   ("x max", wg_length + offset_x),
                   ("y", 0.),
                   ("y span", simulation_span_y),
                   ("z min", clad_min_z- box_thickness),
                   ("z max", clad_min_z),
                   ("index", box_index),
                   ("material",box_material),
                   ("override mesh order from material database",1),
                   ("mesh order",3),
                   ("render type","wireframe"))),
    
    
     ("substrate",(("x min", -2*offset_x),
                   ("x max", wg_length + offset_x),
                   ("y", 0.),
                   ("y span", simulation_span_y),
                   ("z min", clad_min_z - box_thickness - sub_thickness),
                   ("z max", clad_min_z - box_thickness),
                   ("index", sub_index),
                   ("material",sub_material),
                   ("override mesh order from material database",1),
                   ("mesh order",3),
                   ("render type","wireframe"))),   
        
    )


    # Populate the 2D waveguide
    
    for obj, parameters in configuration:
           for k, v in parameters:
               fdtd.setnamed(obj, k, v)    




