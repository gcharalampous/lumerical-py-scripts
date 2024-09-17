#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------

import numpy as np

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

# Oxide
oxide_material = "SiO2 (Glass) - Sze"


# Waveguide Core
wg_material = "Si (Silicon)"
wg_mole_fract = 0.2                                 # If applicable, otherwise will be neglected

# Contacts
contact_material = "Al (Aluminium) - CRC"








## ------ Doping

# PEPI [doping in cm^-3]
pepi_p_doping = 1e15

Nnn=2.2e20                                            # N++ 
Ppp=9e19                                              # P++

# -------------------------- End of Input Section -----------------------------

material_list = [oxide_material, wg_material, contact_material]

# Remove Duplicate strings
unique_material_list = []
for item in material_list:
    if item not in unique_material_list:
        unique_material_list.append(item)
