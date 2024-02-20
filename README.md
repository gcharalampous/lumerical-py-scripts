# Welcome

```
lumerical-py-scripts/
.
├── DEVICE
│   └── pin_modulator
├── FDTD
│   ├── directional-coupler
│   ├── disk-resonator-coupling
│   ├── edge_coupler
│   ├── mmi-couplers
│   ├── ring-resonator-coupler
│   ├── swg_grating
│   ├── vertical_taper
│   ├── waveguide-bend
│   ├── waveguide_crossing
│   ├── waveguide_mode_taper
│   └── waveguide-straight
└── MODE
    ├── awg_star_coupler
    ├── butt_coupling
    ├── directional_coupler
    ├── disk_waveguide
    ├── edge_coupler
    ├── swg_grating
    ├── vertical_taper
    └── waveguide
```

## Why this Repository?

In this repositoty you will find useful scripts to optimize your workflow and automate your daily design tasks. All you need to do is to modify the files under `user_inputs` in each subdirectory and run the scripts. The repo is splitted into three main simulation branches with multiple subcategories each:

### 1. [3D FDTD](/FDTD)

- [ ] [directional-coupler](FDTD/directional-coupler): Calculates the coupling and plots the E-field of an s-bend directional coupler.

- [ ] [disk-resonator-coupler](FDTD/disk-resonator-coupler): Calculates the coupling of a (a) weakly tapered disk resonator.

- [x] [edge-coupler](FDTD/edge_coupler): Calculates the coupling loss between a fiber (Gaussian) mode and a waveguide mode.

- [ ] [mmi-coupler](FDTD/mmi-coupler): Calculates the coupling and plots the E-field image of a (a) 2x2 MMI coupler.

- [x] [swg_grating](FDTD/swg_grating): Calculates the frequency response (T/R) of a sub-waveelength grating.

- [x] [vertical-taper](FDTD/vertical-taper): Calculates the transmission on the upper waveguide.

- [x] [waveguide-bend](FDTD/waveguide-bend): Calculates the bending loss and mode profile. 

- [x] [waveguide-crossing](FDTD/waveguide-crossing): Calculations the transmission and crosstalk of a linear taper waveguide-crossing.

- [x] [waveguide-mode-taper](FDTD/waveguide-mode-taper): Calculates the adiabatic length of the tapered waveguide.

- [x] [waveguide-straight](FDTD/waveguide-straight): Mode profile and transmission simulations for a straight waveguide.

- [ ] [ring-resonator-coupler](FDTD/ring-resonator-coupler): Calculates the coupling of a (a) rectangular, (b) concentric, and (c) straight sections ring.

### 2. [MODE Solutions](/MODE)

- [x] [butt-coupling](MODE/butt_coupling): Calculates the overlap integral between two waveguides.

- [x] [directional-coupler](MODE/directional_coupler): Calculates the effective index of the supermodes and plots the coupling as a function of length.

- [x] [disk-waveguide](MODE/disk_waveguide): Calculates the effective index and mode profiles of the disk waveguide.

- [x] [edge-coupler](MODE/edge_coupler): Calculates the overlap integral between a fiber mode (Gaussian) and a waveguide.

- [x] [swg_grating](MODE/swg_grating): Calculates the frequency response (T/R) of a sub-waveelength grating (2.5D var FDTD).

- [x] [vertical-taper](MODE/vertical_taper): Calculates the effective index of vertical tapers over the propagation distance.

- [x] [waveguide](MODE/waveguide): Calculates the effective index, propagation loss, FSR and Q-factor. Metal and doping layers included.

### 3. [DEVICE](/DEVICE)

- [x] [pin-modulator](DEVICE/pin_modulator): Calculates the electrical parameters for the pin junction and extracts data for waveguide mode simulations.

## Requirements

You need installed on your operating system the following software

- Lumerical Software

- Python3

- Python Packages in [requirements.txt](requirements.txt) (Numpy, Matplotlib, Shapely, etc)

- Python IDE Software (i.e. Spyder)


## Installation

Make sure you have Python 3 and the latest version of Lumerical Design Suite installed. In this repository, the *lumapi* is assumed integrated into the Python environment. Here you can find all information how to integrate Lumerical Python API with your system.

[Session management - Python API &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360041873053) 

Clone the repository and run the scripts under the project folder. The code will create a Results folder and you can check the saved data there. If Lumerical is installed to a Linux machine remember to change the path `\\` to `/` in [config.py](config.py)



### Spyder (Recommended)

Click on `Tools` -> `PYTHONPATH manager` and then `Add Path`. Add the path to the lumapi like; `C:\\Program Files\\Lumerical\\v222\\api\\python`.

Your lumerical python api directory probably is different than mine.

In addition you need to assign to your `PYTHONPATH manager` the root of the project directory because I am using absolute paths to load the modules. For example, `D:\Georgios\Python - Scripts\lumerical-py-scripts`

### Visual Studio Code

In VScode you can add the following lines in the .json settings if you are coding on a Windows machine.

```
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "C:\\Program Files\\Lumerical\\v222\\api\\python;D:\\Georgios\\Python - Scripts\\lumerical-py-scripts"
    },
    "python.envFile": "${workspaceFolder}/.env"
```

The separator for Window's path is `;` while for Linux path is `:`. The Pythonpath here contains the path of the `lumapi` and the root path of the project.

In addition, you need to create under the root project directory a file called `.env` to add your lumapi path and the directory of the root project. Like,

```
PYTHONPATH=C:\\Program Files\\Lumerical\\v222\\api\\python;D:\\Georgios\\Python-Scripts\\lumerical-py-scripts\\
```

I reccomend running the code with the Jupyter Interactive Python kernel.

### 

## References

1. [Python API overview &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
2. [Scripting Language &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/categories/360001998954-Scripting-Language)
