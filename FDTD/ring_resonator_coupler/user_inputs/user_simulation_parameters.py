#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are required.

In this file, the user is must enter the parameters required to setup the
simulation file. 

"""

# 1. Set the index file name to load one of the lumerical files
# ["straight_ring_coupling_section.fsp","coocentric_ring_coupling_section.fsp","rectangular_ring_coupling_section"]

file_index = 0


# 2. FDTD Simulation Parameters

# 2.1 FDTD Simulation Region
simulation_span_z = 3e-6
port_extension = 5e-6
monitor_theta = 0

# 2.2 Simulation Accuracy
simulation_time = 5000e-15
mesh_accuracy = 3

# 2.3 Simulation Mesh
enable_dx = True
enable_dy = True
mesh_dx = 100e-9
mesh_dy = 100e-9

# 3. Mode Source
mode_polarization = 'fundamental TE mode'    # or fundamental TM mode
wavelength_start = 1.55e-6
wavelength_stop = 1.55e-6

# 4. Monitor Properties
frequency_points = 64


# 5. Ring Coupler Parameters
ring_radius = 10e-6
wg_ring_width = 0.48e-6
wg_bus_width = wg_ring_width
wg_thickness = 0.22e-6
slab_thickness = 0.11e-6
gap = 0.30e-6
bus_angle = 60