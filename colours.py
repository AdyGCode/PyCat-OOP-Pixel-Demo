# -------------------------------------------------------------------
# Project:    PyCat
# Filename:   colours.py
# Location:   ./
# Author:     Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created:    2024-05-10
# Purpose:
#    This file provides the following features, methods and associated 
#    supporting code:
#    
# ---------------------------------------------------------------------
import numpy
from scipy.spatial import KDTree
from webcolors import (hex_to_rgb, constants)


class Colours:

    def convert_rgb_to_names(rgb_tuple=(0, 0, 0)):
        # a dictionary of all the hex and their respective names in css3
        css3_db = constants.CSS3_HEX_TO_NAMES
        names = []
        rgb_values = []
        for color_hex, color_name in css3_db.items():
            names.append(color_name)
            rgb_values.append(hex_to_rgb(color_hex))

        kdt_db = KDTree(rgb_values)
        distance, index = kdt_db.query(rgb_tuple)
        return f'closest match: {names[index]}'

    def name(self, rgb=(0, 0, 0), spec="css3"):
        return 'x'

    def rgb(self, name="black", spec="css3"):
        pass
