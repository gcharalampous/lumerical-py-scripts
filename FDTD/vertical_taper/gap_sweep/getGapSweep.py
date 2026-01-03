#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot gap sweep results for the vertical taper.

Assumes a sweep named `sweep_gap` with results `T`.
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import sys
from pathlib import Path
from project_layout import setup


spec, out, templates = setup("fdtd.vertical_taper", __file__)
template_fsp = templates[0]
figures_dir = out["figures"] / "Gap Sweep"
figures_dir.mkdir(parents=True, exist_ok=True)


def getGapSweepResponse(fdtd):
    """Return gap sweep transmission results."""
    T = fdtd.getsweepresult("sweep_gap", "T")
    
    lambda_array = np.squeeze(T['lambda'])

    if lambda_array.size > 1:
        index_array = int(np.floor(lambda_array.size / 2))
        transmission = abs(T["T"][index_array])
        gap = np.squeeze(T["vertical_gap"])
        lambda0 = lambda_array[index_array]
        print(f"The central wavelength is: {lambda0*1e6:.3f} um")
    else:
        transmission = abs(T["T"])
        gap = np.squeeze(T["vertical_gap"])
        lambda0 = lambda_array if lambda_array.size == 1 else lambda_array[0]
        print(f"The central wavelength is: {lambda0*1e6:.3f} um")
    
    return transmission, gap, lambda0


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.runsweep("sweep_gap")

        transmission, gap, lambda0 = getGapSweepResponse(fdtd=fdtd)

        px = 1 / plt.rcParams['figure.dpi']

        # Transmission (linear)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(gap * 1e6, abs(transmission), label='Transmission', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (um)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "gap_sweep_transmission.png")

        # Transmission (dB)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        transmission_db = 10 * np.log10(abs(transmission))
        ax.plot(gap * 1e6, transmission_db, label='Transmission', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (um)")
        ax.set_ylabel("Transmission (dB)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "gap_sweep_transmission_dB.png")

        plt.show()
