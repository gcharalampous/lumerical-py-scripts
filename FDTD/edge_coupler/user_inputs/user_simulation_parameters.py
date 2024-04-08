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

taper_length = 100e-6




# 1.1. Taper-bottom Parameters - Soyrce is attached on this taper
wg_width_left = 0.25e-6
wg_width_right = 0.50e-6
wg_thickness = 0.30e-6

slab_thickness = 0.0e-6



# 2. FDTD Simulation Parameters

# 2.1 FDTD Span Region
simulation_span_y = 20e-6
simulation_span_z = 20e-6
simulation_time = 5e-12

# 2.2.1. Mesh Settings 
mesh_accuracy = 1

# 2.2.2. Override Mesh Settings
mesh_dx = 50e-9
mesh_dy = wg_width_left/2
mesh_dz = 50e-9
enable_dx = 0
enable_dy = 1
enable_dz = 0


# 2.3 Source/Monitor Properties
waist_radius = 1.25e-6
wavelength_start = 1.55e-6 - (25.6/2)*1e-9
wavelength_stop = 1.55e-6 + (25.6/2)*1e-9
mode_fundamental = "TE"             # Select TE for fundamental TE or TM for fundamental TM
frequency_points = 32

# 2.4. Port extension
port_extension = 5e-6


# 3. Figures
my_dpi = 96


# -------------------------- End of Input Section -----------------------------


if(mode_fundamental == "TE"):
    mode_monitor = "fundamental TE mode"
else:
    mode_monitor = "fundamental TM mode"  
    
    

if(mode_fundamental == "TE"):
    mode_source = 0
else:
    mode_source = 90
