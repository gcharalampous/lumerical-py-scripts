#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts sweeps the height of the waveguide and calculates the overlap
integral for the given mode-number.
"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------
# Import necessary modules
import json
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup


# Import user-defined input parameters from the waveguide package
from MODE.butt_coupling.fde_region import add_fde_region
from MODE.butt_coupling.user_inputs.user_sweep_parameters import (
    wg_2_width_start, wg_2_width_stop, wg_2_width_step,
)
from MODE.butt_coupling.user_inputs.user_simulation_parameters import num_modes, my_dpi, m_waveguide1, m_waveguide2


if __name__ == "__main__":
    spec, out, templates = setup("mode.butt_coupling", __file__)
    figures_dir = out["figures"] / "Sweep Width"
    figures_dir.mkdir(parents=True, exist_ok=True)
    lumerical_dir = out["lumerical"] / "sweep_width"
    lumerical_dir.mkdir(parents=True, exist_ok=True)
    dcards_dir = out["lumerical"] / "d_cards"

    # Define the list of d-card and template files
    file_data = ['waveguide_1.ldf','waveguide_2.ldf']
    file_data_directory = [str(dcards_dir / f) for f in file_data]
    file_mode_directory = [str(templates[0]), str(templates[1])]

    # Load polarization data saved by mode_profile_2D.py
    polariz_json = dcards_dir / "polariz_mode_waveguide.json"
    if not polariz_json.exists():
        import warnings
        warnings.warn(
            f"Polarization data not found at {polariz_json}.\n"
            "Run mode_profile/mode_profile_2D.py first to generate it.\n"
            "Exiting."
        )
        import sys
        sys.exit(1)
    with open(polariz_json, "r") as f:
        polariz_mode_waveguide = json.load(f)

    # ----------------------------- Start Sweeping ------------------------------

    # The overlap integral between TE and TM is zero. Therefore,the integral will be

    # is defined from the mode 'm_waveguide1' you defined in simulation parameters
    polarization_wg_1 = polariz_mode_waveguide[0][m_waveguide1-1]
        
    wg_2_width_array = []
    wg_2_width_array = np.arange(wg_2_width_start, wg_2_width_stop, wg_2_width_step) 
    file_name_data_writing = ['str']*len(wg_2_width_array)
    file_name_data_reading = ['str']*len(wg_2_width_array)


    w, h = 2, len(wg_2_width_array)
    overlap_TE = [[0 for x in range(w)] for y in range(h)] 
    overlap_TM = [[0 for x in range(w)] for y in range(h)] 

    overlap_TE_coupling = [0]*len(overlap_TE)
    overlap_TE_power = [0]*len(overlap_TE)
    overlap_TM_coupling = [0]*len(overlap_TM)
    overlap_TM_power = [0]*len(overlap_TM)

    # Initialize empty list for polarization fraction
    polariz_frac = [0]*num_modes

    with lumapi.MODE() as mode:
        if(polarization_wg_1 == 'TE'):
            
            # Open waveguide-2 file
            mode.load(file_mode_directory[1])    
            mode.loaddata(file_data_directory[0])
            
            # Reload the simulation region from user_inputs.user_simualtion_parameters
            add_fde_region(mode)

            
            for wd in range(0,len(wg_2_width_array)):
                mode.switchtolayout()
                mode.redrawoff()
                mode.setnamed("waveguide-constructor","width",wg_2_width_array[wd])
                mode.run()
                mode.mesh()
                mode.findmodes()
                file_name_mode_writing = str(lumerical_dir / ("waveguide_2_mode_sweep_" + str(wd) + ".lms"))
                mode.save(file_name_mode_writing)

                file_name_data_writing[wd] = str(lumerical_dir / ("waveguide_2_data_sweep_" + str(wd) + ".ldf"))
                
                
                file_name_mode_writing = str(lumerical_dir / ("waveguide_2_mode_sweep_" + str(wd) + ".lms"))
                mode.save(file_name_mode_writing)
                
                file_name_data_writing[wd] = str(lumerical_dir / ("waveguide_2_data_sweep_" + str(wd) + ".ldf"))
                mode.savedcard(file_name_data_writing[wd])
                # mode.loaddata(file_name_data_reading[0])

                
                for m in range(1,num_modes+1):
                            polariz_frac[m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
                            
                            if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
                    
                                # Do something when you find the TE Mode
                                print("TE Mode " + str(m) + "\n")
                                mode.copydcard("mode"+str(m),"waveguide_2_mode"+str(m))
                                overlap_TE[wd] = mode.overlap("waveguide_1_mode"+str(m_waveguide1),"waveguide_2_mode"+str(m))
                                mode.cleardcard("waveguide_2_mode"+str(m))
                                print('\n')
                                break;
                    
                            else:
                                # Do something when you find the TM Mode
                                print("TM Mode " + str(m) + "\n")
                                continue;
                                


    # Get the data from the TE lists and prepare for the plot
            for i in range(0,len(overlap_TE)):
                overlap_TE_coupling[i] = overlap_TE[i][0]
                overlap_TE_power[i] = overlap_TE[i][1]
            




            # Plot mode overlap integral versus waveguide height for given mode
            plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

            plt.plot(wg_2_width_array*1e6,overlap_TE_coupling,'-o', label = 'Mode Coupling')
            plt.plot(wg_2_width_array*1e6,overlap_TE_power,'-o', label = 'Power Coupling')
            plt.legend()
            plt.xlabel("width (um)")
            plt.ylabel("TE Mode Overlap")
            plt.ylim([0,1])
            plt.title("Waveguide-2 width Sweep") 

            plt.legend()
            plt.xlabel("width (um)")
            plt.ylabel("TE overlap")

            # Save the figure files as .png     
            file_name_plot = str(figures_dir / "overlap_waveguide2_width_sweep.png")
            plt.tight_layout()
            plt.savefig(file_name_plot, dpi=my_dpi, format="png")



        
        
        
        
        
        
    # If you set the source polarization angle, you will get the TM mode

        if(polarization_wg_1 == 'TM'):
        

            # Open waveguide-2 file
            mode.load(file_mode_directory[1])    
            mode.loaddata(file_data_directory[0])
            
            # Reload the simulation region from user_inputs.user_simualtion_parameters
            add_fde_region(mode)
                    
            for wd in range(0,len(wg_2_width_array)):
                mode.switchtolayout()
                mode.redrawoff()
                mode.setnamed("waveguide-constructor","width",wg_2_width_array[wd])
                mode.run()
                mode.mesh()
                mode.findmodes()
                file_name_mode_writing = str(lumerical_dir / ("waveguide_2_mode_sweep_" + str(wd) + ".lms"))
                mode.save(file_name_mode_writing)

                file_name_data_writing[wd] = str(lumerical_dir / ("waveguide_2_data_sweep_" + str(wd) + ".ldf"))
                
                
                file_name_mode_writing = str(lumerical_dir / ("waveguide_2_mode_sweep_" + str(wd) + ".lms"))
                mode.save(file_name_mode_writing)
                
                file_name_data_writing[wd] = str(lumerical_dir / ("waveguide_2_data_sweep_" + str(wd) + ".ldf"))
                mode.savedcard(file_name_data_writing[wd])
                # mode.loaddata(file_name_data_reading[0])

                
                for m in range(1,num_modes+1):
                            polariz_frac[m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
                            
                            if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
                    
                                # Do something when you find the TE Mode
                                print("TE Mode " + str(m) + "\n")
                                continue;
                                break;
                    
                            else:
                                # Do something when you find the TM Mode
                                print("TM Mode " + str(m) + "\n")
                                mode.copydcard("mode"+str(m),"waveguide_2_mode"+str(m))
                                overlap_TM[wd] = mode.overlap("waveguide_1_mode"+str(m_waveguide1),"waveguide_2_mode"+str(m))
                                mode.cleardcard("waveguide_2_mode"+str(m))
                                print('\n')
                                break;                                    
                                

    # Get the data from the TM lists and prepare for the plot


            for i in range(0,len(overlap_TM)):
                overlap_TM_coupling[i] = overlap_TM[i][0]
                overlap_TM_power[i] = overlap_TM[i][1]
                        




            # Plot mode overlap integral versus waveguide height for given mode
            plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

            plt.plot(wg_2_width_array*1e6,overlap_TM_coupling,'-o', label = 'Mode Coupling')
            plt.plot(wg_2_width_array*1e6,overlap_TM_power,'-o', label = 'Power Coupling')
            plt.legend()
            plt.xlabel("width (um)")
            plt.ylabel("TM Mode Overlap")
            plt.ylim([0,1])
            plt.title("Waveguide-2 width Sweep") 

            plt.legend()
            plt.xlabel("width (um)")
            plt.ylabel("TM overlap")

            # Save the figure files as .png     
            file_name_plot = str(figures_dir / "overlap_waveguide2_width_sweep.png")
            plt.tight_layout()
            plt.savefig(file_name_plot, dpi=my_dpi, format="png")

