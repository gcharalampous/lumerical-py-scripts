#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the apperture profile of the star coupler specified in
'user_inputs/awg_input_taper.lms'.

"""

#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import numpy as np
import lumapi
import matplotlib.pyplot as plt
from project_layout import setup

# ------------------------- No inputs are required ---------------------------


def getFarField(mode):
    """Run the simulation and return the far-field data."""
    mode.switchtolayout()
    mode.run()
    mode.save()

    Ep = mode.farfield2d("monitor_field")
    theta = mode.farfieldangle("monitor_field")
    return Ep, theta


if __name__ == "__main__":
    spec, out, templates = setup("mode.awg_star_coupler", __file__)
    template_lms = templates[0]
    figures_dir = out["figures"] / "Far Field Profile"
    figures_dir.mkdir(parents=True, exist_ok=True)

    with lumapi.MODE(str(template_lms)) as mode:

        Ep, theta = getFarField(mode)

        # Normalize in dB scale
        Ep_dB = 10 * np.log10(abs(Ep))
        Ep_dB_unity = 10 * np.log10(abs(Ep)) - np.max(Ep_dB)

        px = 1 / plt.rcParams['figure.dpi']  # pixel in inches

        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(theta, Ep_dB_unity, label='Ep')
        ax.set_xlabel("\u03B8 (deg)")
        ax.set_ylabel("Transmission (dB)")
        ax.grid()

        ax.axhline(y=-30, linestyle='--', color='g')

        ax.axvline(x=-30, linestyle='--', color='r')
        ax.axvline(x=30, linestyle='--', color='r')

        fig.tight_layout()
        fig.savefig(figures_dir / "far_field_profile.png")
        plt.show()