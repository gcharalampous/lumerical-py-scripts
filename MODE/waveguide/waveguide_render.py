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

import lumapi
from config import *


#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from MODE.waveguide.user_inputs.user_simulation_parameters import *  
from MODE.waveguide.user_inputs.user_materials import *

def waveguide_draw(mode):
    


    # Adds the material for the Doping Section
    p_material = "P++"
    temp = mode.addmaterial("(n,k) Material")
    mode.setmaterial(temp, "name",p_material)
    mode.setmaterial(p_material,{"Refractive Index": slab_index, "Imaginary Refractive Index": k_P})


    n_material = "N++"
    temp = mode.addmaterial("(n,k) Material")
    mode.setmaterial(temp, "name",n_material)
    mode.setmaterial(n_material,{"Refractive Index": slab_index, "Imaginary Refractive Index": k_N})
    
    silicon_np = "silicon_np"
    temp = mode.addmaterial("Index perturbation")
    mode.setmaterial(temp, "name",silicon_np)
    mode.setmaterial(silicon_np, "np density model", "Soref and Bennett"); # use "Soref" model type
    mode.setmaterial(silicon_np, "Base Material", "Si (Silicon) - Palik"); # use "Silicon" model type
    
    # Adds the four rectangulars shown above

    mode.addrect(name = "waveguide")
    mode.addrect(name = "cladding")
    mode.addrect(name = "box")
    mode.addrect(name = "substrate")
    mode.addrect(name = "slab")
    mode.addrect(name = "slab_P++")
    mode.addrect(name = "slab_N++")
    mode.addgridattribute("np density");

    if(slab_thickness>0):
      slab_enable  = 1
    else:
      slab_enable = 0



    # Set the parameters of each structure from the user file

    configuration = (
    ("waveguide", (("x", 0.),
                   ("y min", 0),
                   ("z", 0.),
                   ("x span", wg_width),
                   ("y max", wg_thickness),
                   ("z span", 5e-6),
                   ("index",wg_index),
                   ("material",wg_material),
                   ("override mesh order from material database",1),
                   ("mesh order",2))),
    
    ("slab",       (("x", 0.),
                   ("y min", 0.),
                   ("z", 0.),
                   ("x span", simulation_span_x),
                   ("y max", slab_thickness),
                   ("z span", 5e-6),
                   ("index",slab_index),
                   ("material",slab_material),
                   ("enabled", slab_enable),
                   ("override mesh order from material database",1))),

    ("slab_P++",  (("x min", -simulation_span_x/2),
                   ("x max", -offset_P),
                   ("y min", 0.),
                   ("z", 0.),
                   ("y max", slab_thickness),
                   ("z span", 5e-6),
                   ("index",slab_index),
                   ("material",p_material),
                   ("enabled", doping_enable),
                   ("override mesh order from material database",1))),
    
    ("slab_N++",  (("x min", offset_N),
                   ("x max", simulation_span_x/2),
                   ("y min", 0.),
                   ("z", 0.),
                   ("y max", slab_thickness),
                   ("z span", 5e-6),
                   ("index",slab_index),
                   ("material",n_material),
                   ("enabled", doping_enable),
                   ("override mesh order from material database",1))),


    ("cladding",  (("x", 0.),
                   ("y", 0.),
                   ("x span", simulation_span_x + 1e-6),
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
                   ("x span", simulation_span_x + 1e-6),
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
                   ("x span", simulation_span_x + 1e-6),
                   ("y min", clad_min_y - box_thickness - sub_thickness),
                   ("y max", clad_min_y - box_thickness),
                   ("z span", 5e-6),
                   ("index", sub_index),
                   ("material",sub_material),
                   ("override mesh order from material database",1),
                   ("mesh order",3),
                   ("render type","wireframe"))),   
     
     
     ("np density",(("enabled", False),
                   ("x",0))),   
     
        
    )


    # Populate the 2D waveguide structure
    
    for obj, parameters in configuration:
           for k, v in parameters:
               mode.setnamed(obj, k, v)    




if(__name__=="__main__"):
    with lumapi.MODE(hide=True) as mode:
    
      # Disable Rendering
      mode.redrawoff()

      # Draw the waveguide structure using a custom function
      waveguide_draw(mode)

      # Turn redraw back on and close LumAPI connection
      mode.redrawon()        

      mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_modes.lms")
      
