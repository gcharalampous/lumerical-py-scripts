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
the devices to decay enough avoiding interfering with the simulation
boundaries.

"""
import lumapi
from config import *


#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from DEVICE.electro_optic.user_inputs.user_simulation_parameters import *  
from DEVICE.electro_optic.user_inputs.user_materials import *  
from DEVICE.electro_optic.waveguide_render import waveguide_draw

def add_charge_region(device):

    # Add the mesh and the FDE regions
    device.addchargesolver()
    device.addchargemesh()
    
    # Adds the anode and cathode
    device.addelectricalcontact(name = "ground_left")
    device.addelectricalcontact(name = "signal")
    device.addelectricalcontact(name = "ground_right")

    # Monitors
    device.addefieldmonitor(name = "electric_monitor")

    
    configuration = (
        
    ("CHARGE", 
              (("min edge length", min_edge_length),
              ("max edge length", max_edge_length))),

        
    ("CHARGE::mesh", 
             (("x", 0.),
              ("y", 0),
              ("z min", 0.),
              ("x span", wg_width),
              ("z max", wg_thickness),
              ("max edge length", max_edge_length_mesh_override),
              ("enabled", mesh_enable))),
    
    ("simulation region",
             (("dimension", "2D Y-Normal"),
              ("x", 0.),
              ("z", 0.),
              ("y", 0.),
              ("x span", simulation_span_x),
              ("z min", simulation_min_z),
              ("z max", simulation_max_z),
              ("background material", background_material))),  
        
    ("CHARGE::boundary conditions::ground_left",
             (("bc mode", "steady state"),
              ('sweep type', 'single'),
              ('voltage', 0),
              ("surface type", "solid"),
              ("solid", "metal_left"))),
    
    ("CHARGE::boundary conditions::signal",
             (("bc mode", "steady state"),
              ('sweep type', 'single'),
              ('voltage', v_signal),
              ("surface type", "solid"),
              ("solid", "metal_center"))),
    
    ("CHARGE::electric_monitor",
             (("monitor type", 6),
              ("x", 0.),
              ("y", 0.),
              ("z", 0.),
              ("x span", simulation_span_x),
              ("z min", simulation_min_z),
              ("z max", simulation_max_z))),


    ("CHARGE::boundary conditions::ground_right",
             (("bc mode", "steady state"),
              ('sweep type', 'single'),
              ('voltage', 0),
              ("surface type", "solid"),
              ("solid", "metal_right"))),
     
    
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
      add_charge_region(device)


      device.save(EO_MODULATOR_DIRECTORY_WRITE_FILE + "\\eo_waveguide_render.ldev")


