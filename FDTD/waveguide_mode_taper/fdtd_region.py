#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.



The script sets the FDTD region for the taper waveguide simulation.

There are in total

1.  A mode source
2.  FDTD Region
3.  2D_xz: A 2D side-view monitor
4.  2D_xy: A 2D top-view monitor
5.  linear_y: A 1D monitor across y-direction
6.  linear_z: A 1D monitor across z-direction
7.  transmission: A transmission monitor
8.  monitor_exp: An expansion monitor
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from FDTD.waveguide_mode_taper.user_inputs.user_simulation_parameters import *  


def add_fdtd_region(fdtd,taper_length):

    # Add the mesh and the FDE regions
    fdtd.addmode()
    fdtd.addfdtd()
    
    fdtd.addprofile()
    fdtd.set("name","2D_xz")
    
    fdtd.addprofile()
    fdtd.set("name","2D_xy")
    
    fdtd.addprofile()
    fdtd.set("name","linear_y")
    
    fdtd.addprofile()
    fdtd.set("name","linear_z")    
        
    fdtd.addpower()
    fdtd.set("name","transmission")
    
    fdtd.addmodeexpansion()
    fdtd.set("name","monitor_exp")
    fdtd.setexpansion("input", "transmission")
    
    
    
    
    configuration = (
    ("source",      (("mode selection", mode_source),
                     ("injection axis", "x"),
                     ("x", -offset_x/2),
                     ("y", 0.),
                     ("z", 0.),
                     ("y span", simulation_span_y),
                     ("z span", simulation_span_z),
                     ("wavelength start", wavelength_start),
                     ("wavelength stop", wavelength_stop))),
    
    
   ("2D_xz",        (("monitor type", 6),
                     ("x min", -2*offset_x),
                     ("x max", taper_length + 2*offset_x),
                     ("y", 0.),
                     ("z", 0.),
                     ("z span", simulation_span_z))),
   
     
   ("2D_xy",        (("monitor type", 7),
                     ("x min", -2*offset_x),
                     ("x max", taper_length + 2*offset_x),
                     ("y", 0),
                     ("y span", simulation_span_y),                     
                     ("z", wg_thickness/2))),
   
    
    ("transmission",(("monitor type", 5),
                     ("x", taper_length + offset_x - offset_x/2),
                     ("y", 0.),
                     ("z", 0.),
                     ("y span", simulation_span_y),
                     ("z span", simulation_span_z))),
    
    ("linear_y",    (("monitor type", 3),
                     ("x", taper_length + offset_x - offset_x/2),
                     ("y", 0.),
                     ("z", wg_thickness/2),
                     ("y span", simulation_span_y))),
        
    ("linear_z",    (("monitor type", 4),
                     ("x", taper_length + offset_x - offset_x/2),
                     ("y", 0.),
                     ("z", 0),
                     ("z span", simulation_span_z))),
   
    
    ("monitor_exp", (("mode selection", mode_monitor),
                     ("x", taper_length + offset_x - offset_x/2),
                     ("y", 0.),
                     ("z", 0.),
                     ("y span", simulation_span_y),
                     ("z span", simulation_span_z))),
    
     
    ("FDTD",        (("x min", -offset_x),
                     ("x max", taper_length + offset_x),
                     ("y", 0.),
                     ("z", 0.),
                     ("y span", simulation_span_y),
                     ("z span", simulation_span_z),
                     ("simulation time", simulation_time),
                     ("mesh accuracy",mesh_accuracy))),
    
    )

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               fdtd.setnamed(obj, k, v)

