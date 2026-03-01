#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
No user-inputs are required.

The scripts calculates the overlap integral for the mode order you defined in
the user_simulation_parameters.py.

# 4.1 Waveguide_1.lms
m_waveguide1=2

# 4.2 Waveguide_2.lms
m_waveguide2=1


"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------
# Import necessary modules
import lumapi
from project_layout import setup
from MODE.butt_coupling.user_inputs.user_simulation_parameters import m_waveguide1, m_waveguide2, my_dpi
from MODE.butt_coupling.user_inputs.user_sweep_parameters import (
    misalign_y_start, misalign_y_stop, misalign_y_step,
    misalign_z_start, misalign_z_stop, misalign_z_step,
)
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    spec, out, templates = setup("mode.butt_coupling", __file__)
    dcards_dir = out["lumerical"] / "d_cards"
    figures_dir = out["figures"] / "Sweep Misalignment"
    figures_dir.mkdir(parents=True, exist_ok=True)

    # Define the list of waveguide files to be loaded into Lumerical MODE
    file_waveguide = ['waveguide_1.ldf', 'waveguide_2.ldf']

    # Initialize a list to store the names of the waveguide modes in Lumerical MODE
    file_name_mode = [str]*len(file_waveguide)


    # ------------------------- Start Sweeping Misalign---------------------------

    # Initialize the misalignment arrays
    misalign_y_array = np.arange(misalign_y_start,misalign_y_stop,misalign_y_step)
    misalign_z_array = np.arange(misalign_z_start,misalign_z_stop,misalign_z_step)


    w, h = 2, len(misalign_y_array)
    overlap_y = [[0 for x in range(w)] for y in range(h)] 
    w, h = 2, len(misalign_z_array)
    overlap_z = [[0 for x in range(w)] for y in range(h)] 

    # Initialize LumAPI and turn off redraw for faster simulations
    with lumapi.MODE() as mode:
        
        # Switch to layout mode
        mode.switchtolayout()
        
        # Load each waveguide file into Lumerical MODE
        for i in range(0,len(file_waveguide)):
            file_name_mode[i] = str(dcards_dir / file_waveguide[i])
            mode.loaddata(file_name_mode[i])

        
        
        for i in range(len(misalign_y_array)):
            overlap_y[i] = mode.overlap("waveguide_1_mode" + str(m_waveguide1), 
                                "waveguide_2_mode" + str(m_waveguide2)
                                ,0,misalign_y_array[i],0)

        for i in range(len(misalign_z_array)):
            overlap_z[i] = mode.overlap("waveguide_1_mode" + str(m_waveguide1), 
                                "waveguide_2_mode" + str(m_waveguide2)
                                ,0,0,misalign_z_array[i])


    # ---------------------------------------------------------------------------


    # ----------------------- Prepare the data for plots --------------------------
    overlap_y_coupling = [0]*len(overlap_y)
    overlap_y_power = [0]*len(overlap_y)

    overlap_z_coupling = [0]*len(overlap_z)
    overlap_z_power = [0]*len(overlap_z)


    for i in range(0,len(overlap_y)):
        overlap_y_coupling[i] = overlap_y[i][0]
        overlap_y_power[i] = overlap_y[i][1]
                
    for i in range(0,len(overlap_z)):
        overlap_z_coupling[i] = overlap_z[i][0]
        overlap_z_power[i] = overlap_z[i][1]
                        
    # ---------------------------------------------------------------------------


    # ---------------------------  Plot the Results  ----------------------------
    # Plot overlap integral versus waveguide y-axis missalignement for given mode
    plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

    plt.plot(misalign_y_array*1e6,overlap_y_coupling,'-o', label = 'Mode Coupling')
    plt.plot(misalign_y_array*1e6,overlap_y_power,'-o', label = 'Power Coupling')
    plt.legend()
    plt.xlabel("Horizontal y-axis (um)")
    plt.ylabel("Mode Overlap")
    plt.ylim([0,1])
    plt.title("Horizontal Misalignment") 
    plt.legend()

    # Save the figure files as .png     
    file_name_plot = str(figures_dir / "overlap_misalignment_horizontal.png")
    plt.tight_layout()
    plt.savefig(file_name_plot, dpi=my_dpi, format="png")


    # Plot overlap integral versus waveguide z-axis missalignement for given mode
    plt.figure(figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)

    plt.plot(misalign_z_array*1e6,overlap_z_coupling,'-o', label = 'Mode Coupling')
    plt.plot(misalign_z_array*1e6,overlap_z_power,'-o', label = 'Power Coupling')
    plt.legend()
    plt.xlabel("Vertical z-axis (um)")
    plt.ylabel("Mode Overlap")
    plt.ylim([0,1])
    plt.title("Vertical Misalignment") 
    plt.legend()


    # Save the figure files as .png     
    file_name_plot = str(figures_dir / "overlap_misalignment_vertical.png")
    plt.tight_layout()
    plt.savefig(file_name_plot, dpi=my_dpi, format="png")



