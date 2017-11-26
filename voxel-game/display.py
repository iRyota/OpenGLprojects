#!/usr/bin/python
# coding: utf-8
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from func import *
import variables as var

import math

from Object.bullet import *

DEG2RAD = math.pi/180

# callback
def cb():
    var.clock_pre = var.clock_now
    var.clock_now = getClockNow()

    if var.play_flag == 1:
        var.day += (var.clock_now - var.clock_pre)*10

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    MoveSelf()

    # ズームイン・ズームアウト & 視点の移動
    gluLookAt(var.horizontal, var.vertical, var.orthogonal, var.horizontal+math.sin(var.yaw)*math.cos(var.pitch), var.vertical+math.sin(var.pitch), var.orthogonal-math.cos(var.yaw)*math.cos(var.pitch), 0.0, 1.0, 0.0)

    glPushMatrix()

    for i in range(len(var.planet_array)):
        var.planet_array[i].draw()


    glPopMatrix()

    glutSwapBuffers()

def MoveSelf():
    var.horizontal += var.speed * var.horizontal_flag * math.cos(var.yaw) + var.speed * var.orthogonal_flag * math.sin(var.yaw)
    var.orthogonal += var.speed * var.horizontal_flag * math.sin(var.yaw) - var.speed * var.orthogonal_flag * math.cos(var.yaw)
