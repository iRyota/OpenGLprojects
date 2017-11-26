#!/usr/bin/python
# coding: utf-8
import sys, os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import math
import numpy as np

sys.path.append(os.pardir)
import variables as var

class  Planet:
    def __init__(self,name,rot_vel,rot_axis,rev_vel,rev_axis,orbit_rad,planet_rad,color,hp):
        self.name = name
        self.pos = [0.0,0.0,0.0]
        self.rot_vel = rot_vel
        self.rot_axis = rot_axis
        self.rev_vel = rev_vel
        self.rev_axis = rev_axis
        self.orbit_rad = orbit_rad
        self.planet_rad = planet_rad
        self.color = color
        self.hp = 0
        self.children = []
        self.parent = None

    def set_parent(self, parent_planet):
        self.parent = parent_planet

    def set_child(self, child_planet):
        self.children.append(child_planet)

    # def set_pos(self):
    #     axis_norm = math.sqrt(self.rev_axis[0]**2+self.rev_axis[1]**2+self.rev_axis[2]**2)
    #     skew_symmetric = np.array([[0,-self.rev_axis[0],self.rev_axis[1]],[self.rev_axis[2],0,-self.rev_axis[0]],[-self.rev_axis[1],self.rev_axis[0],0]])
    #     skew_symmetric = skew_symmetric/axis_norm
    #     rotation_matrix = np.identity(3)+skew_symmetric*math.sin(self.rev_vel*var.day)+np.dot(skew_symmetric,skew_symmetric)*(1-math.cos(self.rev_vel*var.day))
    #     self.pos = self.parent.pos+rotation_matrix

    def draw(self):

        glPushMatrix()

        glRotatef(self.rev_vel * var.day, self.rev_axis[0],self.rev_axis[1],self.rev_axis[2])
        if self.rev_axis[0]==0 and self.rev_axis[2]==0:
            glTranslatef(self.orbit_rad, 0.0, 0.0)
        else:
            norm = math.sqrt(self.rev_axis[0]**2+self.rev_axis[2]**2)
            glTranslatef(-self.orbit_rad * self.rev_axis[2]/norm, 0.0, self.orbit_rad * self.rev_axis[0]/norm)
        glRotatef(self.rot_vel * var.day, self.rot_axis[0],self.rot_axis[1],self.rot_axis[2])
        glMaterialfv(GL_FRONT, GL_AMBIENT, self.color)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.color)

        glPushMatrix()
        glRotatef(90.0, 1.0, 0.0, 0.0)
        glutWireSphere(self.planet_rad, 20, 20)
        glPopMatrix()

        if not self.children == []:
            for i in range(len(self.children)):
                self.children[i].draw()

        glPopMatrix()

    # def judge(self):
