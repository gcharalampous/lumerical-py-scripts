#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Plot E-field profiles for the waveguide crossing structure.

Monitors are expected to be named `xy_topview`.
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from project_layout import setup
from pathlib import Path

spec, out, templates = setup("fdtd.waveguide_crossing", __file__)
template_fsp = templates[0]  # waveguide_crossing_multi_wg_taper.fsp
e_fields_dir = out["figure_groups"].get("E-fields", out["figures"] / "Fields")


def getFields(fdtd):
    """Extract electric field data from FDTD simulation."""
    field_xy = fdtd.getelectric("xy_topview")
    x = fdtd.getdata("xy_topview", "x").squeeze()
    y = fdtd.getdata("xy_topview", "y").squeeze()
    return x, y, field_xy


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.run()

        x, y, E_xy = getFields(fdtd=fdtd)
        c_wavelength = E_xy.shape[-1] // 2  # central wavelength index

        px = 1 / plt.rcParams['figure.dpi']  # pixel to inch conversion
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        cmap = ax.pcolormesh(
            x * 1e6,
            y * 1e6,
            np.transpose(E_xy[:, :, 0, c_wavelength]),
            shading='gouraud',
            cmap='jet',
            norm=LogNorm(vmin=1e-4, vmax=1),
        )
        fig.colorbar(cmap)
        plt.xlabel("x (um)")
        plt.ylabel("y (um)")
        plt.title("Top-view (xy)")
        plt.tight_layout()
        plt.savefig(e_fields_dir / "E_profile_xy.png")
        plt.show()
