#!/usr/bin/python
# coding: utf-8
# from OpenGL.GL import *
# from OpenGL.GLUT import *
import sys
from variables import *
import time
import variables as var


# キーが押されたときのcallback
def cb(key, x, y):
    if key==GLUT_KEY_LEFT:
        var.horizontal_flag = -1
    if key==GLUT_KEY_RIGHT:
        var.horizontal_flag = 1
    if key==GLUT_KEY_UP:
        var.orthogonal_flag = 1
    if key==GLUT_KEY_DOWN:
        var.orthogonal_flag = -1
    # else:
    #     var.horizontal = 0
    #     var.vertical = 0

# キーが離されたときのcallback
def cb_up(key, x, y):
    if key==GLUT_KEY_LEFT or key==GLUT_KEY_RIGHT:
        var.horizontal_flag = 0
    if key==GLUT_KEY_UP or key==GLUT_KEY_DOWN:
        var.orthogonal_flag = 0


