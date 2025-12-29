import os



# Get the Project Root Directory
PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))


# --------------------------------3D FDTD ---------------------------------

#PACKAGE DIRECTORIES

# Adiabatic Directional FDTD
FDTD_ADIAB_DC_FILENAME = "sbend_adiabatic_directional_coupler.fsp"
FDTD_ADIAB_DC_PATH_READ = "FDTD\\adiabatic_directional_coupler\\user_inputs\\lumerical_files"
FDTD_ADIAB_DC_PATH_WRITE_FIGURES = "FDTD\\Results\\adiabatic_directional_coupler\\Figures"
FDTD_ADIAB_DC_PATH_WRITE_LUMERICAL = "FDTD\\Results\\adiabatic_directional_coupler\\lumerical_files"

FDTD_ADIAB_DC_PATH_WRITE_DATA = ["Sweep Transmission", "Frequency Response","E-fields"]
FDTD_ADIAB_DC_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_ADIAB_DC_PATH_READ,FDTD_ADIAB_DC_FILENAME)
FDTD_ADIAB_DC_DIRECTORY_WRITE = [str]*len(FDTD_ADIAB_DC_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_ADIAB_DC_PATH_WRITE_DATA):
    FDTD_ADIAB_DC_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_ADIAB_DC_PATH_WRITE_FIGURES,FDTD_ADIAB_DC_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_ADIAB_DC_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_ADIAB_DC_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_ADIAB_DC_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_ADIAB_DC_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_ADIAB_DC_DIRECTORY_WRITE[i] + "\n already exists!")
        break


FDTD_ADIAB_DC_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, FDTD_ADIAB_DC_PATH_WRITE_LUMERICAL)
if not os.path.exists(FDTD_ADIAB_DC_DIRECTORY_WRITE_FILE):
    os.makedirs(FDTD_ADIAB_DC_DIRECTORY_WRITE_FILE)
    #print("Directory:" + FDTD_ADIAB_DC_DIRECTORY_WRITE[i] + "\n created successfully!")







# Adiabatic Y-Branch FDTD
FDTD_ADIAB_Y_BR_FILENAME = "adiabatic_y_branch.fsp"
FDTD_ADIAB_Y_BR_PATH_READ = "FDTD\\adiabatic_y_branch\\user_inputs\\lumerical_files"
FDTD_ADIAB_Y_BR_PATH_WRITE_FIGURES = "FDTD\\Results\\adiabatic_y_branch\\Figures"
FDTD_ADIAB_Y_BR_PATH_WRITE_LUMERICAL = "FDTD\\Results\\adiabatic_y_branch\\lumerical_files"

FDTD_ADIAB_Y_BR_PATH_WRITE_DATA = ["Sweep Transmission", "Frequency Response","E-fields"]
FDTD_ADIAB_Y_BR_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_ADIAB_Y_BR_PATH_READ,FDTD_ADIAB_Y_BR_FILENAME)
FDTD_ADIAB_Y_BR_DIRECTORY_WRITE = [str]*len(FDTD_ADIAB_Y_BR_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_ADIAB_Y_BR_PATH_WRITE_DATA):
    FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_ADIAB_Y_BR_PATH_WRITE_FIGURES,FDTD_ADIAB_Y_BR_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_ADIAB_Y_BR_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[i] + "\n already exists!")
        break


FDTD_ADIAB_Y_BR_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, FDTD_ADIAB_Y_BR_PATH_WRITE_LUMERICAL)
if not os.path.exists(FDTD_ADIAB_Y_BR_DIRECTORY_WRITE_FILE):
    os.makedirs(FDTD_ADIAB_Y_BR_DIRECTORY_WRITE_FILE)
    #print("Directory:" + FDTD_ADIAB_Y_BR_DIRECTORY_WRITE[i] + "\n created successfully!")






