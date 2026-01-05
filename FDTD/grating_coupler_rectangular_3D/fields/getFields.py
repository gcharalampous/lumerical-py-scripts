#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Extract and plot near fields for the rectangular 3D grating coupler.
# ----------------------------------------------------------------------------
import numpy as np
import lumapi
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from project_layout import setup


def get_fields(fdtd):
    """Return x, y, z axes plus xy/xz field monitors if present."""
    field_xy = fdtd.getelectric("xy_topview")
    x = fdtd.getdata("xy_topview", "x").squeeze()
    y = fdtd.getdata("xy_topview", "y").squeeze()

    try:
        field_xz = fdtd.getelectric("xz_sideview")
        z = fdtd.getdata("xz_sideview", "z").squeeze()
    except Exception:
        field_xz = None
        z = None

    return x, y, z, field_xy, field_xz


def plot_field_xy(x_axis, y_axis, field, title, output_path, xlabel, ylabel, px):
    c_wavelength = field.shape[-1] // 2
    c_data = np.transpose(field[:, :, 0, int(c_wavelength)])  # (len(y), len(x))

    fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
    cmap = ax.pcolormesh(
        x_axis * 1e6,
        y_axis * 1e6,
        c_data,
        shading="gouraud",
        cmap="jet",
        norm=LogNorm(vmin=1e-4, vmax=1),
    )
    fig.colorbar(cmap)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()


def plot_field_xz(x_axis, z_axis, field, title, output_path, xlabel, ylabel, px):
    c_wavelength = field.shape[-1] // 2
    c_data = np.transpose(field[:, 0, :, int(c_wavelength)])  # (len(z), len(x))

    fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
    cmap = ax.pcolormesh(
        x_axis * 1e6,
        z_axis * 1e6,
        c_data,
        shading="gouraud",
        cmap="jet",
        norm=LogNorm(vmin=1e-4, vmax=1),
    )
    fig.colorbar(cmap)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()


if __name__ == "__main__":
    # Setup project layout and figure directory
    spec, out, templates = setup("fdtd.grating_coupler_rectangular_3D", __file__)
    template_fsp = templates[0]
    fields_dir = out["figure_groups"].get("Fields", out["figures"])
    fields_dir.mkdir(parents=True, exist_ok=True)

    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.run()

        px = 1 / plt.rcParams["figure.dpi"]  # pixel to inch conversion

        x, y, z, E_xy, E_xz = get_fields(fdtd=fdtd)
        plot_field_xy(
            x, y, E_xy, "Top-view (xy)", fields_dir / "E_profile_xy.png", "x (um)", "y (um)", px
        )

        # Optional side-view (xz) if monitor exists
        if E_xz is not None and z is not None:
            plot_field_xz(
                x, z, E_xz, "Side-view (xz)", fields_dir / "E_profile_xz.png", "x (um)", "z (um)", px
            )