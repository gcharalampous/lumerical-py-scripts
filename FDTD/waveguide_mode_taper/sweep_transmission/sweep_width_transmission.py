#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot width sweep results for the waveguide mode taper.

Assumes a sweep named ``sweep_width`` with result ``T`` defined in
the template .fsp file (mode_taper.fsp).
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup


spec, out, templates = setup("fdtd.waveguide_mode_taper", __file__)
template_fsp = templates[0]
figures_dir = out["figure_groups"]["Sweep Transmission"]


def getWidthSweepResponse(fdtd):
    """Return width sweep transmission results."""
    T = fdtd.getsweepresult("sweep_width", "T")

    lambda_array = np.squeeze(T['lambda'])
    taper_width = np.squeeze(T["taper_width"])
    T_forward = np.squeeze(T["T_forward"])

    if lambda_array.size > 1:
        index_array = int(np.floor(lambda_array.size / 2))
        lambda0 = lambda_array[index_array]
        # T_forward shape after squeeze: (n_wavelengths, n_widths)
        if T_forward.ndim == 2:
            transmission = abs(T_forward[index_array, :])
        else:
            transmission = abs(T_forward)
        print(f"The central wavelength is: {lambda0*1e6:.3f} um")
    else:
        lambda0 = float(lambda_array)
        transmission = np.squeeze(abs(T_forward))
        print(f"The central wavelength is: {lambda0*1e6:.3f} um")

    return transmission, taper_width, lambda0


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.runsweep("sweep_width")

        transmission, taper_width, lambda0 = getWidthSweepResponse(fdtd=fdtd)

        px = 1 / plt.rcParams['figure.dpi']

        # Transmission (linear)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(taper_width * 1e6, abs(transmission), label='Transmission', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Taper Width (um)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "sweep_width_linear.png")

        # Transmission (dB)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        transmission_db = 10 * np.log10(abs(transmission))
        ax.plot(taper_width * 1e6, transmission_db, label='Transmission', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Taper Width (um)")
        ax.set_ylabel("Transmission (dB)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "sweep_width_dB.png")
        plt.show()