# Disk Coupler FDTD
FDTD_DISK_FILENAME = ["straight_disk_coupling_section.fsp","coocentric_disk_coupling_section.fsp","rectangular_disk_coupling_section.fsp"]
FDTD_DISK_PATH_READ = "FDTD\\disk_resonator_coupler\\user_inputs\\lumerical_files"
FDTD_DISK_PATH_WRITE_FIGURES = "FDTD\\Results\\disk_resonator_coupler\\Figures"
FDTD_DISK_PATH_WRITE_DATA = ["Index Profile", "Frequency Response","E-fields", "Coupling"]
#FDTD_DISK_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_DISK_PATH_READ,FDTD_DISK_FILENAME[0])
FDTD_DISK_DIRECTORY_WRITE = [str]*len(FDTD_DISK_PATH_WRITE_DATA)
FDTD_DISK_DIRECTORY_READ = [str]*len(FDTD_DISK_FILENAME)

for i,data in enumerate(FDTD_DISK_FILENAME):
    FDTD_DISK_DIRECTORY_READ[i] = os.path.join(PACKAGE_DIR,FDTD_DISK_PATH_READ,FDTD_DISK_FILENAME[i])

for i,data in enumerate(FDTD_DISK_PATH_WRITE_DATA):
    FDTD_DISK_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_DISK_PATH_WRITE_FIGURES,FDTD_DISK_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_DISK_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_DISK_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_DISK_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n already exists!")
        break


# Ring Coupler FDTD
FDTD_RING_FILENAME = ["straight_ring_coupling_section.fsp","coocentric_ring_coupling_section.fsp","rectangular_ring_coupling_section"]
FDTD_RING_PATH_READ = "FDTD\\ring_resonator_coupler\\user_inputs\\lumerical_files"
FDTD_RING_PATH_WRITE_FIGURES = "FDTD\\Results\\ring_resonator_coupler\\Figures"
FDTD_RING_PATH_WRITE_DATA = ["Index Profile", "Frequency Response","E-fields", "Coupling"]
#FDTD_RING_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_RING_PATH_READ,FDTD_RING_FILENAME[0])
FDTD_RING_DIRECTORY_WRITE = [str]*len(FDTD_RING_PATH_WRITE_DATA)
FDTD_RING_DIRECTORY_READ = [str]*len(FDTD_RING_FILENAME)

for i,data in enumerate(FDTD_RING_FILENAME):
    FDTD_RING_DIRECTORY_READ[i] = os.path.join(PACKAGE_DIR,FDTD_RING_PATH_READ,FDTD_RING_FILENAME[i])

for i,data in enumerate(FDTD_RING_PATH_WRITE_DATA):
    FDTD_RING_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_RING_PATH_WRITE_FIGURES,FDTD_RING_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_RING_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_RING_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_RING_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n already exists!")
        break







# WAVEGUIDE CROSSING FDTD
FDTD_CROSS_FILENAME = ["waveguide_crossing_multi_wg_taper.fsp"]
FDTD_CROSS_PATH_READ = "FDTD\\waveguide_crossing\\user_inputs\\lumerical_files"
FDTD_CROSS_PATH_WRITE_FIGURES = "FDTD\\Results\\waveguide_crossing\\Figures"
FDTD_CROSS_PATH_WRITE_DATA = ["Index Profile", "Frequency Response","E-fields"]
FDTD_CROSS_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_CROSS_PATH_READ,FDTD_CROSS_FILENAME[0])
FDTD_CROSS_DIRECTORY_WRITE = [str]*len(FDTD_CROSS_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_CROSS_PATH_WRITE_DATA):
    FDTD_CROSS_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_CROSS_PATH_WRITE_FIGURES,FDTD_CROSS_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_CROSS_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_CROSS_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_CROSS_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n already exists!")
        break





# EDGE COUPLER FDTD
FDTD_EDGE_FILENAME = ["edge_taper.fsp"]
FDTD_EDGE_PATH_READ = "FDTD\\edge_coupler\\user_inputs\\lumerical_files"
FDTD_EDGE_PATH_WRITE_FIGURES = "FDTD\\Results\\edge_coupler\\Figures"
FDTD_EDGE_PATH_WRITE_DATA = ["Index Profile", "Frequency Response","E-fields", "Coupling"]
FDTD_EDGE_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_EDGE_PATH_READ,FDTD_EDGE_FILENAME[0])
FDTD_EDGE_DIRECTORY_WRITE = [str]*len(FDTD_EDGE_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_EDGE_PATH_WRITE_DATA):
    FDTD_EDGE_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_EDGE_PATH_WRITE_FIGURES,FDTD_EDGE_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_EDGE_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_EDGE_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_EDGE_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_EDGE_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_EDGE_DIRECTORY_WRITE[i] + "\n already exists!")
        break


