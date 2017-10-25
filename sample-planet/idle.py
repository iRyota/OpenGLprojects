#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
import func

# callback
def cb():
    glutPostRedisplay()
