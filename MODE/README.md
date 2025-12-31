# Mode Solution Library for Photonic Simulations

## Purpose
This directory contains Lumerical MODE simulations used to extract guided modes, effective indices, and optical field profiles for integrated photonic waveguide structures. These simulations support geometry selection and provide inputs for downstream FDTD simulations.

## Features

### [awg-star-coupler](awg_star_coupler)
    This module simulates the aperture profile of a 2D star coupler using Lumerical MODE solutions. A star coupler is a key component in Arrayed Waveguide Grating (AWG) devices that distributes light from input waveguides to an array of output waveguides.

### [butt-coupling](butt_coupling)
    This simulation helps analyze how light couples between two waveguides. It focuses on mode interactions and improving device performance in butt-coupling configurations for photonic devices.

### [directional-coupler](directional_coupler)
    This module is used to efficiently extract supermode indices required to compute coupling length  without full 3D propagation simulations.

### [edge-coupler](edge_coupler)
    This module focuses on fiber or free-space Gaussian beam coupling and does not model on-chip laser mode evolution.

### [laser-tapered-waveguide](laser_tapered_waveguide)
    Calculates optical confinement characteristics of a tapered laser waveguide as the width progressively narrows. Tracks how optical modes behave when vertically displaced and determines how tapering affects mode distribution and confinement efficiency.
    
### [swg-grating](swg_grating)
    Simulate and analyze the transmission and reflection properties of a subwavelength grating (SWG) waveguide structure using MODE Solutions, extracting spectral response and mode characteristics across a wavelength range.

### [vertical-taper](vertical_taper)
    Effective index evolution is used to assess adiabatic taper behavior and guide taper length selection. The following module provides capabilities for analyzing vertical taper structures in photonics.

### [waveguide](waveguide)
    This directory contains Lumerical MODE simulations used to extract guided modes, effective indices, and optical field profiles for integrated photonic waveguide structures. These simulations support geometry selection and provide inputs for downstream FDTD simulations.
