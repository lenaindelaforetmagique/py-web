#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from SVGlib import *
from math import pi, cos, sin
from random import randrange

class HTMLpage:
    def __init__(self, title="No title"):
        self.title = title
        self.stack = []

    def addLine(self, line=""):
        self.stack.append(line)

    def __repr__(self):
        res = '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n'
        res += '<title>{}</title>\n</head>\n<body leftmargin="0" topmargin="0" rightmargin="0">\n'.format(self.title)
        for s in self.stack:
            res += str(s) #+ '\n'
        res += '</body>\n</html>'
        return res

    def __str__(self):
        return self.__repr__()


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

file = open("pi1000000.txt")
pidigits = file.readlines()
file.close()

pidigits=[int(c) for i, c in enumerate(pidigits[0]) if c != '.' and i<10000]

contenu = HTMLpage("Digits of pi")
contenu.addLine('<p style="line-height:0%">')

h = 30
w = 30

for d in pidigits:
    img = SVGpicture(w,h)
    img.rect(0,0,w,h,rx=h/4, ry=w/3,fill='hsl({}, {}%,{}%)'.format(d*360/10,100,50),strokewidth=0)
    # img.circle(10/2,10/2, 50, fill=COLORS[d+6],strokewidth=0)
    contenu.addLine(img)
    # contenu.addLine(d)

# contenu.addLine("</p>")
file = open("digitsofpi.htm", "w")
file.write(str(contenu))
file.close()