# GRATING COUPLER 2D FDTD
FDTD_GRATING_COUPLER_2D_FILENAME = ["grating_coupler_2D.fsp"]
FDTD_GRATING_COUPLER_2D_PATH_READ = "FDTD\\grating_coupler_2D\\user_inputs\\lumerical_files"
FDTD_GRATING_COUPLER_2D_PATH_WRITE_FIGURES = "FDTD\\Results\\grating_coupler_2D\\Figures"
FDTD_GRATING_COUPLER_2D_PATH_WRITE_DATA = ["Index Profile", "Frequency Response","E-fields", 'Sweeps']
FDTD_GRATING_COUPLER_2D_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_GRATING_COUPLER_2D_PATH_READ,FDTD_GRATING_COUPLER_2D_FILENAME[0])
FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE = [str]*len(FDTD_GRATING_COUPLER_2D_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_GRATING_COUPLER_2D_PATH_WRITE_DATA):
    FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_GRATING_COUPLER_2D_PATH_WRITE_FIGURES,FDTD_GRATING_COUPLER_2D_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_GRATING_COUPLER_2D_DIRECTORY_WRITE[i] + "\n already exists!")
        break






# SWG FDTD
FDTD_SWG_FILENAME = ["sub_wavelength_grating_layer_1.fsp","sub_wavelength_grating_layer_2.fsp"]
FDTD_SWG_PATH_READ = "FDTD\\swg_grating\\user_inputs\\lumerical_files"
FDTD_SWG_PATH_WRITE_FIGURES = "FDTD\\Results\\swg_grating\\Figures"
FDTD_SWG_PATH_WRITE_DATA = ["Index Profile", "Frequency Response","E-fields"]
FDTD_SWG_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_SWG_PATH_READ,FDTD_SWG_FILENAME[0])
FDTD_SWG_DIRECTORY_WRITE = [str]*len(FDTD_SWG_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_SWG_PATH_WRITE_DATA):
    FDTD_SWG_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_SWG_PATH_WRITE_FIGURES,FDTD_SWG_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_SWG_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_SWG_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_SWG_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n already exists!")
        break

# VERTICAL TAPER FDTD
FDTD_VERTICAL_FILENAME = ["vertical_taper.fsp"]
FDTD_VERTICAL_PATH_READ = "FDTD\\vertical_taper\\user_inputs\\lumerical_files"
FDTD_VERTICAL_PATH_WRITE_FIGURES = "FDTD\\Results\\vertical_taper\\Figures"
FDTD_VERTICAL_PATH_WRITE_DATA = ["Index Profile", "Frequency Response","E-fields"]
FDTD_VERTICAL_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_VERTICAL_PATH_READ,FDTD_VERTICAL_FILENAME[0])
FDTD_VERTICAL_DIRECTORY_WRITE = [str]*len(FDTD_VERTICAL_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_VERTICAL_PATH_WRITE_DATA):
    FDTD_VERTICAL_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_VERTICAL_PATH_WRITE_FIGURES,FDTD_VERTICAL_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_VERTICAL_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_VERTICAL_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_VERTICAL_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_VERTICAL_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_VERTICAL_DIRECTORY_WRITE[i] + "\n already exists!")
        break


