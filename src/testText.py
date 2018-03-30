#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from SVGlib import *
from HTMLlib import *
from math import pi, cos, sin
from random import randrange
import os

print(os.getcwd())

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

file = open("examples/pi1000000.txt")
pidigits = file.readlines()
file.close()

pidigits=[int(c) for i, c in enumerate(pidigits[0]) if c != '.' and i<1000]

page = HTMLpage("Digits of pi")
page.head.addLine('<meta charset="utf-8">')
page.body.addLine('<p style="line-height:0%">')

h = 30
w = 30
r = 0.9*(h+w)/4
for i, d in enumerate(pidigits):
    img = SVGpicture(w,h)
    teta = i*2*pi/len(pidigits)
    img.circle(h/2,w/2, r/1.5, fill=COLORS[d+6],strokewidth=0)
    #img.line(w/2, h/2, w/2+r*cos(teta), h/2-r*sin(teta), strokewidth=2)
    s = 12
    img.text(w/2, h/2, d, fill="black", fontfamily="Monaco", fontsize=s)
    # img.rect(0,0,w,h,rx=h/4, ry=w/3,fill='hsl({}, {}%,{}%)'.format(d*360/10,100,50),strokewidth=0)

    page.body.addLine(img)

page.body.addLine("</p>")

file = open("examples/digitsofpi3.htm", "w")
file.write(str(page))
file.close()
