#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
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
clad_index = 3.0981


# Waveguide Core
is_wg_index = True                              # If true ignore wg_material
wg_material = "Si3N4 (Silicon Nitride) - Phillip"
wg_index = 3.33


# Box
is_box_index = True                             # If true ignore box_material
box_material = "Si (Silicon) - Palik"
box_index = 3.0981



# Substrate
is_sub_index = True                            # If true ignore sub_material
sub_material = "SiO2 (Glass) - Palik"
sub_index = 3.0981




# -------------------------- End of Input Section -----------------------------


if(is_wg_index):
    wg_material = "<Object defined dielectric>"
else:
    wg_material = wg_material
    
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
