#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
import func
import variables as var
import math

# ボタンが押されているときに呼ばれるcallback
def cb(x, y):
    if var.play_flag==0:
        if var.mouse_button == GLUT_LEFT_BUTTON:
            if x == var.mouse_x and y == var.mouse_y:
                return

            var.yaw -= (x - var.mouse_x)/1000.0
            var.pitch -= (y - var.mouse_y)/1000.0
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

    if var.yaw < -2*math.pi:
        var.yaw += 2*math.pi
    elif var.yaw > 2*math.pi:
        var.yaw -= 2*math.pi

    if var.pitch < -math.pi / 2:
        var.pitch = -math.pi/2
    elif var.pitch > math.pi / 2:
        var.pitch = math.pi/2

    glutPostRedisplay()

# ボタンが押されていないときに呼ばれるcallback
def cb_passive(x, y):
    if var.play_flag==1:
        var.yaw += (x - var.center_x)/20000.0
        var.pitch -= (y - var.center_y)/20000.0

    if var.yaw < -2*math.pi:
        var.yaw += 2*math.pi
    elif var.yaw > 2*math.pi:
        var.yaw -= 2*math.pi

    if var.pitch < -math.pi / 2:
        var.pitch = -math.pi/2
    elif var.pitch > math.pi / 2:
        var.pitch = math.pi/2









