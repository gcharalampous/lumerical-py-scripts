# Welcome

```
lumerical-py-scripts/

├── DEVICE
│   ├── electro_optic
│   └── pin_modulator
├── FDTD
│   ├── directional-coupler
│   ├── disk_resonator_coupler
│   ├── edge_coupler
│   ├── grating_coupler_2D
│   ├── mmi-couplers
│   ├── ring_resonator_coupler
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
    ├── edge_coupler
    ├── swg_grating
    ├── vertical_taper
    └── waveguide
```

## Why this Repository?

In this repository, you will find useful scripts to optimize your workflow and automate your daily design tasks. All you need to do is modify the .py files under `user_inputs` in each subdirectory and run the scripts. The results will be shown on the interactive terminal and stored under a `Result` directory that will be created after you run the scripts. The repository is divided into three main simulation branches with multiple subcategories each:


## Requirements

You need installed on your operating system the following software

- Lumerical Software

- Python3

- Python Packages in [requirements.txt](requirements.txt) (Numpy, Matplotlib, Shapely, etc)

- Python IDE Software (i.e. Spyder)


## Installation

Make sure you have Python 3 and the latest version of Lumerical Design Suite installed. In this repository, it is assumed that *lumapi* is integrated into the Python environment. Check the instructions below for Spyder and VSC.

Clone the repository and run the scripts under the root project folder. The code will create a Results folder, and you can check the saved data there. If Lumerical is installed on a Linux machine, remember to change the path `\\` to `/` in [config.py](config.py).



### Spyder (Recommended)

1. Click on `Tools` -> `PYTHONPATH manager` and then `Add Path`.
2. Add the path to the lumapi, for example: `C:\\Program Files\\Lumerical\\v222\\api\\python`.

(Note: Your Lumerical Python API directory may differ from mine.)

3. Additionally, assign the root of the project directory to your `PYTHONPATH manager` since absolute paths are used to load the modules. For example: `D:\Georgios\Python - Scripts\lumerical-py-scripts`

### Visual Studio Code

If you're coding on a Windows machine, you can create a file called `.env` under the root project directory to add your lumapi path and the working directory of the root project. For example:

``` mathematica
PYTHONPATH=C:\\Program Files\\Lumerical\\v222\\api\\python;D:\\Georgios\\Python-Scripts\\lumerical-py-scripts\\
```

Ensure that you run the code with the Jupyter Interactive Python kernel to view the plots in the interactive terminal. In VSCode, you may need to restart the Python kernel each time you update one of the imported library files.

## References

1. [Python API overview &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
2. [Scripting Language &ndash; Ansys Optics](https://optics.ansys.com/hc/en-us/categories/360001998954-Scripting-Language)
