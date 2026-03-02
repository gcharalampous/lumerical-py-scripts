# Welcome

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Lint](https://github.com/gcharalampous/lumerical-py-scripts/actions/workflows/lint.yml/badge.svg)](https://github.com/gcharalampous/lumerical-py-scripts/actions/workflows/lint.yml)

```
.
├── DEVICE
│   ├── disk_modulator
│   ├── electro_optic
│   ├── pin_modulator
│   └── README.md
├── FDTD
│   ├── adiabatic_directional_coupler
│   ├── adiabatic_y_branch
│   ├── coupled_ring_coupler
│   ├── directional_coupler
│   ├── disk_resonator_coupler
│   ├── edge_coupler
│   ├── grating_coupler_2D
│   ├── grating_coupler_rectangular_3D
│   ├── mmi_couplers
│   ├── README.md
│   ├── ring_resonator_coupler
│   ├── swg_grating
│   ├── vertical_taper
│   ├── waveguide_bend
│   ├── waveguide_crossing
│   ├── waveguide_mode_taper
│   └── waveguide_straight
└── MODE
    ├── awg_star_coupler
    ├── butt_coupling
    ├── directional_coupler
    ├── edge_coupler
    ├── laser_tapered_waveguide
    ├── README.md
    ├── swg_grating
    ├── vertical_taper
    └── waveguide

```
## Quick Navigation

| Solver | Modules | Description |
|--------|---------|-------------|
| [FDTD](FDTD/README.md) | 16 modules | Finite-Difference Time-Domain electromagnetic simulations |
| [MODE](MODE/README.md) | 8 modules | Mode analysis and effective index calculations |
| [DEVICE](DEVICE/README.md) | 3 modules | Carrier transport and optoelectronic simulations |

**Infrastructure:**
- [`project_layout.py`](project_layout.py) — directory management and results paths for all modules
- [`sim_registry.py`](sim_registry.py) — central typed registry of all 27 simulation specs

## Why this Repository?

In this repository, you will find useful scripts to optimize your workflow and automate your daily design tasks. All you need to do is modify the .py files under `user_inputs` in each subdirectory and run the scripts. The results will be shown on the Python interactive terminal and stored under a `Result` directory that will be created after you run the scripts. The repository is divided into three main simulation branches with multiple subcategories each:


## Requirements

You need installed on your operating system the following software

- Lumerical Software

- Python 3.8+

- Python Packages in [requirements.txt](requirements.txt) (Numpy, Matplotlib, Shapely, etc)

- Python IDE Software (i.e. Spyder)


## Installation

Make sure you have Python 3 and the latest version of Lumerical Design Suite installed. In this repository, it is assumed that *lumapi* is integrated into the Python environment. Check the instructions below for Spyder and VSC.

Clone the repository and run the scripts under the root project folder. The code will create a Results folder, and you can check the saved data there. The code is cross-platform compatible and handles path separators automatically.



### Spyder (Recommended)

1. Click on `Tools` -> `PYTHONPATH manager` and then `Add Path`.
2. Add the path to the lumapi. Your Lumerical Python API directory path depends on your installed version, for example: `C:\Program Files\Lumerical\vXXX\api\python` where `XXX` is your Lumerical version number. Check your Lumerical installation directory to find the correct version.

3. Additionally, assign the root of the project directory to your `PYTHONPATH manager` since absolute paths are used to load the modules. For example: `D:\Georgios\Python-Scripts\lumerical-py-scripts`

### Visual Studio Code

If you're coding on a Windows machine, you can create a file called `.env` under the root project directory to add your lumapi path and the working directory of the root project. For example:

``` mathematica
PYTHONPATH=C:\Program Files\Lumerical\vXXX\api\python;D:\Georgios\Python-Scripts\lumerical-py-scripts\
```
Make sure the `.env` file is loaded after restarting VSCode.

Ensure that you run the code with the Jupyter Interactive Python kernel to view the plots in the interactive terminal. In VSCode, you may need to restart the Python kernel each time you update one of the imported library files. The code is cross-platform compatible and works on both Windows and Linux machines.

## To-Do List
See the full [To-Do List](TODO.md) for upcoming tasks and features.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions, code conventions, and how to add new simulation modules.

## References

1. [Python API overview &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
2. [Scripting Language &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/categories/360001998954-Scripting-Language)
