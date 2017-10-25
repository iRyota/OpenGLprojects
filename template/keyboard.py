#!/usr/bin/python
# coding: utf-8
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from func import *
import variables as var

# callback
def cb(key, x, y):
    if key==b'\x1b': # Escape
        sys.exit()
    elif key==b'q':
        sys.exit()
    else:
        print(key)