#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# @author: Georgios Gcharalampous (gcharalampous)
# version ='1.0'
# ---------------------------------------------------------------------------
"""
User configuration for coupled ring coupler simulations.

Select which template to use. All other parameters (geometry, mesh, sources, 
monitors) should be edited directly in the Lumerical FSP template files.
"""

# 1. Select the template file by index
# Available templates:
#   0: "circular_bend_coupler.fsp"
#   1: "racetrack_coupler.fsp"

template_index = 0
