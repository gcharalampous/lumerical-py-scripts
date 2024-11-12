#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User Inputs Required

This file contains the parameters necessary to set up the simulation. 
Users must input the required values to configure the simulation environment. 
The parameters and their respective units are listed below.
"""

# Length units are in meters!

# 1. Simulation Parameters
simulation_min_y = -5.0e-6

# 2. Cladding Dimensions. Note, waveguide y min = 0.
cladding_thickness = 1.5e-6

# 3. Waveguide Dimensions - Slab Waveguide
wg_thickness = 0.22e-6

# 3.1 Set slab thickness > 0 to enable a slab waveguide
slab_thickness = 0.110e-6

# 4. Box Layer Thickness
box_thickness = 3.0e-6

# 5. Substrate Layer Thickness
sub_thickness = 10e-6

# 6. Grating Coupler Parameters
period = 0.657e-6                        # Grating Period
fill_factor = 0.5                       # Fill Factor
gc_sections = 50                        # Number of Gratings Sections
port_extension = 15.0e-6                 # Port Extension

# 7. Input Optical Source Parameters
wavelength_center = 1.55e-6             # Central Wavelength
wavelength_span = 0.1e-6                # Wavelength Span
polarization = 'TE'                     # 'TE' or 'TM'

# 7.1 Optical Fibre Parameters (Gaussian Source)
fiber_position_x = 4.5e-6               # Position of the optical source on GC
fiber_angle = -12                       # Angle of the optical source - Incident Angle
waist_radius = 4.5e-6
distance_from_waist = 0.0e-6


# 10. 2D FDTD Simulation Parameters

# 10.1 2D FDTD Span Region
simulation_time = 5e-12

# 10.2 Mesh Settings 
mesh_accuracy = 3

# 10.2 Mesh Settings 
# mesh_dy = wg_width / 2
# mesh_dz = 50e-9
# enable_dx = 0
# enable_dy = 1
# enable_dz = 0

# 10.3 Source/Monitor Properties
mode_fundamental = "TE"                 # Select TE for fundamental TE or TM for fundamental TM
frequency_points = 64

# 11. Figures
my_dpi = 96

# -------------------------- End of Input Section -----------------------------

wavelength_start = wavelength_center - wavelength_span / 2
wavelength_stop = wavelength_center + wavelength_span / 2


if mode_fundamental == "TE":
    mode_source = 90
else:
    mode_source = 0
