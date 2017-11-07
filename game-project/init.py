#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from func import *
import math
import variables as var

from Object.planet import *


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

    sun = Planet("sun",1.0 / 27.275,[0,1.0,0],0,[0,1.0,0],0,1.0,[0.8, 0.2, 0.2, 1.0],100)
    var.planet_array.append(sun)

    mercury = Planet("mercury",1.0 / 58.65,[0,1.0,0],1.0 / 0.241,[0,1.0,0],1.5,0.1,[0.1,0.6,1.0,1.0],20)
    var.planet_array.append(mercury)

    venus = Planet("venus",1.0 / 243.0187,[0.0,1.0,0.0],1.0 / 0.615,[0.0,1.0,0.0],2.0,0.12,[0.6,1.0,0.1,1.0],15)
    var.planet_array.append(venus)

    earth = Planet("earth",1.0 / 0.997271,[0,1.0,0],1.0,[0,1.0,0],2.5,0.12,[0.1,0.3,0.8,1.0],50)
    moon = Planet("moon",1.0 / 27.32,[0,1.0,0],1.0 / 27.32 * 365.2564,[math.cos(math.pi/3), math.sin(math.pi/3), 0.0],0.3,0.05,[0.2,0.2,0.2,1.0],10)
    AssocPlanet(earth,moon)
    var.planet_array.append(earth)

    mars = Planet("mars",1.0 / 1.02595,[0.0,1.0,0.0],1.0 / 1.881,[0.0,1.0,0.0],4.0,0.09,[0.6,0.2,0.3,1.0],25)
    var.planet_array.append(mars)

def AssocPlanet(parent_planet, child_planet):
    parent_planet.set_child(child_planet)
    child_planet.set_parent(parent_planet)