# WAVEGUIDE TAPER LASER
FDTD_LASER_TAPERED_FILENAME = ["laser_mesa_waveguide_tapered.fsp"]
FDTD_LASER_TAPERED_PATH_READ = "FDTD\\laser_tapered_waveguide\\user_inputs\\lumerical_files"
FDTD_LASER_TAPERED_PATH_WRITE_FIGURES = "FDTD\\Results\\laser_mesa_waveguide_tapered\\Figures"
FDTD_LASER_TAPERED_PATH_WRITE_DATA = ["Index Profile", "Frequency Response","E-fields"]
FDTD_LASER_TAPERED_PATH_WRITE_LUMERICAL = "FDTD\\Results\\laser_mesa_waveguide_tapered\\lumerical_files"
FDTD_LASER_TAPERED_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_LASER_TAPERED_PATH_READ,FDTD_LASER_TAPERED_FILENAME[0])
FDTD_LASER_TAPERED_DIRECTORY_WRITE = [str]*len(FDTD_LASER_TAPERED_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_LASER_TAPERED_PATH_WRITE_DATA):
    FDTD_LASER_TAPERED_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_LASER_TAPERED_PATH_WRITE_FIGURES,FDTD_LASER_TAPERED_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_LASER_TAPERED_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_LASER_TAPERED_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_LASER_TAPERED_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_LASER_TAPERED_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_LASER_TAPERED_DIRECTORY_WRITE[i] + "\n already exists!")
        break

FDTD_LASER_TAPERED_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, FDTD_LASER_TAPERED_PATH_WRITE_LUMERICAL)
if not os.path.exists(FDTD_LASER_TAPERED_DIRECTORY_WRITE_FILE):
    os.makedirs(FDTD_LASER_TAPERED_DIRECTORY_WRITE_FILE)
    #print("Directory:" + FDTD_LASER_TAPERED_DIRECTORY_WRITE_FILE[i] + "\n created successfully!")




# MMI Couplers FDTD
FDTD_MMI_FILENAME = ["MMI_1x2.fsp","MMI_2x2.fsp"]
FDTD_MMI_PATH_READ = ["FDTD\\mmi_couplers\\1x2\\user_inputs\\lumerical_files","FDTD\\mmi_couplers\\2x2\\user_inputs\\lumerical_files"]
FDTD_MMI_PATH_WRITE_FIGURES = "FDTD\\Results\\mmi_couplers\\Figures"
FDTD_MMI_PATH_WRITE_LUMERICAL = "FDTD\\Results\\mmi_couplers\\lumerical_files"

FDTD_MMI_PATH_WRITE_DATA = ["Sweep Transmission", "Frequency Response","E-fields"]
FDTD_MMI_DIRECTORY_READ = [os.path.join(PACKAGE_DIR, path, filename) for path, filename in zip(FDTD_MMI_PATH_READ, FDTD_MMI_FILENAME)]
FDTD_MMI_DIRECTORY_WRITE = [str]*len(FDTD_MMI_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_MMI_PATH_WRITE_DATA):
    FDTD_MMI_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_MMI_PATH_WRITE_FIGURES,FDTD_MMI_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_MMI_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_MMI_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_MMI_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_MMI_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_MMI_DIRECTORY_WRITE[i] + "\n already exists!")
        break


FDTD_MMI_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, FDTD_MMI_PATH_WRITE_LUMERICAL)
if not os.path.exists(FDTD_MMI_DIRECTORY_WRITE_FILE):
    os.makedirs(FDTD_MMI_DIRECTORY_WRITE_FILE)
    #print("Directory:" + FDTD_MMI_DIRECTORY_WRITE[i] + "\n created successfully!")






# WAVEGUIDE MODE TAPER FDTD
FDTD_WGTAPER_FILENAME = "waveguide_mode_taper.fsp"
FDTD_WGTAPER_PATH_READ = "FDTD\\waveguide_mode_taper\\user_inputs\\lumerical_files"
FDTD_WGTAPER_PATH_WRITE_FIGURES = "FDTD\\Results\\waveguide_mode_taper\\Figures"
FDTD_WGTAPER_PATH_WRITE_LUMERICAL = "FDTD\\Results\\waveguide_mode_taper\\lumerical_files"

