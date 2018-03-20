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
        res += '<title>{}</title>\n</head>\n<body>\n'.format(self.title)
        for s in self.stack:
            res += str(s) + '\n'
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

image = SVGpicture(500, 500)
for i in range(100):
    teta = 10*pi*i/100
    rd = 150*i/100
    r = rd*(1+cos(i/10)/2)
    image.circle(150+r*cos(teta),150+ r*sin(teta), rd/10, stroke = "none", fill=COLORS[i%len(COLORS)])

contenu = HTMLpage("BIdule")
contenu.addLine(image)

file = open("test.html", "w")
file.write(str(contenu))
file.close()
