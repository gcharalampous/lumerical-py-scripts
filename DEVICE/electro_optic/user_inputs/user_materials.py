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
### Electrical Materials
# Oxide
oxide_material_e = "SiO2 (Glass) - Sze"


# Waveguide Core
wg_material_e = "AlGaAs (Aluminium Gallium Arsenide)"
wg_mole_fract = 0.2                                 # If applicable, otherwise will be neglected

# Contacts
contact_material_e = "Au (Gold) - CRC"

# Background Material
background_material_e = "Air"


### 

### Optical Materials
# Oxide
oxide_material_o = "SiO2 (Glass) - Palik"


# Waveguide Core
wg_material_o = 'Dielectric'
wg_index = 3.28               #   'ordinary'


# Contacts
contact_material_o = "Au (Gold) - CRC"

# Background Material
background_material_o = "etch"


# Background p Doping
pepi_p_doping = 1e15

# Waveguide pp Doping
waveguide_pp_doping = 1e18



# -------------------------- End of Input Section -----------------------------

material_list_e = [oxide_material_e, wg_material_e, 
                 contact_material_e, background_material_e]

# Remove Duplicate strings
unique_material_list_e = []
for item in material_list_e:
    if item not in unique_material_list_e:
        unique_material_list_e.append(item)


material_list_o = [oxide_material_o, wg_material_o, 
                 contact_material_o, background_material_o]

        
# Remove Duplicate strings
unique_material_list_o = []
for item in material_list_o:
    if item not in unique_material_list_o:
        unique_material_list_o.append(item)      
      