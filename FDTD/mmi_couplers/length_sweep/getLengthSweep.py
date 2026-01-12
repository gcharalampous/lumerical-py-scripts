#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot MMI length sweep results.

Assumes a sweep named `sweep_Lmmi` with results `T1` and `T2`.
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

spec, out, templates = setup("fdtd.mmi_couplers", __file__)
template_fsp = templates[file_index]
figures_dir = out["figure_groups"].get("Length Sweep", out["figures"])


def getLengthResponse(fdtd):
    """Return through port sweep results."""
    T1 = fdtd.getsweepresult("sweep_Lmmi", "T1")
    T2 = fdtd.getsweepresult("sweep_Lmmi", "T2")
    return T1, T2


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.runsweep("sweep_Lmmi")

        T1, T2 = getLengthResponse(fdtd=fdtd)
        length = np.squeeze(T1["Lmmi"])
        
        # Extract T data and handle wavelength dimension
        T1_data = np.squeeze(T1["T"])
        T2_data = np.squeeze(T2["T"])
        
        # Slice at center wavelength if multiple wavelength points
        if T1_data.ndim > 1:
            c_wavelength = int(np.rint(T1_data.shape[0] / 2))
            T1_data = T1_data[c_wavelength, :]
            T2_data = T2_data[c_wavelength, :]
        
        through_1 = T1_data
        through_2 = T2_data

        px = 1 / plt.rcParams['figure.dpi']

        # Port 1 (linear)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(length * 1e6, abs(through_1), label='Port 1', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("MMI Length (um)")
        ax.set_ylabel("Transmission (Linear)")
        plt.tight_layout()
        plt.savefig(figures_dir / "length_sweep_port1.png")

        # Port 2 (linear)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(length * 1e6, abs(through_2), label='Port 2', marker='o', color='orange')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("MMI Length (um)")
        ax.set_ylabel("Transmission (Linear)")
        plt.tight_layout()
        plt.savefig(figures_dir / "length_sweep_port2.png")

        # Port 1 (dB)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        through_1_db = 10 * np.log10(abs(through_1))
        ax.plot(length * 1e6, through_1_db, label='Port 1', marker='o')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("MMI Length (um)")
        ax.set_ylabel("Transmission (dB)")
        plt.tight_layout()
        plt.savefig(figures_dir / "length_sweep_port1_dB.png")

        # Port 2 (dB)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        through_2_db = 10 * np.log10(abs(through_2))
        ax.plot(length * 1e6, through_2_db, label='Port 2', marker='o', color='orange')
        ax.grid(which='both', alpha=0.3)
        ax.legend()
        ax.set_xlabel("MMI Length (um)")
        ax.set_ylabel("Transmission (dB)")
        plt.tight_layout()
        plt.savefig(figures_dir / "length_sweep_port2_dB.png")

        plt.show()
