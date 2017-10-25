#!/usr/bin/python
# coding: utf-8
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from func import *
import variables as var

# callback
def cb(button, state, x, y):
    print(button,state,x,y)