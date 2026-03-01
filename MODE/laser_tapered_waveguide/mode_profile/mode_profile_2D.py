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
# Imports from user files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import shapely.geometry as sg
import shapely.ops as so
import matplotlib.pyplot as plt
from pathlib import Path
from project_layout import setup
from MODE.laser_tapered_waveguide.user_inputs.user_sweep_parameters import num_modes



# ------------------------- No inputs are required ---------------------------


def modeProfiles(mode, figures_dir=None):

    mode.findmodes()

    Ef = mode.getresult("FDE::data::mode"+str(1),"E")
    wavelength = np.squeeze(Ef['lambda'])

    neff = []
    polariz_frac = []
    polariz_mode = []
    sym_mode = [0]*(num_modes)



    for m in range(1,num_modes+1):
        neff.append(mode.getdata("FDE::data::mode"+str(m),"neff"))
        polariz_frac.append(mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
        

        if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
            polariz_mode.append("TE")
            E1 = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Ex"))
            H1 = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Hx"))
            
        else:
            polariz_mode.append("TM")
            E1 = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Ey"))
            H1 = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"Hy"))
            
        sym_mode[m-1] = np.real(E1.min())
        x  = np.squeeze(mode.getdata("FDE::data::mode"+str(m),"x")); 
        y= np.squeeze(mode.getdata("FDE::data::mode"+str(m),"y"));


        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig, ax = plt.subplots(figsize=(512*px, 256*px))
            
        im = ax.pcolormesh(x*1e6, y*1e6, np.transpose(np.real(E1)), shading='gouraud', cmap='jet')
        cbar = fig.colorbar(im)


        ax.set_xlabel("x (\u00B5m)")
        ax.set_ylabel("y (\u00B5m)")
        ax.set_title("Mode-"+str(m) + "(E-field): " + polariz_mode[m-1] + ", neff=" + str(neff[m-1]))
        

        # Add the waveguide
        wg_thickness = mode.getnamed("waveguide-constructor","thickness")
        slab_thickness = mode.getnamed("waveguide-constructor","slab_thickness")
        wg_xmin = mode.getnamed("waveguide-constructor::waveguide_core","x min")
        wg_xmax = mode.getnamed("waveguide-constructor::waveguide_core","x max")

        r1 = sg.box(wg_xmin*1e6,-wg_thickness*1e6,wg_xmax*1e6,0)

    
        
        if(slab_thickness > 0):
        
            #Add the slab
            slab_xmin = mode.getnamed("waveguide-constructor::slab","x min")
            slab_xmax = mode.getnamed("waveguide-constructor::slab","x max")
            r2 = sg.box(slab_xmin*1e6,-wg_thickness*1e6,slab_xmax*1e6,(-wg_thickness+slab_thickness)*1e6)

            # Cascaded union can work on a list of shapes
            merged_shape = so.unary_union([r1,r2])

            #exterior coordinates split into two arrays, xs and ys
            # which is how matplotlib will need for plotting
            xs, ys = merged_shape.exterior.xy
            plt.fill(xs, ys, alpha=0.5, fc='none', ec='w')
        else:
            xs, ys = r1.exterior.xy
            plt.fill(xs, ys, alpha=0.5, fc='none', ec='w')


        if figures_dir is not None:
            file_name_plot = str(Path(figures_dir) / ("mode_profile_"+str(m)+".png"))
            plt.savefig(file_name_plot)



        # Add the mesa
        mesa_width = mode.getnamed("mesa-constructor","mesa_width")
        gap = mode.getnamed("::model","mesa_gap")

        n_contact_thickness = mode.getnamed("mesa-constructor","n_contact_thickness")
        previous_= gap + n_contact_thickness
        r3 = sg.box(-0.5*mesa_width*1e6,gap,0.5*mesa_width*1e6,previous_*1e6)
        

        n_cladding_thickness = mode.getnamed("mesa-constructor","n_cladding_thickness")
        r4 = sg.box(-0.5*mesa_width*1e6,previous_,0.5*mesa_width*1e6,(previous_+n_cladding_thickness)*1e6)
        previous_ = previous_ + n_cladding_thickness

        core_thickness = mode.getnamed("mesa-constructor","core_thickness")
        r5 = sg.box(-0.5*mesa_width*1e6,previous_,0.5*mesa_width*1e6,(previous_+core_thickness)*1e6)
        previous_ = previous_ + core_thickness

        p_cladding_thickness = mode.getnamed("mesa-constructor","p_cladding_thickness")
        r6 = sg.box(-0.5*mesa_width*1e6,previous_,0.5*mesa_width*1e6,(previous_+p_cladding_thickness)*1e6)
        previous_ = previous_ + p_cladding_thickness

        p_contact_thickness = mode.getnamed("mesa-constructor","p_contact_thickness")
        r7 = sg.box(-0.5*mesa_width*1e6,previous_,0.5*mesa_width*1e6,(previous_+p_contact_thickness)*1e6)
        previous_ = previous_ + p_contact_thickness        

        
        
        for r in [r3, r4, r5, r6, r7]:
            xs, ys = r.exterior.xy
            plt.fill(xs, ys, alpha=0.5, fc='none', ec='w')
            ax.set_xlim([x.min()*1e6, x.max()*1e6])
            ax.set_ylim([y.min()*1e6, y.max()*1e6])




        

   


    return neff, polariz_frac, polariz_mode, sym_mode







if(__name__=="__main__"):
    spec, out, templates = setup("mode.laser_tapered_waveguide", __file__)

    with lumapi.MODE(str(templates[0])) as mode:

    # Run the simulation, create a mesh, and compute the modes, then save
    

        # Mode Profiles
        # Initialize empty lists to store mode properties
        neff = []           # effective index
        polariz_frac = []   # polarization fraction
        polariz_mode = []   # polarization mode (TE or TM)
        sym_mode = []       # symmetry of the mode

        # Switch to layout mode
        mode.switchtolayout()
        
        # Generate the mesh for the simulation
        mode.mesh()
        
        # Run the simulation
        mode.run()
        
        # Find the modes in the simulation
        # mode.findmodes()
        
        
        # Retrieve mode profiles and assign to respective variables
        neff, polariz_frac, polariz_mode, sym_mode = modeProfiles(mode, figures_dir=out["figure_groups"]["Mode Profile"])

    