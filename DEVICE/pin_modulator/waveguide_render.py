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

from DEVICE.pin_modulator.user_inputs.user_simulation_parameters import *  
from DEVICE.pin_modulator.user_inputs.user_materials import *

def waveguide_draw(device):
    


    # # Adds the material for the Doping Section
    # p_material = "P++"
    # temp = device.addmaterial("(n,k) Material")
    # device.setmaterial(temp, "name",p_material)
    # device.setmaterial(p_material,{"Refractive Index": slab_index, "Imaginary Refractive Index": k_P})


    # n_material = "N++"
    # temp = device.addmaterial("(n,k) Material")
    # device.setmaterial(temp, "name",n_material)
    # device.setmaterial(n_material,{"Refractive Index": slab_index, "Imaginary Refractive Index": k_N})
    

    # Adds the waveguide rectangles and metal layers

    device.addrect(name = "waveguide")
    device.addrect(name = "cladding")
    device.addrect(name = "box")
    device.addrect(name = "slab")
    device.addrect(name = "plateau_left")
    device.addrect(name = "plateau_right")
    device.addrect(name = "metal_anode")
    device.addrect(name = "metal_cathode")




    # device.addrect(name = "slab_P++")
    # device.addrect(name = "slab_N++")




    # Add Materials
    for material in unique_material_list:    
    
        device.addmodelmaterial()
        device.setnamed("materials::New Material","name", material)
        device.addmaterialproperties("CT", material)




    if(slab_thickness>0):
      slab_enable  = 1
    else:
      slab_enable = 0



    # Set the parameters of each structure from the user file

    configuration = (
    ("waveguide", (("x", 0.),
                    ("y min", slab_thickness),
                    ("z", 0.),
                    ("x span", wg_width),
                    ("y max", wg_thickness),
                    ("z span", 5e-6),
                    ("material", wg_material),
                    ("mole frac constant", wg_mole_fract))),
    
    ("slab",       (("x min", -simulation_span_x/2 + plateau_width),
                    ("y min", 0.),
                    ("z", 0.),
                    ("x max", simulation_span_x/2 - plateau_width),
                    ("y max", slab_thickness),
                    ("z span", 5e-6),
                    ("enabled", slab_enable),
                    ("material", wg_material))),
    
    ("plateau_left",(("x min", -simulation_span_x/2),
                    ("y min", 0),
                    ("z", 0.),
                    ("x max", -simulation_span_x/2 + plateau_width),
                    ("y max", plateau_thickness),
                    ("z span", 5e-6),
                    ("material", wg_material))),   

    ("plateau_right",(("x min", simulation_span_x/2 - plateau_width),
                    ("y min", 0),
                    ("z", 0.),
                    ("x max", simulation_span_x/2),
                    ("y max", plateau_thickness),
                    ("z span", 5e-6),
                    ("material", wg_material))),   

    ("metal_anode",(("x min", -simulation_span_x/2),
                    ("y min", plateau_thickness),
                    ("z", 0.),
                    ("x max", -simulation_span_x/2 + metal_anode_width),
                    ("y max", simulation_max_y/4),
                    ("z span", 5e-6),
                    ("material", contact_material),
                    ("enabled", True))),        

    ("metal_cathode",(("x min", simulation_span_x/2 - metal_cathode_width),
                    ("y min", plateau_thickness),
                    ("z", 0.),
                    ("x max", simulation_span_x/2),
                    ("y max", simulation_max_y/4),
                    ("z span", 5e-6),
                    ("material", contact_material),
                    ("enabled", True))),      

    ("cladding",  (("x", 0.),
                    ("y", 0.),
                    ("x span", simulation_span_x),
                    ("y min", clad_min_y),
                    ("y max", clad_max_y),
                    ("z span", 5e-6),
                    ("material", oxide_material),
                    ("mesh order",3),
                    ("render type","wireframe"))),

    ("box",       (("x", 0.),
                    ("z", 0.),
                    ("x span", simulation_span_x),
                    ("y min", clad_min_y- box_thickness),
                    ("y max", clad_min_y),
                    ("z span", 5e-6),
                    ("material", oxide_material),
                    ("mesh order",3),
                    ("render type","wireframe"))),

    )


    # Populate the 2D waveguide structure
    
    for obj, parameters in configuration:
            for k, v in parameters:
                device.setnamed(obj, k, v)    




if(__name__=="__main__"):
    with lumapi.DEVICE(hide=True) as device:
    
      # Draw the waveguide structure using a custom function
      device.redrawoff()
      waveguide_draw(device)

      device.save(PIN_MODULATOR_DIRECTORY_WRITE_FILE + "\\pin_waveguide_render.ldev")

