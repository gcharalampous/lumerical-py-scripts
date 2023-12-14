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

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from config import *


from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  


# ------------------------- No inputs are required ---------------------------



def modeProfiles():

    # Initialize empty lists to store mode properties
    neff = []           # effective index
    ng = []             # group index
    polariz_frac = []   # polarization fraction
    polariz_mode = []   # polarization mode (TE or TM)

    # Loop over each mode and extract its properties
    for m in range(1,num_modes+1):
        # Extract effective index and polarization fraction
        neff.append(mode.getdata("FDE::data::mode"+str(m),"neff"))
        ng.append(mode.getdata("FDE::data::mode"+str(m),"ng"))
        polariz_frac.append(mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
        
        # Determine if mode is TE-like or TM-like based on polarization fraction
        if ( polariz_frac[m-1] > 0.5 ):
            polariz_mode.append("TE")
        else:
            polariz_mode.append("TM")

        # Extract electric and magnetic fields and plot the electric field
        plt.figure(m-1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        x  = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"x")); 
        y= np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"));
        E1 = np.squeeze(mode.getelectric("FDE::data::mode"+str(m)))
        H1 = np.squeeze(mode.getmagnetic("FDE::data::mode"+str(m)))
        plt.pcolormesh(x*1e6,y*1e6,np.transpose(E1),shading = 'gouraud',cmap = 'jet')


        plt.xlabel("x (\u00B5m)")
        plt.ylabel("y (\u00B5m)")
        plt.title("Mode-"+str(m) + "(E-field): " + polariz_mode[m-1] + ", neff=" + str(np.round(neff[m-1],4)))

        #add the waveguide
        plt.gca().add_patch(Rectangle((-0.5*wg_width*1e6, 0*1e6),
                            wg_width*1e6,(wg_thickness)*1e6,
                            ec='white',
                            fc='none',
                            lw=0.5))
        
        if(slab_thickness > 0):
            #add the slab
            plt.gca().add_patch(Rectangle((-0.5*simulation_span_x*1e6, 0),
                                simulation_span_x*1e6,slab_thickness*1e6,
                                ec='white',
                                fc='none',
                                lw=0.5))

        # Save the figure files as .png
        plt.tight_layout()
        file_name_plot = os.path.join(MODE_WAVEGUIDE_DIRECTORY_WRITE[1], "mode_profile_"+str(m)+".png")
        plt.savefig(file_name_plot)
    return neff, ng, polariz_frac, polariz_mode




if(__name__=="__main__"):
    with lumapi.MODE() as mode:
        
        # Disable Rendering
        mode.redrawoff()

        # Draw the waveguide structure using a custom function
        waveguide_draw(mode)

        # Add a finite-difference eigenmode (FDE) region to the simulation environment
        add_fde_region(mode)

        # Run the simulation, create a mesh, and compute the modes, then save
        mode.run()
        mode.findmodes()
        mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_modes.lms")
        
        # Turn redraw back on and close LumAPI connection
        mode.redrawon()  

        # Mode Profiles
        # Initialize empty lists to store mode properties
        neff = []           # effective index
        ng = []             # group index
        polariz_frac = []   # polarization fraction
        polariz_mode = []   # polarization mode (TE or TM)

        neff, ng, polariz_frac, polariz_mode = modeProfiles()
