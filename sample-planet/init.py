#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from func import *
import variables as var


# callback
def cb():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glShadeModel(GL_SMOOTH)

    glLightfv(GL_LIGHT0, GL_POSITION, var.light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, var.light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, var.light_ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_default_color);
    glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_default_color);
    glMaterialfv(GL_FRONT, GL_SPECULAR, var.mat_default_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, var.mat_default_shininess);

    var.clock_pre = getClockNow()
    var.clock_now = getClockNow()
