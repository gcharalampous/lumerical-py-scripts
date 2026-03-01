#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are not required.

The script calculates the mode profile for the waveguide bend structure
defined in the circular_bend.fsp template.

The script extracts and plots:
- Top-view E-field magnitude (xy)
- Output cross-section E-field magnitude (xz)

"""

#----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup
from FDTD.waveguide_bend.user_inputs.user_simulation_parameters import file_index


def getFields(fdtd):
    fdtd.run()

    x_top = np.squeeze(fdtd.getdata("xy_topdown", "x"))
    y_top = np.squeeze(fdtd.getdata("xy_topdown", "y"))
    ex_top = np.squeeze(fdtd.getdata("xy_topdown", "Ex"))
    ey_top = np.squeeze(fdtd.getdata("xy_topdown", "Ey"))
    ez_top = np.squeeze(fdtd.getdata("xy_topdown", "Ez"))

    x_out = np.squeeze(fdtd.getdata("transmission", "x"))
    z_out = np.squeeze(fdtd.getdata("transmission", "z"))
    ex_out = np.squeeze(fdtd.getdata("transmission", "Ex"))
    ey_out = np.squeeze(fdtd.getdata("transmission", "Ey"))
    ez_out = np.squeeze(fdtd.getdata("transmission", "Ez"))

    e_top = np.sqrt(np.abs(ex_top) ** 2 + np.abs(ey_top) ** 2 + np.abs(ez_top) ** 2)
    e_out = np.sqrt(np.abs(ex_out) ** 2 + np.abs(ey_out) ** 2 + np.abs(ez_out) ** 2)

    return x_top, y_top, e_top, x_out, z_out, e_out


if __name__ == "__main__":
    spec, out, templates = setup("fdtd.waveguide_bend", __file__)
    template_fsp = templates[file_index]  # circular_bend.fsp
    figures_dir = out["figure_groups"]["Fields"]

    with lumapi.FDTD(str(template_fsp)) as fdtd:
        x_top, y_top, e_top, x_out, z_out, e_out = getFields(fdtd=fdtd)
        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches

# --------------------------------Top-View---------------------------------
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        e_top_db = 20 * np.log10(np.transpose(e_top))
        cmap = ax.pcolormesh(x_top * 1e6, y_top * 1e6, e_top_db,
                             shading='gouraud', cmap='jet', vmin=-40, vmax=0)
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title("Top-view (xy)")
        plt.tight_layout()
        plt.savefig(figures_dir / "E_profile_xy.png")

# ----------------------------Cross-Section--------------------------------
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        cmap = ax.pcolormesh(x_out * 1e6, z_out * 1e6, np.transpose(e_out),
                             shading='gouraud', cmap='jet', vmin=0, vmax=1)
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("z (um)")
        plt.title("Cross-section (xz)")
        plt.tight_layout()
        plt.savefig(figures_dir / "E_profile_xz.png")
        plt.show()


