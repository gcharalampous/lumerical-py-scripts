import os


PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))



#PACKAGE DIRECTORIES

# SWG
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
        print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n created successfully!")
    else:
        print("Directory:" + FDTD_SWG_DIRECTORY_WRITE[i] + "\n already exists!")