FDTD_WGTAPER_PATH_WRITE_DATA = ["Sweep Transmission", "Frequency Response","E-fields"]
FDTD_WGTAPER_DIRECTORY_READ = os.path.join(PACKAGE_DIR,FDTD_WGTAPER_PATH_READ,FDTD_WGTAPER_FILENAME[0])
FDTD_WGTAPER_DIRECTORY_WRITE = [str]*len(FDTD_WGTAPER_PATH_WRITE_DATA)
for i,data in enumerate(FDTD_WGTAPER_PATH_WRITE_DATA):
    FDTD_WGTAPER_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,FDTD_WGTAPER_PATH_WRITE_FIGURES,FDTD_WGTAPER_PATH_WRITE_DATA[i])
for i in range(0,len(FDTD_WGTAPER_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(FDTD_WGTAPER_DIRECTORY_WRITE[i]):
        os.makedirs(FDTD_WGTAPER_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_WGTAPER_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_WGTAPER_DIRECTORY_WRITE[i] + "\n already exists!")
        break


FDTD_WGTAPER_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, FDTD_WGTAPER_PATH_WRITE_LUMERICAL)
if not os.path.exists(FDTD_WGTAPER_DIRECTORY_WRITE_FILE):
    os.makedirs(FDTD_WGTAPER_DIRECTORY_WRITE_FILE)
    #print("Directory:" + FDTD_WGTAPER_DIRECTORY_WRITE[i] + "\n created successfully!")






# --------------------------------MODE SOLUTIONS---------------------------------
    
# AWG STAR COUPLER FIELD MODE
MODE_AWG_FILENAME = ["awg_input_taper.lms"]
MODE_AWG_PATH_READ = "MODE\\awg_star_coupler\\user_inputs\\lumerical_files"
MODE_AWG_PATH_WRITE_FIGURES = "MODE\\Results\\awg_star_coupler\\Figures"
MODE_AWG_PATH_WRITE_DATA = ["Index Profile", "Far Field"]
MODE_AWG_DIRECTORY_READ = os.path.join(PACKAGE_DIR,MODE_AWG_PATH_READ,MODE_AWG_FILENAME[0])
MODE_AWG_DIRECTORY_WRITE = [str]*len(MODE_AWG_PATH_WRITE_DATA)
for i,data in enumerate(MODE_AWG_PATH_WRITE_DATA):
    MODE_AWG_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,MODE_AWG_PATH_WRITE_FIGURES,MODE_AWG_PATH_WRITE_DATA[i])
