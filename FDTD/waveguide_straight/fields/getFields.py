#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Plot 2D E-field profiles for the straight waveguide template.

The script plots the electric-field intensity distributions for the top-view
(xy), side-view (xz) and cross-section (yz) of the straight waveguide.

Monitors expected: ``xy_topdown``, ``xz_sideview``, ``transmission``.
"""

# ----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import lumapi
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

from project_layout import setup

spec, out, templates = setup("fdtd.waveguide_straight", __file__)
template_fsp = templates[0]  # straight_wg.fsp
e_fields_dir = out["figure_groups"].get("Fields", out["figures"])


def getFields(fdtd):
    """Extract electric-field intensity data from the 2D profile monitors."""
    # 2D top-view (xy)
    x_xy = fdtd.getdata("xy_topdown", "x").squeeze()
    y_xy = fdtd.getdata("xy_topdown", "y").squeeze()
    E_xy = fdtd.getelectric("xy_topdown")

    # 2D side-view (xz)
    x_xz = fdtd.getdata("xz_sideview", "x").squeeze()
    z_xz = fdtd.getdata("xz_sideview", "z").squeeze()
    E_xz = fdtd.getelectric("xz_sideview")

    # 2D cross-section (yz)
    y_yz = fdtd.getdata("transmission", "y").squeeze()
    z_yz = fdtd.getdata("transmission", "z").squeeze()
    E_yz = fdtd.getelectric("transmission")

    return x_xy, y_xy, E_xy, x_xz, z_xz, E_xz, y_yz, z_yz, E_yz


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.run()

        x_xy, y_xy, E_xy, x_xz, z_xz, E_xz, y_yz, z_yz, E_yz = getFields(fdtd=fdtd)
        c_wavelength = E_xy.shape[-1] // 2  # central wavelength index

        px = 1 / plt.rcParams["figure.dpi"]  # pixel to inch conversion

        # -------------------------------Top-view (xy)-------------------------------
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        cmap = ax.pcolormesh(
            x_xy * 1e6,
            y_xy * 1e6,
            np.transpose(E_xy[:, :, 0, int(c_wavelength)]),
            shading="gouraud",
            cmap="jet",
            norm=LogNorm(vmin=1e-4, vmax=1),
        )
        fig.colorbar(cmap)
        ax.set_xlabel("x (um)")
        ax.set_ylabel("y (um)")
        ax.set_title("Top-view (xy)")
        fig.tight_layout()
        plt.savefig(e_fields_dir / "E_profile_xy.png")

        # -------------------------------Side-view (xz)------------------------------
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        cmap = ax.pcolormesh(
            x_xz * 1e6,
            z_xz * 1e6,
            np.transpose(E_xz[:, 0, :, int(c_wavelength)]),
            shading="gouraud",
            cmap="jet",
            norm=LogNorm(vmin=1e-4, vmax=1),
        )
        fig.colorbar(cmap)
        ax.set_xlabel("x (um)")
        ax.set_ylabel("z (um)")
        ax.set_title("Side-view (xz)")
        fig.tight_layout()
        plt.savefig(e_fields_dir / "E_profile_xz.png")

        # -----------------------------Cross-section (yz)----------------------------
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.axis("equal")
        cmap = ax.pcolormesh(
            y_yz * 1e6,
            z_yz * 1e6,
            np.transpose(E_yz[0, :, :, int(c_wavelength)]),
            shading="gouraud",
            cmap="jet",
            norm=LogNorm(vmin=1e-4, vmax=1),
        )
        fig.colorbar(cmap)
        ax.set_xlabel("y (um)")
        ax.set_ylabel("z (um)")
        ax.set_title("Cross-section (yz)")
        fig.tight_layout()
        plt.savefig(e_fields_dir / "E_profile_yz.png")
        plt.show()
