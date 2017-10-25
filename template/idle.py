#!/usr/bin/python
# coding: utf-8
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
import func

# callback
def cb():
    print("idle")
    # glutPostRedisplay()
