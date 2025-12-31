# Device Library for Optoelectronic Simulations

## Purpose
This library contains Lumerical DEVICE simulations for extracting optoelectronic properties of integrated photonic devices, including IV curves, charge distribution, capacitance, electrostatics, and Pockels effects. The simulations support geometry selection and provide inputs for downstream optical simulations and free-carrier absorption modeling.

## Features

### [electro-optic](electro_optic)
    This module models a Pockels electro-optic modulator to study electric-field-induced refractive index changes and their effect on optical transmission. The simulation quantifies the electro-optic coefficient and modulation efficiency under applied voltage.


### [pin-modulator](pin_modulator)
    This module models a PIN optical modulator to study carrier-induced refractive index and absorption changes under electrical bias. The simulation is used to quantify the optoelectronic properties of the PIN junction.

### [disk-modulator](disk_modulator)
    This module models a high-speed PN junction optical modulator to study carrier-induced refractive index and absorption changes under electrical bias. The simulation quantifies the optoelectronic modulation efficiency and frequency response of the PN junction.


