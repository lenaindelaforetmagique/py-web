#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from HTMLlib import *
from SVGlib import *
from math import pi, cos, sin
from random import randrange


COLORS = ["#002B36",
          "#073642",
          "#586E75",
          "#657B83",
          "#839496",
          "#93A1A1",
          "#EEE8D5",
          "#FDF6E3",
          "#B58900",
          "#CB4B16",
          "#DC322F",
          "#D33682",
          "#6C71C4",
          "#268BD2",
          "#2AA198",
          "#859900"]

image = SVGpicture(500, 500)
for i in range(16):
    teta = pi*i/10-pi/2
    rd = 15*i/1.5
    r = rd*(1+2*cos(i/10)/2)/1.5
    image.circle(150+r*cos(teta),150+ r*sin(teta), rd/10, stroke = "none", fill=COLORS[i%len(COLORS)])

contenu = HTMLpage("BIdule")
contenu.addLine(image)

file = open("test.html", "w")
file.write(str(contenu))
file.close()
