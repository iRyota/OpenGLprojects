#!/usr/bin/python
# coding: utf-8
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
import func

# callback
def cb(button, state, x, y):
    print(button,state,x,y)