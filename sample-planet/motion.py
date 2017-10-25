#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
import func
import variables as var

# callback
def cb(x, y):
    if var.mouse_button == GLUT_LEFT_BUTTON:
        if x == var.mouse_x and y == var.mouse_y:
            return

        var.yaw -= (x - var.mouse_x)/100.0
        var.pitch -= (y - var.mouse_y)/100.0
    elif mouse_button == GLUT_RIGHT_BUTTON:
        if y == var.mouse_y:
            return
        if y < mouse_y:
            var.distance += (var.mouse_y - y)/50.0
        else:
            var.distance += (y - var.mouse_y)/50.0

        if var.distance < 1.0:
            var.distance = 1.0
        if var.distance > 10.0:
            var.distance = 10.0

    var.mouse_x = x
    var.mouse_y = y

    glutPostRedisplay()
