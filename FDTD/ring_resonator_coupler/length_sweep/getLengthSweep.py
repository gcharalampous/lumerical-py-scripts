#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot length sweep results for the ring resonator coupler.

Assumes a sweep named `sweep_straight_coupler` with results `Through` and `Bar`.
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
from user_simulation_parameters import file_index

spec, out, templates = setup("fdtd.ring_resonator_coupler", __file__)
template_fsp = templates[file_index]
figures_dir = out["figures"] / "Length Sweep"
figures_dir.mkdir(parents=True, exist_ok=True)


def getCouplingResponse(fdtd):
    """Return through and coupled sweep results."""
    T = fdtd.getsweepresult("sweep_coupling_length", "T")
    C = fdtd.getsweepresult("sweep_coupling_length", "C")
    return T, C

# Validation: length sweep only works with racetrack_coupler (file_index=2)
if file_index != 2:
    raise ValueError(
        f"Length sweep requires racetrack_coupler (file_index=2), "
        f"but file_index={file_index} was selected. "
        f"Please set file_index=2 in user_inputs/user_simulation_parameters.py"
    )


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.runsweep("sweep_coupling_length")

        T, C = getCouplingResponse(fdtd=fdtd)
        length = np.squeeze(T["coupling_length"])
        through = np.squeeze(T["T"])
        coupled = np.squeeze(C["T"])

        px = 1 / plt.rcParams['figure.dpi']

        # Through (linear)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(length * 1e6, abs(through), label='Through', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Length (μm)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "length_sweep_through.png")

        # Coupled (linear)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(length * 1e6, abs(coupled), label='Coupled', marker='o', color='orange')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Length (μm)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "length_sweep_coupled.png")

        # Combined plot
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(length * 1e6, abs(through), label='Through', marker='o')
        ax.plot(length * 1e6, abs(coupled), label='Coupled', marker='o', color='orange')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Length (μm)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "length_sweep_combined.png")

        plt.show()