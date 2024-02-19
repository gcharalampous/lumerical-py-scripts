#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the index mesh for the given waveguide specified in 
'user_simulation_parameters.py'.


"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi, os
import matplotlib.pyplot as plt
from config import *
import shapely.geometry as sg
import shapely.ops as so

from MODE.waveguide.waveguide_render import *
from MODE.waveguide.fde_region import add_fde_region  


# ------------------------- No inputs are required ---------------------------


def getIndex(mode):

    # Get the data from the FDE Region
    x  = np.squeeze(mode.getdata("FDE::data::material","x")); 
    y  = np.squeeze(mode.getdata("FDE::data::material","y")); 
    index_x = np.squeeze(mode.getdata("FDE::data::material","index_x"));
    index_y = np.squeeze(mode.getdata("FDE::data::material","index_y"));

    return x,y, index_x, index_y




if(__name__=="__main__"):
    with lumapi.MODE() as mode:
        
        # Disable Rendering
        mode.redrawoff()

        # Draw the waveguide structure using a custom function
        waveguide_draw(mode)

        # Add a finite-difference eigenmode (FDE) region to the simulation environment
        add_fde_region(mode)

        # Run the simulation, create a mesh, and compute the modes, then save
        mode.mesh()
        mode.save(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE + "\\waveguide_modes.lms")

        # Turn redraw back on and close LumAPI connection
        mode.redrawon()  

 
        x, y, index_x, index_y = getIndex(mode=mode)



        # Real Index Mesh
        plt.figure(1, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)


        plt.pcolormesh(x*1e6,y*1e6,np.real(np.transpose(index_x)),shading = 'gouraud',cmap = 'jet')
        plt.colorbar()

        plt.xlabel("x (\u00B5m)")
        plt.ylabel("y (\u00B5m)")
        plt.title("Waveguide Real Index Mesh")
        plt.tight_layout()


        # Save the file
        file_name_plot = os.path.join(MODE_WAVEGUIDE_DIRECTORY_WRITE[0], "index_real_profile_2D.png")
        plt.savefig(file_name_plot)



        # Imaginary Index Mesh
        plt.figure(2, figsize=(512/my_dpi, 256/my_dpi), dpi=my_dpi)
        plt.pcolormesh(x*1e6,y*1e6,np.imag(np.transpose(index_x)),shading = 'gouraud',cmap = 'jet')
        plt.colorbar()

        plt.xlabel("x (\u00B5m)")
        plt.ylabel("y (\u00B5m)")
        plt.title("Waveguide Imag Index Mesh")
        plt.tight_layout()


        # Save the file
        file_name_plot = os.path.join(MODE_WAVEGUIDE_DIRECTORY_WRITE[0], "index_imag_profile_2D.png")
        plt.savefig(file_name_plot)





        for i in range(1,3):
            # Add the waveguide
            wg_xmin = mode.getnamed("waveguide","x min")
            wg_xmax = mode.getnamed("waveguide","x max")

            r1 = sg.box(wg_xmin*1e6,0,wg_xmax*1e6,wg_thickness*1e6)

        
            
            if(slab_thickness > 0):
            
                #Add the slab
                slab_xmin = mode.getnamed("slab","x min")
                slab_xmax = mode.getnamed("slab","x max")
                r2 = sg.box(slab_xmin*1e6,0,slab_xmax*1e6,slab_thickness*1e6)

                # Cascaded union can work on a list of shapes
                merged_shape = so.unary_union([r1,r2])

                #exterior coordinates split into two arrays, xs and ys
                # which is how matplotlib will need for plotting
                xs, ys = merged_shape.exterior.xy
                plt.figure(i)
                plt.fill(xs, ys, alpha=0.5, fc='none', ec='w')
            else:
                xs, ys = r1.exterior.xy
                plt.figure(i)
                plt.fill(xs, ys, alpha=0.5, fc='none', ec='w')