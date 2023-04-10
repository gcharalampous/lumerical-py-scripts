# Welcome

    lumerical-py-scripts
     └──FDTD
         ├──waveguide-straight
         ├──waveguide-bend
         ├──waveguide-mode-taper
         ├──vertical-taper
         ├──edge-coupler
         ├──waveguide-crossing
         ├──ring-resonator-coupling
         ├──mmi-coupler
         ├──disk-resonator-coupler
         └──directional-coupler
    
     └──MODE 
         ├──waveguide 
         ├──vertical-taper 
         ├──edge-coupler
         ├──directional-coupler
         ├──disk-waveguide
         └──waveguide-heater

## Why this Repository?

In this repositoty you will find useful scripts to optimize your workflow and automate your daily design tasks. All you need to do is to modify the files under `user_inputs` in each subdirectory and run the scripts. The repo is splitted into two main simulation branches with multiple subcategories each:

### 1. [FDTD](/FDTD)

- [x] [waveguide-straight](FDTD/waveguide-straight): Mode profile and transmission simulations for a straight waveguide.

- [x] [waveguide-bend](FDTD/waveguide-bend): Calculates the bending loss and mode profile. 

- [x] [waveguide-mode-taper](FDTD/waveguide-mode-taper): Calculates the adiabatic length of the tapered waveguide.

- [ ] [vertical-taper](FDTD/vertical-taper): Calculates the transmission on the upper waveguide.

- [ ] [edge-coupler](FDTD/edge-coupler): Calculates the coupling loss between a fiber (Gaussian) mode and a waveguide mode.

- [ ] [waveguide-crossing](waveguide-crossing): Calculations the transmission and crosstalk of a linear taper waveguide-crossing.

- [ ] [ring-resonator-coupler](ring-resonator-coupler): Calculates the coupling of a (a) rectangular, (b) concentric, and (c) straight sections ring.

- [ ] [mmi-coupler](mmi-coupler): Calculates the coupling and plots the E-field image of a (a) 2x2 MMI coupler.

- [ ] [disk-resonator-coupler](disk-resonator-coupler): Calculates the coupling of a (a) weakly tapered disk resonator.

- [ ] [directional-coupler](directional-coupler): Calculates the coupling and plots the E-field of an s-bend directional coupler.

### 2. [MODE Solutions](/MODE)

- [x] [waveguide](MODE/waveguide): Calculates the effective index and the mode profile of waveguide.

- [x] [vertical-taper](MODE/vertical-taper): Calcuates the effective index of vertical tapers over the propagation distance.

- [ ] [edge-coupler](FDTD/edge-coupler): Calculates the overlap integral between a fiber mode (Gaussian) and a waveguide.

- [ ] [directional-coupler](directional-coupler): Calculates the effective index of the supermodes and plots the coupling as a function of length.

- [ ] [disk-waveguide](disk-waveguide): Calculates the effective index and mode profiles of the disk waveguide.

- [ ] [waveguide-heater](waveguide-heater): Calculate the propagation loss as a function of the metal heater gap.

## Requirements

You need installed on your operating system the following software

- Lumerical Software

- Python3

- Python IDE Software (i.e. Spyder)

## Installation

Make sure you have Python 3 and the latest version of Lumerical Design Suite installed. Here you can find all information how to integrate Lumerical Python API with your system.

[Session management - Python API &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360041873053) 

## References

1. [Python API overview &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
2. [Scripting Language &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/categories/360001998954-Scripting-Language)
3. [ASCII Diagragm: GitHub - ArthurSonzogni/Diagon: Interactive ASCII art diagram generators. :star2:](https://github.com/ArthurSonzogni/Diagon)
