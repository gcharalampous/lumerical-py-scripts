#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The purpose of this script is to take the parameters from the 'materials.py'
and 'simulation_parameters.py' and render the structure below

                                   
                                ^ y-axis               
                                |                      
                                |                      
                                |                      
                                |                      
                                |                      
                              z o ------------- >  x-axis

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
                                                                               
                                                                               

The 2D waveguide is rendered on the 'y' and 'x' axis while the 'z' axis 
remains the propagation. The z-axis is not used during mode simulations.


"""
#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from MODE.edge_coupler.user_inputs.user_simulation_parameters import *  
from MODE.edge_coupler.user_inputs.user_materials import *

def waveguide_draw(mode):
    
    # Adds the four rectangulars shown above

    mode.addrect(name = "waveguide")
    mode.addrect(name = "cladding")
    mode.addrect(name = "box")
    mode.addrect(name = "substrate")



    # Set the parameters of each structure from the user file

    configuration = (
    ("waveguide", (("x", 0.),
                   ("y min", 0.),
                   ("z", 0.),
                   ("x span", wg_width),
                   ("y max", wg_thickness),
                   ("z span", 5e-6),
                   ("index",wg_index),
                   ("material",wg_material),
                   ("override mesh order from material database",1),
                   ("mesh order",2))),
    
    
    ("cladding",  (("x", 0.),
                   ("y", 0.),
                   ("x span", simulation_span_x),
                   ("y min", clad_min_y),
                   ("y max", clad_max_y),
                   ("z span", 5e-6),
                   ("index",clad_index),
                   ("material",clad_material),
                   ("override mesh order from material database",1),
                   ("mesh order",3),
                   ("render type","wireframe"))),
    
    ("box",       (("x", 0.),
                   ("z", 0.),
                   ("x span", simulation_span_x),
                   ("y min", clad_min_y- box_thickness),
                   ("y max", clad_min_y),
                   ("z span", 5e-6),
                   ("index", box_index),
                   ("material",box_material),
                   ("override mesh order from material database",1),
                   ("mesh order",3),
                   ("render type","wireframe"))),
    
    
     ("substrate",(("x", 0.),
                   ("z", 0.),
                   ("x span", simulation_span_x),
                   ("y min", clad_min_y - box_thickness - sub_thickness),
                   ("y max", clad_min_y - box_thickness),
                   ("z span", 5e-6),
                   ("index", sub_index),
                   ("material",sub_material),
                   ("override mesh order from material database",1),
                   ("mesh order",3),
                   ("render type","wireframe"))),   
        
    )


    # Populate the 2D waveguide structure
    
    for obj, parameters in configuration:
           for k, v in parameters:
               mode.setnamed(obj, k, v)    




