#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from func import *
import variables as var


# callback
def cb(w, h):
    var.center_x = w/2.0
    var.center_y = h/2.0
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, w/h, 1.0, 20.0)