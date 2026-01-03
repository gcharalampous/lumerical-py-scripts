#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot length sweep results for the directional coupler.

Performs a length sweep on the coupling length and plots the transmission
for through and coupled ports as a function of coupling length.
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup

spec, out, templates = setup("fdtd.directional_coupler", __file__)
template_fsp = templates[0]
figures_dir = out["figure_groups"].get("Sweep Transmission", out["figures"])


def getCouplingResponse(fdtd):
    """Extract length sweep results from FDTD simulation."""
    T = fdtd.getsweepresult("sweep_coupling_length", "Through")
    C = fdtd.getsweepresult("sweep_coupling_length", "Bar")
    return T, C


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.runsweep("sweep_coupling_length")

        T, C = getCouplingResponse(fdtd=fdtd)
        length = np.squeeze(T["coupling_length"])
        through = np.squeeze(T["T"])
        coupled = np.squeeze(C["T"])

        px = 1 / plt.rcParams['figure.dpi']

        # Linear scale
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(length * 1e6, through, label='Through', marker='o')
        ax.plot(length * 1e6, coupled, label='Coupled', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Length (um)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "sweep_length_linear.png")

        # Logarithmic scale (dB)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        through_db = 10 * np.log10(through)
        coupled_db = 10 * np.log10(coupled)
        ax.plot(length * 1e6, through_db, label='Through', marker='o')
        ax.plot(length * 1e6, coupled_db, label='Coupled', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Length (um)")
        ax.set_ylabel("Transmission (dB)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "sweep_length_dB.png")

        plt.show()
