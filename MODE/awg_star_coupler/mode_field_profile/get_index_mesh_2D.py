#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script plots the refractive index profile for the AWG star coupler
defined in the awg_input_taper.lms file.

"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup

# ------------------------- No inputs are required ---------------------------


def getIndex(mode):
    """Run the simulation and return the index mesh data."""
    mode.switchtolayout()
    mode.run()

    index = np.squeeze(mode.getdata("effective_index", "index_x"))
    x = np.squeeze(mode.getdata("effective_index", "x"))
    y = np.squeeze(mode.getdata("effective_index", "y"))
    return index, x, y


if __name__ == "__main__":
    spec, out, templates = setup("mode.awg_star_coupler", __file__)
    template_lms = templates[0]
    figures_dir = out["figures"] / "Index Profile"
    figures_dir.mkdir(parents=True, exist_ok=True)

    with lumapi.MODE(str(template_lms)) as mode:

        index, x, y = getIndex(mode)

    px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
    fig, ax = plt.subplots(figsize=(512 * px, 256 * px))

    c = ax.pcolormesh(x * 1e6, y * 1e6, np.real(np.transpose(index)),
                      shading='gouraud', cmap='jet')
    fig.colorbar(c, ax=ax)

    ax.set_xlabel("x (\u00B5m)")
    ax.set_ylabel("y (\u00B5m)")
    ax.set_title("Star Coupler Index Mesh")

    plt.tight_layout()
    plt.savefig(figures_dir / "index_profile_xz.png")
    plt.show()

