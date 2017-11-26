#!/usr/bin/python
# coding: utf-8
# from OpenGL.GL import *
# from OpenGL.GLUT import *
import sys
from variables import *
import time
import variables as var

# キーが押されたときに呼ばれるcallback
def cb(key, x, y):
    if key==b'\x1b': # Escape
        sys.exit()
    elif key==b'p':
        if var.play_flag == 1:
            var.play_flag = 0
        else:
            var.play_flag = 1
        time.sleep(1000)
    elif key==b'z':
        var.distance-=0.1
        if var.distance < 1.0:
            var.distance = 1.0
    elif key==b'Z':
        var.distance+=0.1
        if var.distance > 10.0:
            var.distance = 10.0
    elif key==b' ':
        var.shoot_flag = 1

# キーが離されたときに呼ばれるcallback
def cb_up(key, x, y):
    if key==b' ':
        var.shoot_flag = 0
        var.shoot_lock = 0