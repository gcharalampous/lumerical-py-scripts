#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot transmission response for the coupled ring coupler.

Assumes monitors named `through` and `bar` in the template project.
"""

#----------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
import scipy.constants as scpy
from project_layout import setup
import sys
from pathlib import Path

# Import user configuration
user_inputs_dir = Path(__file__).resolve().parent.parent / "user_inputs"
sys.path.insert(0, str(user_inputs_dir))
from user_simulation_parameters import template_index

spec, out, templates = setup("fdtd.coupled_ring_coupler", __file__)
template_fsp = templates[template_index]
figures_dir = out["figure_groups"].get("Frequency Response", out["figures"])

TARGET_3DB = -3.01  # Target 3 dB point for quick sanity check


def getCrossResponse(fdtd):
    """Return through and bar transmission along with frequency array."""
    T1 = np.squeeze(fdtd.getresult("through", "T").get("T"))
    T2 = np.squeeze(fdtd.getresult("bar", "T").get("T"))
    f = np.squeeze(fdtd.getdata("through", "f"))
    return T1, T2, f


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.run()

        T1, T2, f = getCrossResponse(fdtd=fdtd)
        wavelength = (scpy.c / f) * 1e6  # micrometers

        px = 1 / plt.rcParams['figure.dpi']

        # Linear magnitude response (separate plots)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(wavelength, abs(T1), label='Through', marker='o')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Transmission (Linear)")
        plt.tight_layout()
        plt.savefig(figures_dir / "frequency_response_through.png")

        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(wavelength, abs(T2), label='Coupled', marker='o')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Transmission (Linear)")
        plt.tight_layout()
        plt.savefig(figures_dir / "frequency_response_coupled.png")

        # Log magnitude response
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        T1_db = 10 * np.log10(abs(T1))
        T2_db = 10 * np.log10(abs(T2))

        ax.plot(wavelength, T1_db, label='Through', marker='o')
        ax.plot(wavelength, T2_db, label='Coupled', marker='o')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Transmission (dB)")

        plt.tight_layout()
        plt.savefig(figures_dir / "frequency_response_dB.png")

        plt.show()
