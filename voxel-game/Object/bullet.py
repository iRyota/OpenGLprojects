#!/usr/bin/python
# coding: utf-8
import sys, os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import math

sys.path.append(os.pardir)
import variables as var

class Bullet:
    def __init__(self):
        self.pos = [0.0,0.0,0.0]
        self.vel = [0.0,0.0,0.0]
        self.range = 10
        self.rad = 0.1
        self.hit_flag = 0
        self.shot_flag = 0

    def set_pos(self):
        self.pos = [var.horizontal,var.vertical,var.orthogonal]

    def set_vel(self):
        x = math.sin(var.yaw)*math.cos(var.pitch)
        y = math.sin(var.pitch)
        z = -math.cos(var.yaw)*math.cos(var.pitch)
        self.vel = [x,y,z]

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]

        glPushMatrix()
        glTranslatef(self.pos[0],self.pos[1],self.pos[2])
        glutSolidSphere(self.rad, 20, 20)
        glPopMatrix()

    def judge(self):
        if self.hit_flag==1:
            self.shot_flag = 0
            self.hit_flag = 0
        if self.pos[0]**2+self.pos[1]**2+self.pos[2]**2 > self.range**2:
            self.shot_flag = 0