#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
SVGlib
22/03/2018
X. Morin
A SVG library for python.

Contains a SVGpicture class that produce a svg-string to integrate to html pages.

SVGpicture methods:
* rect
* circle
* ellipse
* line
* polygon
* polyline

"""

from XMLlib import *

class SVGpicture(XMLblock):
    def __init__(self, width=0, height=0):
        XMLblock.__init__(self, 'svg', args='width="{}" height="{}"'.format(width, height))
        self.sep = ''
        # self.width = width
        # self.height = height

    def rect(self,
        x=0, y=0,
        width=0, height=0,
        fill="none", stroke="black", strokewidth=1,
        rx=None, ry=None):
        res = '<rect '
        res += 'x="{}" y="{}" width="{}" height="{}"'.format(x, y, width, height)
        if rx is not None:
            res += 'rx={} '.format(rx)
        if ry is not None:
            res += 'ry={} '.format(ry)
        res += 'fill="{}" stroke="{}" stroke-width="{}" '.format(fill, stroke, strokewidth)
        res += '/>'
        self.addLine(res)

    def circle(self, cx=0, cy=0, r=0, fill="none", stroke="black", strokewidth=1):
        res = '<circle '
        res += 'cx="{}" cy="{}" r="{}" '.format(cx, cy, r)
        res += 'fill="{}" stroke="{}" stroke-width="{}" '.format(fill, stroke, strokewidth)
        res += '/>'
        self.addLine(res)

    def ellipse(self,
        cx=0, cy=0, rx=0, ry=0,
        fill="none", stroke="black", strokewidth=1):
        res = '<ellipse '
        res += 'cx="{}" cy="{}" rx="{}" ry="{}" '.format(cx, cy, rx, ry)
        res += 'fill="{}" stroke="{}" stroke-width="{}" '.format(fill, stroke, strokewidth)
        res += '/>'
        self.addLine(res)

    def line(self,
        x1=0, y1=0, x2=0, y2=0,
        stroke="black", strokewidth=1):
        res = '<line '
        res += 'x1="{}" y1="{}" x2="{}" y2="{}" '.format(x1, y1, x2, y2)
        res += 'stroke="{}" stroke-width="{}" '.format(stroke, strokewidth)
        res += '/>'
        self.addLine(res)

    def polygon(self,
        listOfPoints,
        fill="none", stroke="black", strokewidth=1):
        pointsCoords = ""
        for pt in listOfPoints:
            pointsCoords += '{},{} '.format(pt[0], pt[1])
        res = '<polygon '
        res += 'points="{}" '.format(pointsCoords)
        res += 'fill="{}" stroke="{}" stroke-width="{}" '.format(fill, stroke, strokewidth)
        res += '/>'
        self.addLine(res)

    def polyline(self,
        listOfPoints,
        fill="none", stroke="black", strokewidth=1):
        pointsCoords = ""
        for pt in listOfPoints:
            pointsCoords += '{},{} '.format(pt[0], pt[1])
        res = '<polyline '
        res += 'points="{}" '.format(pointsCoords)
        res += 'fill="{}" stroke="{}" stroke-width="{}" '.format(fill, stroke, strokewidth)
        res += '/>'
        self.addLine(res)
