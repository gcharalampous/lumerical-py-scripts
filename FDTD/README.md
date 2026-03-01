## FDTD Simulations

This repository contains various simulations using the Finite-Difference Time-Domain (FDTD) method, which is widely used in photonics to model the behavior of light in different structures. Each simulation is designed to analyze specific coupling mechanisms and efficiencies in waveguide systems.

## Features

### [Adiabatic Directional Coupler](adiabatic_directional_coupler)
- Simulates an adiabatic directional coupler where coupling occurs gradually over an extended interaction region.
- Calculates transmission characteristics and power transfer efficiency.
- Plots field profiles across the coupling region for optimization of device geometry.

### [Adiabatic Y-Branch](adiabatic_y_branch)
- Models a Y-branch waveguide splitter designed for adiabatic power splitting.
- Analyzes power distribution between output branches and transmission efficiency.
- Plots field profiles to assess splitting uniformity and minimize back-reflections.

### [Coupled Ring Coupler](coupled_ring_coupler)
- Simulates coupling between waveguides and coupled ring resonator structures.
- Analyzes resonance characteristics and coupling efficiency for multi-ring configurations.
- Plots field profiles and transmission spectra for resonant wavelengths.

### [Directional Coupler](directional_coupler)
- Simulates the coupling between two parallel waveguides.
- Calculates the power transfer between waveguides as a function of the coupling length.
- Plots the E-field profiles for different coupling lengths.

### [Disk Resonator Coupler](disk_resonator_coupler)
- Simulates the coupling between a waveguide and a disk resonator.
- Models the resonance and coupling efficiency as a function of the waveguide-resonator distance.
- Plots the E-field profiles of the resonator.

### [Edge Coupler](edge_coupler)
- Models light coupling from a waveguide to a 2D edge structure.
- Simulates the coupling efficiency and the E-field profile of the coupling region.

### [Grating Coupler 2D](grating_coupler_2D)
- Simulates the performance of a 2D grating coupler.
- Calculates the coupling efficiency and the angle of incidence required for maximum coupling.

### [Grating Coupler Rectangular 3D](grating_coupler_rectangular_3D)
- Simulates a 3D rectangular grating coupler for fiber-to-chip coupling.
- Calculates coupling efficiency, directionality, and far-field radiation patterns.
- Analyzes the influence of grating parameters on coupling performance.

### [MMI Couplers](mmi_couplers)
- Models the multi-mode interference (MMI) coupler performance.
- Calculates the output power distribution for different input waveguide configurations.
- Plots the E-field profiles at the output of the MMI.

### [Ring Resonator Coupler](ring_resonator_coupler)
- Models the coupling between a waveguide and a ring resonator.
- Calculates the resonance wavelength and the coupling efficiency.
- Plots the E-field profiles inside the resonator.

### [SWG Grating](swg_grating)
- Simulates the performance of a slab waveguide (SWG) grating coupler.
- Calculates the diffraction efficiency and the far-field diffraction patterns.
- Plots the E-field profiles of the grating coupler.

### [Vertical Taper](vertical_taper)
- Simulates the performance of a vertical taper between waveguide sections with different heights.
- Calculates the transmission and power transfer efficiency between waveguide segments.
- Plots the E-field profiles across the taper region.

### [Waveguide Bend](waveguide_bend)
- Calculates the transmission as a function of the bending radius.
- Plots the E-field profiles at the bending section.

### [Waveguide Crossing](waveguide_crossing)
- Simulates the field profile at waveguide crossings.
- Calculates the coupling between intersecting waveguides as a function of the crossing angle.
- Plots the E-field profile across the intersection.

### [Waveguide Mode Taper](waveguide_mode_taper)
- Plots the E-field profile of the propagated mode across the tapered waveguide section and calculates transmission.
- Sweeps the taper-tip width and length to calculate the transmission of the fundamental TE or TM mode.

### [Waveguide Straight](waveguide_straight)
- Plots the E-field profile of the propagated mode.
- Sweeps the waveguide width to calculate the transmission of the fundamental TE or TM mode.

## Usage Instructions
To run the simulations, ensure you have the necessary software installed and follow the instructions provided in the main README file.

