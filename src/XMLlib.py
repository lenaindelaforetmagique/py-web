#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
XMLlib
22/03/2018
X. Morin
A XML library for python.

Contains a XMLblock class that produce a xml-string.


"""

class XMLblock:
    def __init__(self, name, args=None):
        self.name = name
        self.stack = []
        self.sep = '\n'
        if args is None:
            self.addLine('<{}>'.format(self.name))
        else:
            self.addLine('<{} {}>'.format(self.name, args))

    def addLine(self, line=""):
            self.stack.append(line)

    def __repr__(self):
        res = "" #'<{}>\n'.format(self.name)
        for s in self.stack:
            res += str(s) + self.sep
        res += '</{}>'.format(self.name)
        return res

    def __str__(self):
        return self.__repr__()
