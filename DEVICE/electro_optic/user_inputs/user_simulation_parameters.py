#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Author: Georgios Gcharalampous (gcharalampous)
# Version: 1.0
# Description: User inputs required to set up the simulation file.
#----------------------------------------------------------------------------

"""
User inputs are required.

This script prompts the user to enter parameters needed to set up the simulation file.
"""

# Length units are in meters!

# 1. Simulation Region Parameters
simulation_span_x = 10.5e-6   # X-axis span of simulation
simulation_min_z = -3.0e-6    # Minimum Z-coordinate of simulation region
simulation_max_z = 3.5e-6     # Maximum Z-coordinate of simulation region


# 2. Cladding Dimensions. Note: waveguide y min = 0.
clad_min_y = 0e-6             # Minimum Y-coordinate of cladding
clad_max_y = 1.0e-6           # Maximum Y-coordinate of cladding


# 3. Waveguide Dimensions
wg_width = 0.5e-6             # Width of waveguide
wg_thickness = 0.3e-6         # Thickness of waveguide
wg_angle = 80                 # Angle of waveguide (degrees) - Not yet implemented


# 3.1 Set slab thickness > 0 to enable a slab waveguide
slab_thickness = 0.05e-6      # Thickness of slab waveguide (set > 0 to enable)


# 3.2 Metal Layer
metal_left_width = 2.0e-6     # Width of left metal layer
metal_center_width = metal_left_width   # Width of center metal layer
metal_right_width = metal_left_width    # Width of right metal layer
metal_thickness = 1.0e-6      # Thickness of metal layer
metal_pitch = 3e-6            # Pitch of metal layer


# 3.2.1 GSG Pads
GSG_pads_enable = True        # True for GSG Pads, False for GS Pads


# 3.4 Voltage of Signal and Ground
v_signal = 3                  # Voltage of signal


# 4. Box Layer Thickness
box_thickness = abs(simulation_min_z)   # Thickness of box layer


# 5. Substrate Layer Thickness
sub_thickness = 10e-6         # Thickness of substrate layer


# 6. Charge Parameters.
# 6.1 Mesh Parameters
min_edge_length = 4e-9        # Minimum edge length for mesh
max_edge_length = 600e-9      # Maximum edge length for mesh


# 6.2 3D Expansion
norm_length = 1e-6            # Normalization length for 3D expansion


# 6.3 Doping
# 6.3.1 Background Doping
pepi_p_doping_enable = False   # Enable background doping


# 6.3.2 Waveguide Doping (thickness starts from top)
waveguide_pp_doping_enable = False    # Enable waveguide doping
waveguide_pp_thickness = 20e-9      # Thickness of waveguide doping

waveguide_nn_doping_enable = False    # Enable waveguide doping
waveguide_nn_thickness = 20e-9      # Thickness of waveguide doping


# 7 FEEM Parameters
wavelength = 1.55e-6          # Wavelength
num_modes = 6                 # Number of modes


# 7.1 Mesh (waveguide)
mesh_enable = True            # Enable mesh
max_edge_length_mesh_override = 500e-9   # Maximum edge length for mesh override



# 8. Figures
my_dpi = 96                   # DPI for figures
