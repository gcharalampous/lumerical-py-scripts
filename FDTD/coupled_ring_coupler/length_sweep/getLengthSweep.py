#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot length sweep results for the coupled ring coupler.

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
import sys
from pathlib import Path

# Import user configuration
user_inputs_dir = Path(__file__).resolve().parent.parent / "user_inputs"
sys.path.insert(0, str(user_inputs_dir))
from user_simulation_parameters import template_index

spec, out, templates = setup("fdtd.coupled_ring_coupler", __file__)
template_fsp = templates[template_index]
figures_dir = out["figure_groups"].get("Sweep Transmission", out["figures"])


def getCouplingResponse(fdtd):
    """Extract length sweep results from FDTD simulation."""
    T = fdtd.getsweepresult("sweep_coupling_straight", "Through")
    C = fdtd.getsweepresult("sweep_coupling_straight", "Bar")
    return T, C


# Validation: length sweep only works with racetrack_coupler (template_index=1)
if template_index != 1:
    raise ValueError(
        f"Length sweep requires racetrack_coupler (template_index=1), "
        f"but template_index={template_index} was selected. "
        f"Please set template_index=1 in user_inputs/user_simulation_parameters.py"
    )

if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        # fdtd.runsweep("sweep_coupling_straight")

        T, C = getCouplingResponse(fdtd=fdtd)
        length = np.squeeze(T["coupling length"])
        through = np.squeeze(T["T"])
        coupled = np.squeeze(C["T"])

        px = 1 / plt.rcParams['figure.dpi']

        # Linear scale
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(length * 1e6, abs(through), label='Through', marker='o')
        ax.plot(length * 1e6, abs(coupled), label='Coupled', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Length (um)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "sweep_length_linear.png")

        # Logarithmic scale (dB)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        through_db = 10 * np.log10(abs(through))
        coupled_db = 10 * np.log10(abs(coupled))
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
