#!/usr/bin/python
# coding: utf-8
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from func import *
import variables as var

import math

DEG2RAD = math.pi/180

# callback
def cb():
    var.clock_pre = var.clock_now
    var.clock_now = getClockNow()

    if var.flg_play == 1:
        var.day += (var.clock_now - var.clock_pre)*10

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0.0, 0.0, var.distance, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotatef(-var.pitch, 1.0, 0.0, 0.0)
    glRotatef(-var.yaw, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_default_color)
    glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_default_color)
    DrawCircle(var.orbit_radius_mercury)
    DrawCircle(var.orbit_radius_venus)
    DrawCircle(var.orbit_radius_earth)
    DrawCircle(var.orbit_radius_mars)

    glPushMatrix() #level01

    # 太陽
    glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_sun)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_sun)

    glPushMatrix() #level02
    glRotatef(var.rot_vel_sun * var.day, 0.0, 1.0, 0.0)
    DrawPlanet(var.radius_sun)
    glPopMatrix() #level02

    # 水星
    glPushMatrix() #level02

    glRotatef(var.rev_vel_mercury * var.day, 0.0, 1.0, 0.0)
    glTranslatef(var.orbit_radius_mercury, 0.0, 0.0)
    glRotatef(var.rot_vel_mercury * var.day, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_mercury)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_mercury)

    DrawPlanet(var.planet_radius_mercury)

    glPopMatrix() #level02

    # 金星
    glPushMatrix() #level02

    glRotatef(var.rev_vel_venus * var.day, 0.0, 1.0, 0.0)
    glTranslatef(var.orbit_radius_venus, 0.0, 0.0)
    glRotatef(var.rot_vel_venus * var.day, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_venus)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_venus)

    DrawPlanet(var.planet_radius_venus)

    glPopMatrix() #level02

    # 地球
    glPushMatrix() #level02

    glRotatef(var.rev_vel_earth * var.day, 0.0, 1.0, 0.0)
    glTranslatef(var.orbit_radius_earth, 0.0, 0.0)
    glRotatef(var.rot_vel_earth * var.day, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_earth)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_earth)

    DrawPlanet(var.planet_radius_earth)

    # 月
    glPushMatrix() #level03

    glRotatef(var.rev_vel_moon * var.day, math.cos(math.pi/3), math.sin(math.pi/3), 0.0)
    glTranslatef(0.0, 0.0, var.orbit_radius_moon)
    glRotatef(var.rot_vel_moon * var.day, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_moon)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_moon)

    DrawPlanet(var.planet_radius_moon)

    glPopMatrix() #level03

    glPopMatrix() #level02

    # 火星
    glPushMatrix() #level02

    glRotatef(var.rev_vel_mars * var.day, 0.0, 1.0, 0.0)
    glTranslatef(var.orbit_radius_mars, 0.0, 0.0)
    glRotatef(var.rot_vel_mars * var.day, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_mars)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_mars)

    DrawPlanet(var.planet_radius_mars)

    glPopMatrix() #level02

    glPopMatrix() #level01

    glutSwapBuffers()



def DrawCircle(radius):
    glBegin(GL_LINE_LOOP)

    for i in range(360):
        degInRad = i * DEG2RAD
        glVertex3f(math.cos(degInRad)*radius, 0.0, math.sin(degInRad)*radius)

    glEnd()

def DrawPlanet(radius):
    glPushMatrix()

    glRotatef(90.0, 1.0, 0.0, 0.0)
    glutWireSphere(radius, 20, 20)

    glPopMatrix()



