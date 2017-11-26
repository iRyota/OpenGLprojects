#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
import variables as var

# callback
def cb(button, state, x, y):
    var.mouse_button = button
    var.mouse_x = x
    var.mouse_y = y

    if state == GLUT_UP:
        var.mouse_button = -1

    glutPostRedisplay()