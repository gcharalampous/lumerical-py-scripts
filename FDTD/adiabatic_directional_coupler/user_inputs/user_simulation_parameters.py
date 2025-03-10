#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are required.

In this file, the user is must enter the parameters required to setup the
simulation file. The simulation parameters along with their dimensions are
presented below.


"""


# Length units are in meters!


# 1. Taper Parameters

taper_gap = 0.5e-6
taper_length = 100e-6




# # 1.1. Taper-bottom Parameters - Soyrce is attached on this taper
# wg_bottom_width_left = 1.20e-6
# wg_bottom_width_right = 0.25e-6
# wg_bottom_thickness = 0.2e-6

# wg_bottom_rib_thickness = 0.0e-6

# # 1.2. Taper-Top Parameters
# wg_top_width_left = 0.25e-6
# wg_top_width_right = 1.20e-6
# wg_top_thickness = 0.2e-6

# wg_top_rib_thickness = 0.0e-6


# # 2. FDTD Simulation Parameters

# # 2.1 FDTD Span Region
# simulation_span_y = 20e-6
# simulation_span_z = 20e-6
# simulation_time = 5e-12

# # 2.2.1. Mesh Settings 
# mesh_accuracy = 1

# # 2.2.2. Override Mesh Settings
# mesh_dx = 50e-9
# mesh_dy = wg_top_width_left/2
# mesh_dz = taper_gap/5
# enable_dx = 0
# enable_dy = 1
# enable_dz = 1


# # 2.3 Source/Monitor Properties
# wavelength_start = 1.2e-6
# wavelength_stop = 1.4e-6
# mode_fundamental = "TE"             # Select TE for fundamental TE or TM for fundamental TM
# frequency_points = 32

# # 2.4. Port extension
# port_extension = 5e-6


# # 3. Figures
# my_dpi = 96


# # -------------------------- End of Input Section -----------------------------


# if(mode_fundamental == "TE"):
#     mode_monitor = "fundamental TE mode"
# else:
#     mode_monitor = "fundamental TM mode"  
    
    

# if(mode_fundamental == "TE"):
#     mode_source = "fundamental TE mode"
# else:
#     mode_source = "fundamental TM mode"  
