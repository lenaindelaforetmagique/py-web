#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
HTMLlib
22/03/2018
X. Morin
A HTML library for python.

Contains a HTMLpage class that produce a html-string to integrate to html pages.


"""

from XMLlib import *

class HTMLpage(XMLblock):
    def __init__(self, title=None):
        XMLblock.__init__(self, 'html')
        self.head = self.HEAD(title)
        self.body = self.BODY()
        self.addLine(self.head)
        self.addLine(self.body)

    def __repr__(self):
        # self.addLine(self.head)
        # self.addLine(self.body)
        res = '<!DOCTYPE html>\n{}'.format(XMLblock.__repr__(self))
        return res

    class HEAD(XMLblock):
        def __init__(self, title=None):
            XMLblock.__init__(self, 'head')
            if title is not None:
                self.addLine('<title>{}</title>'.format(title))

    class BODY(XMLblock):
        def __init__(self):
            XMLblock.__init__(self, 'body')