for i in range(0,len(MODE_AWG_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(MODE_AWG_DIRECTORY_WRITE[i]):
        os.makedirs(MODE_AWG_DIRECTORY_WRITE[i])
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n already exists!")
        break



# WAVEGUIDE TAPER LASER
MODE_LASER_TAPERED_FILENAME = ["laser_taper_waveguide.lms"]
MODE_LASER_TAPERED_PATH_READ = "MODE\\laser_tapered_waveguide\\user_inputs\\lumerical_files"
MODE_LASER_TAPERED_PATH_WRITE_FIGURES = "MODE\\Results\\laser_taper_waveguide\\Figures"
MODE_LASER_TAPERED_PATH_WRITE_DATA = ["Mode Profile"]
MODE_LASER_TAPERED_PATH_WRITE_LUMERICAL = "MODE\\Results\\laser_taper_waveguide\\lumerical_files"
MODE_LASER_TAPERED_DIRECTORY_READ = os.path.join(PACKAGE_DIR,MODE_LASER_TAPERED_PATH_READ,MODE_LASER_TAPERED_FILENAME[0])
MODE_LASER_TAPERED_DIRECTORY_WRITE = [str]*len(MODE_LASER_TAPERED_PATH_WRITE_DATA)
for i,data in enumerate(MODE_LASER_TAPERED_PATH_WRITE_DATA):
    MODE_LASER_TAPERED_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,MODE_LASER_TAPERED_PATH_WRITE_FIGURES,MODE_LASER_TAPERED_PATH_WRITE_DATA[i])
for i in range(0,len(MODE_LASER_TAPERED_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(MODE_LASER_TAPERED_DIRECTORY_WRITE[i]):
        os.makedirs(MODE_LASER_TAPERED_DIRECTORY_WRITE[i])
        #print("Directory:" + MODE_LASER_TAPERED_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + MODE_LASER_TAPERED_DIRECTORY_WRITE[i] + "\n already exists!")
        break

MODE_LASER_TAPERED_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, MODE_LASER_TAPERED_PATH_WRITE_LUMERICAL)
if not os.path.exists(MODE_LASER_TAPERED_DIRECTORY_WRITE_FILE):
    os.makedirs(MODE_LASER_TAPERED_DIRECTORY_WRITE_FILE)
    #print("Directory:" + MODE_LASER_TAPERED_DIRECTORY_WRITE_FILE[i] + "\n created successfully!")






# WAVEGUIDE MODE DIRECTIONAL COUPLER
MODE_DC_FILENAME = ["waveguide_coupler.lms"]
MODE_DC_PATH_READ = "MODE\\directional_coupler\\user_inputs\\lumerical_files"
MODE_DC_PATH_WRITE_FIGURES = "MODE\\Results\\waveguide_coupler\\Figures"
MODE_DC_PATH_WRITE_DATA = ["Mode Profile", "Gap Sweep", "Length Sweep"]
MODE_DC_PATH_WRITE_LUMERICAL = "MODE\\Results\\waveguide_coupler\\lumerical_files"
MODE_DC_DIRECTORY_READ = os.path.join(PACKAGE_DIR,MODE_DC_PATH_READ,MODE_DC_FILENAME[0])
MODE_DC_DIRECTORY_WRITE = [str]*len(MODE_DC_PATH_WRITE_DATA)
for i,data in enumerate(MODE_DC_PATH_WRITE_DATA):
    MODE_DC_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,MODE_DC_PATH_WRITE_FIGURES,MODE_DC_PATH_WRITE_DATA[i])
for i in range(0,len(MODE_DC_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(MODE_DC_DIRECTORY_WRITE[i]):
        os.makedirs(MODE_DC_DIRECTORY_WRITE[i])
        #print("Directory:" + MODE_DC_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + MODE_DC_DIRECTORY_WRITE[i] + "\n already exists!")
        break

MODE_DC_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, MODE_DC_PATH_WRITE_LUMERICAL)
if not os.path.exists(MODE_DC_DIRECTORY_WRITE_FILE):
    os.makedirs(MODE_DC_DIRECTORY_WRITE_FILE)
    #print("Directory:" + MODE_DC_DIRECTORY_WRITE_FILE[i] + "\n created successfully!")


# WAVEGUIDE MODE
MODE_WAVEGUIDE_PATH_WRITE_FIGURES = "MODE\\Results\\waveguide\\Figures"
MODE_WAVEGUIDE_PATH_WRITE_DATA = ["Index Profile", "Mode Profile","Neff","PIN Offset", "Bending Loss"]
MODE_WAVEGUIDE_DIRECTORY_WRITE = [str]*len(MODE_WAVEGUIDE_PATH_WRITE_DATA)
MODE_WAVEGUIDE_PATH_WRITE_LUMERICAL = "MODE\\Results\\waveguide\\lumerical_files"

for i,data in enumerate(MODE_WAVEGUIDE_PATH_WRITE_DATA):
    MODE_WAVEGUIDE_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,MODE_WAVEGUIDE_PATH_WRITE_FIGURES,MODE_WAVEGUIDE_PATH_WRITE_DATA[i])
for i in range(0,len(MODE_WAVEGUIDE_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(MODE_WAVEGUIDE_DIRECTORY_WRITE[i]):
        os.makedirs(MODE_WAVEGUIDE_DIRECTORY_WRITE[i])
        #print("Directory:" + MODE_WAVEGUIDE_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + MODE_WAVEGUIDE_DIRECTORY_WRITE[i] + "\n already exists!")
        break

MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, MODE_WAVEGUIDE_PATH_WRITE_LUMERICAL)
if not os.path.exists(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE):
    os.makedirs(MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE)
    #print("Directory:" + MODE_WAVEGUIDE_DIRECTORY_WRITE_FILE[i] + "\n created successfully!")



# SWG MODE
MODE_SWG_FILENAME = ["sub_wavelength_grating_layer_1.fsp","sub_wavelength_grating_layer_2.fsp"]
MODE_SWG_PATH_READ = "MODE\\swg_grating\\user_inputs\\lumerical_files"
MODE_SWG_PATH_WRITE_FIGURES = "MODE\\Results\\swg_grating\\Figures"
MODE_SWG_PATH_WRITE_DATA = ["Index Profile", "Frequency Response","E-fields"]
MODE_SWG_DIRECTORY_READ = os.path.join(PACKAGE_DIR,MODE_SWG_PATH_READ,MODE_SWG_FILENAME[0])
MODE_SWG_DIRECTORY_WRITE = [str]*len(MODE_SWG_PATH_WRITE_DATA)
for i,data in enumerate(MODE_SWG_PATH_WRITE_DATA):
    MODE_SWG_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,MODE_SWG_PATH_WRITE_FIGURES,MODE_SWG_PATH_WRITE_DATA[i])
for i in range(0,len(MODE_SWG_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(MODE_SWG_DIRECTORY_WRITE[i]):
        os.makedirs(MODE_SWG_DIRECTORY_WRITE[i])
        #print("Directory:" + MODE_SWG_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + MODE_SWG_DIRECTORY_WRITE[i] + "\n already exists!")
        break



# ------------------------------------ DEVICE -----------------------------------------

# PN Disk MODULATOR
PN_DISK_MODULATOR_PATH_WRITE_FIGURES = "DEVICE\\Results\\pn_disk_modulator\\Figures"
PN_DISK_MODULATOR_PATH_WRITE_DATA = ["Charge Profile", "DC Sweep","AC Sweep"]
PN_DISK_MODULATOR_DIRECTORY_WRITE = [str]*len(PN_DISK_MODULATOR_PATH_WRITE_DATA)
PN_DISK_MODULATOR_PATH_WRITE_LUMERICAL = "DEVICE\\Results\\pn_disk_modulator\\lumerical_files"

for i,data in enumerate(PN_DISK_MODULATOR_PATH_WRITE_DATA):
    PN_DISK_MODULATOR_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,PN_DISK_MODULATOR_PATH_WRITE_FIGURES,PN_DISK_MODULATOR_PATH_WRITE_DATA[i])
for i in range(0,len(PN_DISK_MODULATOR_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(PN_DISK_MODULATOR_DIRECTORY_WRITE[i]):
        os.makedirs(PN_DISK_MODULATOR_DIRECTORY_WRITE[i])
        #print("Directory:" + PN_DISK_MODULATOR_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + PN_DISK_MODULATOR_DIRECTORY_WRITE[i] + "\n already exists!")
        break

PN_DISK_MODULATOR_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, PN_DISK_MODULATOR_PATH_WRITE_LUMERICAL)
if not os.path.exists(PN_DISK_MODULATOR_DIRECTORY_WRITE_FILE):
    os.makedirs(PN_DISK_MODULATOR_DIRECTORY_WRITE_FILE)
    #print("Directory:" + PN_DISK_MODULATOR_DIRECTORY_WRITE_FILE[i] + "\n created successfully!")





# PN MODULATOR
PN_MODULATOR_PATH_WRITE_FIGURES = "DEVICE\\Results\\pn_modulator\\Figures"
PN_MODULATOR_PATH_WRITE_DATA = ["Charge Profile", "DC Sweep","AC Sweep"]
PN_MODULATOR_DIRECTORY_WRITE = [str]*len(PN_MODULATOR_PATH_WRITE_DATA)
PN_MODULATOR_PATH_WRITE_LUMERICAL = "DEVICE\\Results\\pn_modulator\\lumerical_files"

for i,data in enumerate(PN_MODULATOR_PATH_WRITE_DATA):
    PN_MODULATOR_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,PN_MODULATOR_PATH_WRITE_FIGURES,PN_MODULATOR_PATH_WRITE_DATA[i])
for i in range(0,len(PN_MODULATOR_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(PN_MODULATOR_DIRECTORY_WRITE[i]):
        os.makedirs(PN_MODULATOR_DIRECTORY_WRITE[i])
        #print("Directory:" + PN_MODULATOR_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + PN_MODULATOR_DIRECTORY_WRITE[i] + "\n already exists!")
        break

PN_MODULATOR_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, PN_MODULATOR_PATH_WRITE_LUMERICAL)
if not os.path.exists(PN_MODULATOR_DIRECTORY_WRITE_FILE):
    os.makedirs(PN_MODULATOR_DIRECTORY_WRITE_FILE)
    #print("Directory:" + PN_MODULATOR_DIRECTORY_WRITE_FILE[i] + "\n created successfully!")






# PIN MODULATOR
PIN_MODULATOR_PATH_WRITE_FIGURES = "DEVICE\\Results\\pin_modulator\\Figures"
PIN_MODULATOR_PATH_WRITE_DATA = ["Charge Profile", "DC Sweep","AC Sweep"]
PIN_MODULATOR_DIRECTORY_WRITE = [str]*len(PIN_MODULATOR_PATH_WRITE_DATA)
PIN_MODULATOR_PATH_WRITE_LUMERICAL = "DEVICE\\Results\\pin_modulator\\lumerical_files"

for i,data in enumerate(PIN_MODULATOR_PATH_WRITE_DATA):
    PIN_MODULATOR_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,PIN_MODULATOR_PATH_WRITE_FIGURES,PIN_MODULATOR_PATH_WRITE_DATA[i])
for i in range(0,len(PIN_MODULATOR_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(PIN_MODULATOR_DIRECTORY_WRITE[i]):
        os.makedirs(PIN_MODULATOR_DIRECTORY_WRITE[i])
        #print("Directory:" + PIN_MODULATOR_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + PIN_MODULATOR_DIRECTORY_WRITE[i] + "\n already exists!")
        break

PIN_MODULATOR_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, PIN_MODULATOR_PATH_WRITE_LUMERICAL)
if not os.path.exists(PIN_MODULATOR_DIRECTORY_WRITE_FILE):
    os.makedirs(PIN_MODULATOR_DIRECTORY_WRITE_FILE)
    #print("Directory:" + PIN_MODULATOR_DIRECTORY_WRITE_FILE[i] + "\n created successfully!")




# ELECTROOPTIC MODULATOR
EO_MODULATOR_PATH_WRITE_FIGURES = "DEVICE\\Results\\eo_modulator\\Figures"
EO_MODULATOR_PATH_WRITE_DATA = ["E-field", "Index Change"]
EO_MODULATOR_DIRECTORY_WRITE = [str]*len(EO_MODULATOR_PATH_WRITE_DATA)
EO_MODULATOR_PATH_WRITE_LUMERICAL = "DEVICE\\Results\\eo_modulator\\lumerical_files"

for i,data in enumerate(EO_MODULATOR_PATH_WRITE_DATA):
    EO_MODULATOR_DIRECTORY_WRITE[i] = os.path.join(PACKAGE_DIR,EO_MODULATOR_PATH_WRITE_FIGURES,EO_MODULATOR_PATH_WRITE_DATA[i])
for i in range(0,len(EO_MODULATOR_DIRECTORY_WRITE)):
    # create the directory if it doesn't exist already
    if not os.path.exists(EO_MODULATOR_DIRECTORY_WRITE[i]):
        os.makedirs(EO_MODULATOR_DIRECTORY_WRITE[i])
        #print("Directory:" + EO_MODULATOR_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        #print("Directory:" + EO_MODULATOR_DIRECTORY_WRITE[i] + "\n already exists!")
        break

EO_MODULATOR_DIRECTORY_WRITE_FILE = os.path.join(PACKAGE_DIR, EO_MODULATOR_PATH_WRITE_LUMERICAL)
if not os.path.exists(EO_MODULATOR_DIRECTORY_WRITE_FILE):
    os.makedirs(EO_MODULATOR_DIRECTORY_WRITE_FILE)
    #print("Directory:" + EO_MODULATOR_DIRECTORY_WRITE_FILE[i] + "\n created successfully!")

