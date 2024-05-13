# -------------------------------------------------------------------
# Project:    PyCat
# Filename:   cat.py
# Location:   ./
# Author:     Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created:    2024-05-10
# Purpose:
#    This file provides the following features, methods and associated 
#    supporting code:
#    
# ---------------------------------------------------------------------
import time

from simulsense_hat import SenseHat


class Cat:
    BLACK = (0, 0, 0)
    BLANK = (0, 0, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 192, 192)
    GREEN = (0, 255, 0)
    INDIGO = (64, 0, 192)
    PURPLE = (128, 0, 192)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)
    CHARCOAL = (64, 64, 64)
    SILVER = (192, 192, 192)
    YELLOW = (255, 255, 0)
    ORANGE = (192, 128, 0)

    def __init__(self, fg="WHITE", bg=BLACK):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()

        b = self.colourise("blue")
        c = self.colourise("cyan")
        g = self.colourise("green")
        k = self.colourise("black")
        m = self.colourise("magenta")
        p = self.colourise("purple")
        r = self.colourise("red")
        w = self.colourise("white")
        y = self.colourise("yellow")
        e = self.colourise("gray")
        d = self.colourise("charcoal")
        s = self.colourise("silver")
        o = self.colourise("orange")
        w = self.colourise("brown")

        self.pixels = [  # Pixels
            p, p, p, p, p, p, p, p,  # 00 - 07
            p, p, p, o, p, p, d, p,  # 08 - 15
            p, p, p, o, o, d, d, p,  # 16 - 23
            d, o, p, o, g, d, g, p,  # 24 - 31
            o, p, p, d, o, s, s, p,  # 32 - 39
            d, o, d, s, s, o, p, p,  # 40 - 47
            p, d, s, s, s, s, p, p,  # 48 - 55
            p, o, k, p, p, k, p, p,  # 56 - 63
        ]

        self.eyes = [28, 30]
        self.tongue = [37]

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)

    def blink(self, blink_colour=["ORANGE", "CHARCOAL"], duration=1):
        original_colours = []
        for eye_pixel in self.eyes:
            original_colours.append(self.pixels[eye_pixel])
        count = 0
        for eye_pixel in self.eyes:
            self.pixels[eye_pixel] = self.colourise(blink_colour[count])
            count += 1
        self.show()
        time.sleep(duration)
        count = 0
        for eye_pixel in self.eyes:
            self.pixels[eye_pixel] = original_colours[count]
            count += 1
        self.show()

    # Not part of the SenseHat implementation
    def colourise(self, colour_name="black"):
        colour_name = colour_name.upper()
        c = self.BLACK
        if colour_name == "BLUE":
            c = self.BLUE
        elif colour_name == "GREEN":
            c = self.GREEN
        elif colour_name == "BLACK":
            c = self.BLACK
        elif colour_name == "YELLOW":
            c = self.YELLOW
        elif colour_name == "ORANGE":
            c = self.ORANGE
        elif colour_name == "PURPLE":
            c = self.PURPLE
        elif colour_name == "INDIGO":
            c = self.INDIGO
        elif colour_name == "CYAN":
            c = self.CYAN
        elif colour_name in ["GREY", "GRAY"]:
            c = self.GREY
        elif colour_name == "SILVER":
            c = self.SILVER
        elif colour_name == "WHITE":
            c = self.WHITE
        elif colour_name == "CHARCOAL":
            c = self.CHARCOAL
        return c
