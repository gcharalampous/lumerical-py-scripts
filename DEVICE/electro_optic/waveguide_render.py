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

from DEVICE.electro_optic.user_inputs.user_simulation_parameters import *  
from DEVICE.electro_optic.user_inputs.user_materials import *

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
    device.addrect(name = "metal_left")
    device.addrect(name = "metal_center")
    device.addrect(name = "metal_right")



    # Add Materials
    for material in unique_material_list:    
    
        device.addmodelmaterial()
        device.setnamed("materials::New Material","name", material)
        device.addmaterialproperties("CT", material)




    if(slab_thickness>0):
      slab_enable  = 1
    else:
      slab_enable = 0


    if(GSG_pads_enable):
        pads_pitch = metal_pitch
    else:
        pads_pitch = metal_pitch/2



    # Set the parameters of each structure from the user file

    configuration = (
    ("waveguide", (("x", 0.),
                    ("z min", slab_thickness),
                    ("y", 0.),
                    ("x span", wg_width),
                    ("z max", wg_thickness),
                    ("y span", 5e-6),
                    ("material", wg_material),
                    ("mole frac constant", wg_mole_fract))),
    
    ("slab",       (("x min", -simulation_span_x/2 - 0.5e-6),
                    ("z min", 0.),
                    ("y", 0.),
                    ("x max", simulation_span_x/2 + 0.5e-6),
                    ("z max", slab_thickness),
                    ("y span", 5e-6),
                    ("enabled", slab_enable),
                    ("material", wg_material))),
    
    ("metal_left", (("x", -pads_pitch),
                    ("z min", clad_max_y),
                    ("y", 0.),
                    ("x span", metal_left_width),
                    ("z max", clad_max_y + metal_thicknes),
                    ("y span", 5e-6),
                    ("material", contact_material),
                    ("enabled", True))),        

    ("metal_center",(("x", 0),
                    ("z min", clad_max_y),
                    ("y", 0.),
                    ("x span", metal_center_width),
                    ("z max", clad_max_y + metal_thicknes),
                    ("y span", 5e-6),
                    ("material", contact_material),
                    ("enabled", GSG_pads_enable))),      


    ("metal_right",(("x", pads_pitch),
                    ("z min", clad_max_y),
                    ("y", 0.),
                    ("x span", metal_right_width),
                    ("z max", clad_max_y + metal_thicknes),
                    ("y span", 5e-6),
                    ("material", contact_material),
                    ("enabled", True))),      

    ("cladding",  (("x", 0.),
                    ("z", 0.),
                    ("x span", simulation_span_x + 1e-6),
                    ("z min", clad_min_y),
                    ("z max", clad_max_y),
                    ("y span", 5e-6),
                    ("material", oxide_material),
                    ("mesh order",3),
                    ("render type","wireframe"))),

    ("box",       (("x", 0.),
                    ("y", 0.),
                    ("x span", simulation_span_x + 1e-6),
                    ("z min", clad_min_y- box_thickness - 0.5e-6),
                    ("z max", clad_min_y),
                    ("y span", 5e-6),
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

      device.save(EO_MODULATOR_DIRECTORY_WRITE_FILE + "\\eo_waveguide_render.ldev")

