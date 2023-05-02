## 2D Butt-Coupling Simulations (MODE Solutions)

    MODE/butt_coupling/
    ├── fde_region.py
    ├── mode_profile
    │   └── mode_profile_2D.py
    ├── overlap_mode
    │   └── overlap_mode_integral_2D.py
    ├── overlap_profile_sweep
    │   ├── overlap_misalignment_integral_2D.py
    │   └── overlap_width_sweep_2D.py
    ├── README.md
    └── user_inputs
        ├── lumerical_files
        │   ├── waveguide_1.lms
        │   └── waveguide_2.lms
        ├── user_simulation_parameters.py
        └── user_sweep_parameters.py

### Quick Simulation Setup

1. After downloading the repository, navigate through the `butt_coupling/user_inputs/` directory.
2. Edit the two lumerical files `waveguide_1.lms`and `waveguide_2.lms` to define the waveguide properties including the materials and dimensions. 
3. Edit the `user_inputs/user_simulation_parameters.py` to define the simulation properties like the number of modes, and the mode order to overlap.
4. Then define in  `user_inputs/user_sweep_parameters.py` the sweep parameters including the width of `waveguide_2.lms` and the misalignment axis.
5. Run the `mode_profile/mode_profile_2D.py` to get the modes of each waveguide. 
6. Run the `overlap_mode/overlap_mode_integral_2D.py`to calculate the overlap integral between the two mode orders you defined in `user_inputs/user_simulation_parameters.py`.
7. Running the `overlap_profile_sweep/overlap_misalignment_integral_2D.py`or `overlap_profile_sweep/overlap_width_sweep_2D.py` you can sweep over the misalignment axis or the width dimensions of the second waveguide, respectively

WARNING: The FDE properties from the two lumerical files `waveguide_1.lms`and `waveguide_2.lms`will be overwritten based on the variables defined in`user_inputs/user_simulation_parameters.py`. This is to make sure, that the overlap integral will be estimated based on the same mesh.



### Proposed Workflow

1. Edit the two lumerical files. For example, `waveguide_1.lms` can be the laser waveguide while the `waveguide_2.lms` can be the passive waveguide.

2. In `user_inputs/user_simulation_parameters.py` define the number of modes you will need to investigate. Typically `num_modes = 6` are enough. 

3. Run the `mode_profile/mode_profile_2D.py` to retrieve the 6 modes from each waveguide template file. The script will also store the simulation profiles to an .ldf file which will load later on.

4. From step (3) you get important information like the polarization for each mode order. Go to `user_inputs/user_simulation_parameters.py` and define the order for each lumerical file  like `m_waveguide1=2` and  `m_waveguide2=1`.

5. Running `overlap_mode/overlap_mode_integral_2D.py` will calculate the overlap integral based on the dimensions you set in the template files and for the mode orders you defined in step (4).

6. If everything runs as expected on step (5), you can calculate the missalginemt across the horizontal and vertical axis of the butt-coupling scheme based on the mode-orders you defined in step (4). Run the `overlap_profile_sweep/overlap_misalignment_integral_2D.py`. The variables for the misalignment axis are defined in the `user_inputs/user_sweep_parameters.py`.

7. Running the `overlap_width_sweep_2D.py` script will take the `m_waveguide1=2` and determine if it is a TE or TM mode. If `m_waveguide1=2` is a TE mode, will sweep the width of the `waveguide_2.lms` and track the fundamental TE mode. Likewise for the TM mode. 
