# Welcome

                                                                +---------------------+                 
                                                        +-------- lumerical-py-scripts------------+     
                                                        |       |    (repository)     |           |     
                                                        |       +---------------------+           |     
                                                        |                                         |     
                                                  +-----v----+                              +-----v----+
                                                  |          |                              |          |
                     +-----------------------------   FDTD   -----+                     +----   MODE   |
                     |                    |       |          |    |                     |   |          |
                     |                    |       +----------+    |                     |   +----------+
            +--------v------+  +----------v---------+   +---------|--------+  +---------v---------+ 
            | butt-coupling |  |waveguide-mode-taper|   |waveguide-straight|  |waveguide-straight | 
            +---------------+  +--------------------+   +------------------+  +-------------------+ 

## Why this Repository?

In this repositoty you will find useful scripts to optimize your workflow and automate your daily design tasks. All you need to do is to modify the files under `user_inputs` in each subdirectory and run the scripts. The repo is splitted into two main simulation branches with multiple subcategories each:

### 1. [FDTD](/FDTD)

    - [waveguide-straight](FDTD/waveguide-straight): Mode profile and transmission simulations for a straight waveguide section.
    
    - [waveguide-mode-taper](FDTD/waveguide-mode-taper): Mode profile and transmission simulations for a tapered waveguide section.

### 2. [MODE Solutions](/MODE)

    - [waveguide-straight](MODE/waveguide-straight): mode profile and effective index calculations.

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
