#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot gap sweep results for the coupled ring coupler.

Assumes a sweep named `sweep_coupling_gap` with results `Through` and `Bar`.
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
    """Return through and coupled sweep results."""
    T = fdtd.getsweepresult("sweep_coupling_gap", "Through")
    C = fdtd.getsweepresult("sweep_coupling_gap", "Bar")
    return T, C


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.runsweep("sweep_coupling_gap")

        T, C = getCouplingResponse(fdtd=fdtd)
        gap = np.squeeze(T["coupling gap"])
        through = np.squeeze(T["T"])
        coupled = np.squeeze(C["T"])

        px = 1 / plt.rcParams['figure.dpi']

        # Through (linear)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(gap * 1e6, abs(through), label='Through', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (um)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "gap_sweep_through.png")

        # Coupled (linear)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(gap * 1e6, abs(coupled), label='Coupled', marker='o', color='orange')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (um)")
        ax.set_ylabel("Transmission (Linear)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "gap_sweep_coupled.png")

        # Through (dB)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        through_db = 10 * np.log10(abs(through))
        ax.plot(gap * 1e6, through_db, label='Through', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (um)")
        ax.set_ylabel("Transmission (dB)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "gap_sweep_through_dB.png")

        # Coupled (dB)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        coupled_db = 10 * np.log10(abs(coupled))
        ax.plot(gap * 1e6, coupled_db, label='Coupled', marker='o', color='orange')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("Gap (um)")
        ax.set_ylabel("Transmission (dB)")
        ax.set_title(fdtd.getnamed("source", "mode selection"))
        plt.tight_layout()
        plt.savefig(figures_dir / "gap_sweep_coupled_dB.png")

        plt.show()
