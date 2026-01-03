#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Extract and plot transmission response for the ring resonator coupler.

Assumes monitors named `T` and `C` in the template project.
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
from user_simulation_parameters import file_index

spec, out, templates = setup("fdtd.ring_resonator_coupler", __file__)
template_fsp = templates[file_index]
figures_dir = out["figure_groups"].get("Transmission", out["figures"])


def getCouplingResponse(fdtd):
    """Return through and coupled transmission along with frequency array."""
    T = np.squeeze(fdtd.getresult("T", "expansion for ").get("T_forward"))
    C = np.squeeze(fdtd.getresult("C", "expansion for ").get("T_forward"))
    f = np.squeeze(fdtd.getdata("through", "f"))
    return T, C, f


if __name__ == "__main__":
    with lumapi.FDTD(str(template_fsp)) as fdtd:
        fdtd.run()

        T, C, f = getCouplingResponse(fdtd=fdtd)
        wavelength = (scpy.c / f) * 1e6  # micrometers

        px = 1 / plt.rcParams['figure.dpi']

        # Linear magnitude response (separate plots)
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(wavelength, abs(T), label='Through', marker='o')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Transmission (Linear)")
        plt.tight_layout()
        plt.savefig(figures_dir / "frequency_response_through.png")

        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(wavelength, abs(C), label='Coupled', marker='o')
        ax.grid(which='both')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Transmission (Linear)")
        plt.tight_layout()
        plt.savefig(figures_dir / "frequency_response_coupled.png")

        # Log magnitude response
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        T_db = 10 * np.log10(abs(T))
        C_db = 10 * np.log10(abs(C))

        ax.plot(wavelength, T_db, label='Through', marker='o')
        ax.plot(wavelength, C_db, label='Coupled', marker='o')
        ax.grid(which='major')
        ax.legend()
        ax.set_xlabel("Wavelength (um)")
        ax.set_ylabel("Transmission (dB)")

        plt.tight_layout()
        plt.savefig(figures_dir / "frequency_response_dB.png")

        plt.show()