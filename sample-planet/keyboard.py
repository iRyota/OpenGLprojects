#!/usr/bin/python
# coding: utf-8
# from OpenGL.GL import *
# from OpenGL.GLUT import *
import sys
from variables import *
import time
import variables as var

# callback
def cb(key, x, y):
    if key==b'\x1b': # Escape
        sys.exit()
    elif key==b'p':
        if var.flg_play == 1:
            var.flg_play = 0
        else:
            var.flg_play = 1
        time.sleep(1000)
    elif key==b'z':
        var.distance-=0.1
        if var.distance < 1.0:
            var.distance = 1.0
    elif key==b'Z':
        var.distance+=0.1
        if var.distance > 10.0:
            var.distance = 10.0
