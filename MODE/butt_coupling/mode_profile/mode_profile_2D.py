#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the mode profile for the number of modes (num_modes) 
specified in 'user_simulation_parameters.py'.

The scripts calculates the effective index of each mode and plots the profile,
it also quantifies if the mode is TE or TM based on the polarization fraction.

The mode profiles are save to a d-cards which are loaded later from 
overlap_mode.overlap_mode_integral_2D.py

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import json
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from project_layout import setup
from MODE.butt_coupling.fde_region import add_fde_region
from MODE.butt_coupling.user_inputs.user_simulation_parameters import num_modes, my_dpi, m_waveguide1, m_waveguide2


# Module-level list so other scripts can import it
polariz_mode_waveguide = []


if __name__ == "__main__":
    spec, out, templates = setup("mode.butt_coupling", __file__)
    figures_dir = out["figures"] / "Mode Profile"
    figures_dir.mkdir(parents=True, exist_ok=True)
    lumerical_dir = out["lumerical"] / "mode_profile"
    lumerical_dir.mkdir(parents=True, exist_ok=True)
    dcards_dir = out["lumerical"] / "d_cards"
    dcards_dir.mkdir(parents=True, exist_ok=True)


    for i in range(0,len(templates)):
        with lumapi.MODE(str(templates[i])) as mode:
            mode.switchtolayout()

            # Reload the simulation region from user_inputs.user_simualtion_parameters
            add_fde_region(mode)

            # Set and Get the data
            mode.setnamed("FDE","number of trial modes",num_modes)
            wg_width = mode.getnamed("waveguide-constructor::waveguide_core","y span")
            wg_thickness = mode.getnamed("waveguide-constructor::waveguide_core","z span")
            slab_thickness = mode.getnamed("waveguide-constructor::rib","z span")
            simulation_span_y = mode.getnamed("::model","FDE_span_y")
            
            
            mode.mesh()
            mode.findmodes()
           
            
            # Save the file
            file_name_mode = str(lumerical_dir / ("waveguide_mode_profile_" + str(i+1) + ".lms"))
            mode.save(file_name_mode)
            mode.save()
            
            # Initialize empty lists to store mode properties
            neff = []           # effective index
            polariz_frac = []   # polarization fraction
            # polarization mode (TE or TM)
            polariz_mode = ['str']*num_modes
        

            for m in range(1,num_modes+1):
                
                # Copy d-card mode to the global deck
                mode.copydcard("mode" + str(m),"waveguide_" + str(i+1) + "_mode" + str(m))
                
                # Extract effective index and polarization fraction
                neff.append(mode.getdata("FDE::data::mode"+str(m),"neff"))
                polariz_frac.append(mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
                
                # Determine if mode is TE-like or TM-like based on polarization fraction
                if ( polariz_frac[m-1] > 0.5 ):
                    polariz_mode[m-1] = "TE"
                else:
                    polariz_mode[m-1] = "TM"
         
         
                # Extract electric and magnetic fields and plot the electric field
                plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
                y  = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"))
                z = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"z"))
                E1 = np.squeeze(mode.getelectric("FDE::data::mode"+str(m)))
                H1 = np.squeeze(mode.getmagnetic("FDE::data::mode"+str(m)))
                plt.pcolormesh(y*1e6,z*1e6,np.transpose(E1),shading = 'gouraud',cmap = 'jet')


                plt.xlabel("y (\u00B5m)")
                plt.ylabel("z (\u00B5m)")
                plt.title("Mode-"+str(m) + "(E-field): " + polariz_mode[m-1] + ", neff=" + str(np.round(neff[m-1],4)))
                print('Waveguide_' + str(i+1) + '.lms, Mode: ' + str(m))
                
                
                #add the waveguide
                plt.gca().add_patch(Rectangle((-0.5*wg_width*1e6, -0.5*wg_thickness*1e6),
                                    wg_width*1e6,wg_thickness*1e6,
                                    ec='white',
                                    fc='none',
                                    lw=0.5))
                
                if(slab_thickness > 0):
                    #add the slab
                    plt.gca().add_patch(Rectangle((-0.5*simulation_span_y*1e6, -0.5*wg_thickness*1e6),
                                        simulation_span_y*1e6,slab_thickness*1e6,
                                        ec='white',
                                        fc='none',
                                        lw=0.5))

                # Save the figure files as .png
                file_name_plot = str(figures_dir / ("waveguide_" + str(i+1) + "_mode_profile_" + str(m) + ".png"))
                plt.tight_layout()
                plt.savefig(file_name_plot, dpi=my_dpi, format="png")
                plt.show()
                x = ["a","a"]
            polariz_mode_waveguide.append(polariz_mode)
            print(polariz_mode_waveguide)
            file_name_ldf = str(dcards_dir / ("waveguide_" + str(i+1) + ".ldf"))
            mode.savedcard(file_name_ldf)

    # Save polarization data to JSON so downstream scripts can load it
    polariz_json = dcards_dir / "polariz_mode_waveguide.json"
    with open(polariz_json, "w") as f:
        json.dump(polariz_mode_waveguide, f)
