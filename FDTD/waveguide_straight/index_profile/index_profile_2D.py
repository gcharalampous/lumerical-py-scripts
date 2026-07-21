#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the refractive index profile of the cross-section (yz) for
the straight waveguide structure defined in the straight_wg.fsp file.

Monitor expected: ``index_yz``.
"""


# ----------------------------------------------------------------------------
# Imports from user input files
# ---------------------------------------------------------------------------

import lumapi
import matplotlib.pyplot as plt
import numpy as np

from project_layout import setup

# -------------------------- No inputs are required --------------------------


def getIndex(fdtd):
    # Get the data from the Index monitor
    index_yz = fdtd.getresult("index_yz", "index")
    return index_yz


if __name__ == "__main__":
    spec, out, templates = setup("fdtd.waveguide_straight", __file__)
    template_fsp = templates[0]  # straight_wg.fsp
    figures_dir = out["figure_groups"]["Index Profile"]

    with lumapi.FDTD(str(template_fsp)) as fdtd:
        index_yz = getIndex(fdtd=fdtd)

        # ------------------------------Cross-View------------------------------
        y = index_yz["y"].squeeze()
        z = index_yz["z"].squeeze()
        index_z = np.real(index_yz["index_z"].squeeze())

        px = 1 / plt.rcParams["figure.dpi"]  # pixel in inches
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.axis("equal")
        cmap = ax.pcolormesh(y * 1e6, z * 1e6, np.transpose(index_z), shading="gouraud", cmap="jet")
        fig.colorbar(cmap)
        ax.set_xlabel("y (um)")
        ax.set_ylabel("z (um)")
        ax.set_title("Cross-view (yz)")
        fig.tight_layout()
        plt.savefig(figures_dir / "index_profile_yz.png")
        plt.show()
