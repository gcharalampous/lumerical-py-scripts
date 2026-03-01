import numpy as np
import lumapi
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pathlib import Path
from project_layout import setup

from MODE.laser_tapered_waveguide.user_inputs.user_sweep_parameters import *
from MODE.laser_tapered_waveguide.OpticalConfinement import optical_confinement

# ------------------------- No inputs are required ---------------------------


waveguide_constructor = 'waveguide-constructor'
mesa_constructor = 'mesa-constructor'



if(__name__=="__main__"):
    spec, out, templates = setup("mode.laser_tapered_waveguide", __file__)

    with lumapi.MODE(str(templates[0])) as mode:



        mode.redrawoff()

        num_modes = 5
        structure_waveguide = waveguide_constructor + "::waveguide_core"
        structure_mesa = mesa_constructor + "::mesa_core"

        # h, w = len(wg_width_array), num_modes
        # polariz_frac = [[0 for y in range(w)] for x in range(h)] 

        polariz_frac = [0]*num_modes

        h, w = len(mesa_width_array), num_modes
        polariz_mode = [[0 for y in range(w)] for x in range(h)] 

        h, w = len(mesa_width_array), len(wg_width_array)
        conf_wg = [[0 for y in range(w)] for x in range(h)] 

        h, w = len(mesa_width_array), len(wg_width_array)
        conf_mesa = [[0 for y in range(w)] for x in range(h)] 



        mode.switchtolayout()    
        mode.setnamed("FDE","number of trial modes",num_modes)

        for md in range(0,len(mesa_width_array)):
            mode.switchtolayout()    
            mode.setnamed(mesa_constructor,"mesa_width",mesa_width_array[md])
            mode.setnamed("mesh_mesa","x span",mesa_width_array[md])
            mode.save()
            for wd in range(0,len(wg_width_array)):
                mode.switchtolayout()    
                mode.setnamed(waveguide_constructor,"width",wg_width_array[wd])
                mode.setnamed("mesh_waveguide","x span",wg_width_array[wd])
                mode.save()
                mode.mesh()
                mode.run()
                mode.findmodes()
                for m in range(1,num_modes+1):
                    polariz_frac[m-1] = (mode.getdata("FDE::data::mode"+str(m),"TE polarization fraction"))
                    
                    if ( polariz_frac[m-1] > 0.5 ):   # identify the TE-like or TM-like modes
            
                        # Do something when you locate the TE Mode
                        print("TE Mode " + str(m) + "\n")
                        conf_wg[md][wd] = optical_confinement(mode,structure_waveguide,m)
                        conf_mesa[md][wd] = optical_confinement(mode,structure_mesa,m)
                        break

                    else:
                        print("TM Mode " + str(m) + "\n")
                        continue



        
        
        





X, Y = np.meshgrid(np.array(wg_width_array)*1e6, np.array(mesa_width_array)*1e6)
Z = np.multiply(conf_mesa, 100)
levels = np.linspace(0, 100, 11)

fig, ax = plt.subplots()
cpf = ax.contourf(X, Y, Z, levels=levels, cmap=cm.Reds, extend='both')

# Set all level lines to black
line_colors = ['black' for l in cpf.levels]

# plot
cp = ax.contour(X, Y, Z, levels=levels, colors=line_colors)
ax.clabel(cp, fontsize=10, colors=line_colors)
ax.set_ylabel("AlInGaAs waveguide width [um]")
ax.set_xlabel("Si waveguide width [um]")
ax.set_title('Confinement Factor (%) to III/V waveguide')
plt.ylim([min(mesa_width_array)*1e6, max(mesa_width_array)*1e6])
plt.xlim([min(wg_width_array)*1e6, max(wg_width_array)*1e6])
plt.colorbar(cpf, ax=ax, label='Confinement Factor (%)')
plt.tight_layout()
plt.savefig(str(out["figure_groups"]["Width Sweep"] / "confinement_III_V_waveguide.png"))
plt.show()

Z = np.multiply(conf_wg, 100)
levels = np.linspace(0, 100, 11)

fig, ax = plt.subplots()
cpf = ax.contourf(X, Y, Z, levels=levels, cmap=cm.Reds, extend='both')

# Set all level lines to black
line_colors = ['black' for l in cpf.levels]

# plot
cp = ax.contour(X, Y, Z, levels=levels, colors=line_colors)
ax.clabel(cp, fontsize=10, colors=line_colors)
ax.set_ylabel("AlInGaAs waveguide width [um]")
ax.set_xlabel("Si waveguide width [um]")
ax.set_title('Confinement Factor (%) to Si waveguide')
plt.ylim([min(mesa_width_array)*1e6, max(mesa_width_array)*1e6])
plt.xlim([min(wg_width_array)*1e6, max(wg_width_array)*1e6])
plt.colorbar(cpf, ax=ax, label='Confinement Factor (%)')
plt.tight_layout()
plt.savefig(str(out["figure_groups"]["Width Sweep"] / "confinement_Si_waveguide.png"))
plt.show()

