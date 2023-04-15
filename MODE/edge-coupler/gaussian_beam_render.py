# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:26:57 2023

@author: Georgios
"""


#----------------------------------------------------------------------------
# Imports from user files
# ---------------------------------------------------------------------------

from user_inputs.gaussian_beam_parameters import *  


def add_gaussian_beam(mode):


    
    configuration = (

        
    ("FDE", (("use fully vectorial thin lens beam profile", False),
             ("define gaussian beam by","waist size and position"),
             ("beam direction","2D Z normal"),
             ("waist radius", waist_radius),
             ("distance from waist", distance_from_waist),
             ("refractive index", refractive_index),
             ("theta", theta),
             ("phi", phi),
             ("polarization angle", polarization_angle),
             ("sample span", sample_span),
             ("sample resolution",sample_resolution))),  
    )

    # Populate the waveguide simulation region

    for obj, parameters in configuration:
           for k, v in parameters:
               mode.setnamed(obj, k, v)
   
    mode.createbeam()
