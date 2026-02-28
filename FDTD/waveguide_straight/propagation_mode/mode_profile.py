#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Plot E-field mode profiles for the straight waveguide template.

The script calculates a slice of the E-field along the y-direction and z-
direction. Additionally, the 2D E-field distributions for the top-view,
side-view and cross-section of the waveguide.

Monitors expected: ``linear_y``, ``linear_z``, ``xy_topdown``, ``xz_sideview``,
``transmission``.
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup

spec, out, templates = setup("fdtd.waveguide_straight", __file__)
template_fsp = templates[0]
mode_profile_dir = out["figure_groups"]["Mode Profile"]
e_fields_dir = out["figure_groups"]["Fields"]


def getFields(fdtd):
    """Extract electric-field data from all profile monitors."""
    # 1D slices
    y = fdtd.getdata("linear_y", "y").squeeze()
    Ey_lin = np.sqrt(
        abs(fdtd.getdata("linear_y", "Ex").squeeze())**2
        + abs(fdtd.getdata("linear_y", "Ey").squeeze())**2
        + abs(fdtd.getdata("linear_y", "Ez").squeeze())**2
    )

    z = fdtd.getdata("linear_z", "z").squeeze()
    Ez_lin = np.sqrt(
        abs(fdtd.getdata("linear_z", "Ex").squeeze())**2
        + abs(fdtd.getdata("linear_z", "Ey").squeeze())**2
        + abs(fdtd.getdata("linear_z", "Ez").squeeze())**2
    )

    # 2D top-view (xy)
    x_xy = fdtd.getdata("xy_topdown", "x").squeeze()
    y_xy = fdtd.getdata("xy_topdown", "y").squeeze()
    E_xy = np.sqrt(
        abs(fdtd.getdata("xy_topdown", "Ex").squeeze())**2
        + abs(fdtd.getdata("xy_topdown", "Ey").squeeze())**2
        + abs(fdtd.getdata("xy_topdown", "Ez").squeeze())**2
    )

    # 2D side-view (xz)
    x_xz = fdtd.getdata("xz_sideview", "x").squeeze()
    z_xz = fdtd.getdata("xz_sideview", "z").squeeze()
    E_xz = np.sqrt(
        abs(fdtd.getdata("xz_sideview", "Ex").squeeze())**2
        + abs(fdtd.getdata("xz_sideview", "Ey").squeeze())**2
        + abs(fdtd.getdata("xz_sideview", "Ez").squeeze())**2
    )

    # 2D cross-section (yz)
    y_yz = fdtd.getdata("transmission", "y").squeeze()
    z_yz = fdtd.getdata("transmission", "z").squeeze()
    E_yz = np.sqrt(
        abs(fdtd.getdata("transmission", "Ex").squeeze())**2
        + abs(fdtd.getdata("transmission", "Ey").squeeze())**2
        + abs(fdtd.getdata("transmission", "Ez").squeeze())**2
    )

    return (y, Ey_lin, z, Ez_lin,
            x_xy, y_xy, E_xy,
            x_xz, z_xz, E_xz,
            y_yz, z_yz, E_yz)


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.run()

        (y, Ey_lin, z, Ez_lin,
         x_xy, y_xy, E_xy,
         x_xz, z_xz, E_xz,
         y_yz, z_yz, E_yz) = getFields(fdtd)

        px = 1 / plt.rcParams['figure.dpi']

        # ---- Linear-Y mode profile ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(y * 1e6, Ey_lin)
        ax.grid()
        ax.set_xlabel("y (\u00B5m)")
        ax.set_ylabel("E$_y$")
        ax.set_title("Mode profile (linear-y)")
        plt.tight_layout()
        plt.savefig(mode_profile_dir / "mode_profile_linear_y.png")

        # ---- Linear-Z mode profile ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(z * 1e6, Ez_lin)
        ax.grid()
        ax.set_xlabel("z (\u00B5m)")
        ax.set_ylabel("E$_z$")
        ax.set_title("Mode profile (linear-z)")
        plt.tight_layout()
        plt.savefig(mode_profile_dir / "mode_profile_linear_z.png")

        # ---- Top-view (xy) ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.pcolormesh(x_xy * 1e6, y_xy * 1e6,
                       np.transpose(E_xy), shading='gouraud', cmap='jet')
        ax.set_xlabel("x (\u00B5m)")
        ax.set_ylabel("y (\u00B5m)")
        ax.set_title("Top-view (xy)")
        plt.tight_layout()
        plt.savefig(e_fields_dir / "E_profile_xy.png")

        # ---- Side-view (xz) ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.pcolormesh(x_xz * 1e6, z_xz * 1e6,
                       np.transpose(E_xz), shading='gouraud', cmap='jet')
        ax.set_xlabel("x (\u00B5m)")
        ax.set_ylabel("z (\u00B5m)")
        ax.set_title("Side-view (xz)")
        plt.tight_layout()
        plt.savefig(e_fields_dir / "E_profile_xz.png")

        # ---- Cross-section (yz) ----
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.pcolormesh(y_yz * 1e6, z_yz * 1e6,
                       np.transpose(E_yz), shading='gouraud', cmap='jet')
        ax.set_xlabel("y (\u00B5m)")
        ax.set_ylabel("z (\u00B5m)")
        ax.set_title("Cross-section (yz)")
        plt.tight_layout()
        plt.savefig(mode_profile_dir / "E_profile_yz.png")

        plt.show()



