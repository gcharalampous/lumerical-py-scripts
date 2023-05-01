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
import numpy as np
import lumapi
import matplotlib.pyplot as plt
import os 


# Import user-defined input parameters from the waveguide package
from MODE.butt_coupling.user_inputs.user_sweep_parameters import *    
from MODE.butt_coupling.mode_profile.mode_profile_2D import *

# ------------------------- Directories for Results ---------------------------

# specify the directory path
path_to_write = ["MODE\\Results\\butt_coupling\\lumerical_files\\sweep_width",
"MODE\\Results\\butt_coupling\\Figures\\sweep"]
directory_to_write = ['']*len(path_to_write)


# get the current file path
current_path = os.path.abspath(__file__)

# get the directory of the current file
current_dir = os.path.dirname(current_path)

# find the project root directory by traversing up the directory 
# tree until a specific file is found
while not os.path.isfile(os.path.join(current_dir, ".gitignore")):
    # move up to the parent directory
    current_dir = os.path.dirname(current_dir)

for i in range(0,len(path_to_write)):
    directory_to_write[i] = os.path.join(current_dir, path_to_write[i])

    # create the directory if it doesn't exist already
    if not os.path.exists(directory_to_write[i]):
        os.makedirs(directory_to_write[i])
        print("Directory:" + directory_to_write[i] + "\n created successfully!")
    else:
        print("Directory:" + directory_to_write[i] + "\n already exists!")



# ---------------------------------------------------------------------------



# ------------------------- Directories for Reading ---------------------------

path_to_read = ["MODE\\butt_coupling\\user_inputs\\lumerical_files",
                "MODE\\Results\\butt_coupling\\lumerical_files\\d_cards"]

file_data = ['waveguide_1.ldf','waveguide_2.ldf']
file_mode = ["waveguide_1.lms", "waveguide_2.lms"]


directory_to_read = [str]*len(file_mode)
file_data_directory = [str]*len(file_data)
file_mode_directory = [str]*len(file_mode)


# Read the two template files
for i in range(0,len(file_mode)):
    directory_to_read[i] = os.path.join(current_dir, path_to_read[i])

    
    
    
    
for i in range(0,len(file_mode)):    
    file_mode_directory[i] = os.path.join(directory_to_read[0], file_mode[i])
    file_data_directory[i] = os.path.join(directory_to_read[1], file_data[i])
    
    



# ---------------------------------------------------------------------------


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



with lumapi.MODE() as mode:
    if(polarization_wg_1 == 'TE'):
        
        # Open waveguide-2 file
        mode.load(file_mode_directory[1])    
        mode.loaddata(file_data_directory[0])
        
        for wd in range(0,len(wg_2_width_array)):
            mode.switchtolayout()
            mode.redrawoff()
            mode.setnamed("waveguide-constructor","width",wg_2_width_array[wd])
            mode.run()
            mode.mesh()
            mode.findmodes()
            file_name_mode_writing = os.path.join(directory_to_write[0], 
                                                    "waveguide_2_mode_sweep_" +str(wd) + ".lms")
            mode.save(file_name_mode_writing)

            file_name_data_writing[wd] = os.path.join(directory_to_write[0], 
                                                    "waveguide_2_data_sweep_" +str(wd) + ".ldf")
            
            
            file_name_mode_writing = os.path.join(directory_to_write[0], 
                                                "waveguide_2_mode_sweep_" +str(wd) + ".lms")
            mode.save(file_name_mode_writing)
            
            file_name_data_writing[wd] = os.path.join(directory_to_write[0], 
                                                "waveguide_2_data_sweep_" +str(wd) + ".ldf")
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
        plt.ylabel("TE Mode Overlap (%)")
        plt.ylim([0,1])
        plt.title("Waveguide-2 width Sweep") 

        plt.legend()
        plt.xlabel("height (um)")
        plt.ylabel("TE overlap (%)")

        # Save the figure files as .png     
        file_name_plot = os.path.join(directory_to_write[1], "overlap_waveguide2_width_sweep" + ".png")
        plt.tight_layout()
        plt.savefig(file_name_plot, dpi=my_dpi, format="png")



    
    
    
    
    
    
# If you set the source polarization angle, you will get the TM mode

    if(polarization_wg_1 == 'TM'):
    

        # Open waveguide-2 file
        mode.load(file_mode_directory[1])    
        mode.loaddata(file_data_directory[0])
        
        for wd in range(0,len(wg_2_width_array)):
            mode.switchtolayout()
            mode.redrawoff()
            mode.setnamed("waveguide-constructor","width",wg_2_width_array[wd])
            mode.run()
            mode.mesh()
            mode.findmodes()
            file_name_mode_writing = os.path.join(directory_to_write[0], 
                                                    "waveguide_2_mode_sweep_" +str(wd) + ".lms")
            mode.save(file_name_mode_writing)

            file_name_data_writing[wd] = os.path.join(directory_to_write[0], 
                                                    "waveguide_2_data_sweep_" +str(wd) + ".ldf")
            
            
            file_name_mode_writing = os.path.join(directory_to_write[0], 
                                                "waveguide_2_mode_sweep_" +str(wd) + ".lms")
            mode.save(file_name_mode_writing)
            
            file_name_data_writing[wd] = os.path.join(directory_to_write[0], 
                                                "waveguide_2_data_sweep_" +str(wd) + ".ldf")
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
        plt.ylabel("TM Mode Overlap (%)")
        plt.ylim([0,1])
        plt.title("Waveguide-2 width Sweep") 

        plt.legend()
        plt.xlabel("width (um)")
        plt.ylabel("TM overlap (%)")

        # Save the figure files as .png     
        file_name_plot = os.path.join(directory_to_write[1], "overlap_waveguide2_width_sweep" + ".png")
        plt.tight_layout()
        plt.savefig(file_name_plot, dpi=my_dpi, format="png")
        
    

