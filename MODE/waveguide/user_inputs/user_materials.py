#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------

import numpy as np
from MODE.waveguide.user_inputs.user_simulation_parameters import wavelength

"""
User-inputs are required.

Input the appropriate material for each structure as appears below 


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

                                                                               
Select between material model or material index. By selecting the variable  
'is_clad_index = True' the material model will be ingonred and instead the 
cladding_index = 1 cladding index 1 will be set.


Please make sure that you type the material model exactly as it is in the material 
database.

"""

# Cladding
is_clad_index = True                            # If true ignore clad_material
clad_material = "SiO2 (Glass) - Palik"
clad_index = 1.444


# Waveguide Core
is_wg_index = True
wg_material = "Si (Silicon) - Palik"
wg_index = 3.4777


# Waveguide Slab
is_slab_index = True                              # If true ignore wg_material
slab_material = "Si (Silicon) - Palik"
slab_index = 3.4777


#  Metal Layers (You can use a metal stuck using arrays)
is_metal_index = [False,False]                    # If true ignore metal_material
metal_material = ["Ti (Titanium) - CRC","Au (Gold) - Johnson and Christy"]
metal_index = [3.6845, 0.52406] # Not sure how imaginary numbers can be used as indices


# PCM Material Index
pcm_index = 2.7631


# Box
is_box_index = True
box_material = "SiO2 (Glass) - Palik"
box_index = 1.444


# Substrate
is_sub_index = False                            # If true ignore sub_material
sub_material = "Si (Silicon) - Palik"
sub_index = 3.4777


## ------ Doping
N=2.5e17                                          # N++ 
P=6.5e17                                            # P++

# -------------------------- End of Input Section -----------------------------


if(is_wg_index):
    wg_material = "<Object defined dielectric>"
else:
    wg_material = wg_material
    
if(is_slab_index):
    slab_material = "<Object defined dielectric>"
else:
    slab_material = slab_material
    
if(is_clad_index):
    clad_material = "<Object defined dielectric>"
else:
    clad_material = clad_material
   
if(is_box_index):
    box_material = "<Object defined dielectric>"
else:
    box_material = box_material
   
if(is_sub_index):
    sub_material = "<Object defined dielectric>"
else:
    sub_material = sub_material

for i in range(0,len(metal_material)):
    if(is_metal_index[i]):
        metal_material[i] = "<Object defined dielectric>"
    else:
        metal_material[i] = metal_material[i]




# Calculates the attenulation coefficients [Silicon only]
alphaN_m = 3.52e-6*wavelength**2*N*100
alphaP_m = 2.4e-6*wavelength**2*P*100
# Calculates the extnction coefficients
k_P = wavelength * alphaP_m /4/np.pi;
k_N = wavelength * alphaN_m /4/np.pi;
