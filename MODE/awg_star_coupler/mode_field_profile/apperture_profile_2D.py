#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User-inputs are Not required.

The script calculates the apperture profile of the star coupler specified in
'user_inputs/awg_input_taper.lms'.

"""

# ----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

import lumapi
import matplotlib.pyplot as plt
import numpy as np

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
        Ep = np.squeeze(Ep)
        theta = np.squeeze(theta)
        # Normalize in dB scale
        Ep_dB = 20 * np.log10(abs(Ep))
        Ep_dB_unity = Ep_dB - np.max(Ep_dB)

        # Find -30 dB crossing angles FIRST
        threshold = -30
        above_threshold = Ep_dB_unity >= threshold
        crossings = np.where(np.diff(above_threshold.astype(int)))[0]
        crossing_angles = []
        for idx in crossings:
            theta1, theta2 = theta[idx], theta[idx + 1]
            dB1, dB2 = Ep_dB_unity[idx], Ep_dB_unity[idx + 1]
            theta_cross = theta1 + (threshold - dB1) * (theta2 - theta1) / (dB2 - dB1)
            crossing_angles.append(theta_cross)

        # Extract difr_angle
        positive_crossings = [a for a in crossing_angles if a > 0]
        difr_angle_extracted = min(positive_crossings)
        print(f"Far field -30 dB crossing angles: {[f'{a:.2f}°' for a in crossing_angles]}")
        print(f"Recommended difr_angle (half-angle): {difr_angle_extracted:.2f}°")
        print(f"Recommended difr_angle (total for BoxAWG): {2 * difr_angle_extracted:.2f}°")

        # NOW plot with all annotations
        px = 1 / plt.rcParams["figure.dpi"]
        fig, ax = plt.subplots(figsize=(512 * px, 256 * px))
        ax.plot(theta, Ep_dB_unity, label="Ep")
        ax.set_xlabel("\u03b8 (deg)")
        ax.set_ylabel("Transmission (dB)")
        ax.grid()
        ax.axhline(y=-30, linestyle="--", color="g")
        for angle in crossing_angles:
            ax.axvline(x=angle, linestyle="--", color="r", alpha=0.7)
            ax.text(angle, -28, f"{angle:.1f}°", color="r", fontsize=8, ha="center")
        fig.tight_layout()
        fig.savefig(figures_dir / "far_field_profile.png")
        plt.show()
