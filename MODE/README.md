# Mode Solution Library for Photonic Simulations

This repository contains a collection of Python-based simulations and calculations for integrated photonics, focusing on mode analysis, coupling efficiencies, and waveguide characteristics.

## Features

### [awg-star-coupler](awg_star_coupler)
  - Simulates the aperture profile of a 2D star coupler.

### [butt-coupling](butt_coupling)
  - Visualizes mode profiles for two coupled waveguides.
  - Computes overlap integrals to quantify coupling efficiency.
  - Analyzes misalignment effects on coupling.
  - Studies coupling efficiency as a function of the second waveguide width for fundamental TE/TM modes.

### [directional-coupler](directional_coupler)
  - Visualizes symmetric and antisymmetric mode profiles.
  - Calculates the coupling length, \(L_{\pi}\), as a function of gap and distance between waveguides.

### [edge-coupler](edge_coupler)
  - Evaluates overlap between Gaussian beam and waveguide mode profiles.
  - Examines coupling efficiency as a function of Gaussian beam Mode-Field Diameter (MFD).
  - Analyzes the impact of waveguide thickness on overlap efficiency.

### [swg-grating](swg_grating)
  - Calculates the transmission and reflection properties of a sub-wavelength grating.

### [vertical-taper](vertical_taper)
  - Computes effective index variation as a function of taper length for vertically tapered structures.

### [waveguide](waveguide)
  - Visualizes mode profiles for various waveguide configurations.
  - Calculates effective index variations with respect to waveguide width and height.
  - Models absorption loss due to metal layer deposition on waveguides.
  - Estimates the Q-factor and Free Spectral Range (FSR) for racetrack resonators.
  - Calculates straight-to-bend waveguide loss.
  - Determines confinement factors in Phase Change Materials (PCM).