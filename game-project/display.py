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

    # 弾丸発射
    ShootBullet()

    glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_default_color)
    glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_default_color)
    for i in range(len(var.planet_array)):
        if not var.planet_array[i].orbit_rad == 0:
            DrawCircle(var.planet_array[i].orbit_rad)
    # DrawCircle(var.orbit_radius_mercury)
    # DrawCircle(var.orbit_radius_venus)
    # DrawCircle(var.orbit_radius_earth)
    # DrawCircle(var.orbit_radius_mars)

    # glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0,0.0,0.8,1.0])
    # glMaterialfv(GL_FRONT, GL_AMBIENT, [1.0,0.0,0.0,1.0])
    # glBegin(GL_LINE_STRIP)
    # glVertex3f(0.0,0.3,0.0)
    # glVertex3f(100.0,0.3,0.0)
    # glEnd()

    # glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8,1.0,0.0,1.0])
    # glMaterialfv(GL_FRONT, GL_AMBIENT, [0.0,1.0,0.0,1.0])
    # glBegin(GL_LINE_STRIP)
    # glVertex3f(0.0,0.3,0.0)
    # glVertex3f(0.0,100.0,0.0)
    # glEnd()

    # glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.8,1.0,1.0])
    # glMaterialfv(GL_FRONT, GL_AMBIENT, [0.0,0.0,1.0,1.0])
    # glBegin(GL_LINE_STRIP)
    # glVertex3f(0.0,0.3,0.0)
    # glVertex3f(0.0,0.3,100.0)
    # glEnd()

    glPushMatrix() #level01

    # 太陽
    # glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_sun)
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_sun)

    # glPushMatrix() #level02
    # glRotatef(var.rot_vel_sun * var.day, 0.0, 1.0, 0.0)
    # DrawPlanet(var.radius_sun)
    # glPopMatrix() #level02

    for i in range(len(var.planet_array)):
        var.planet_array[i].draw()

    # # 水星
    # glPushMatrix() #level02

    # glRotatef(var.rev_vel_mercury * var.day, 0.0, 1.0, 0.0)
    # glTranslatef(var.orbit_radius_mercury, 0.0, 0.0)
    # glRotatef(var.rot_vel_mercury * var.day, 0.0, 1.0, 0.0)

    # glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_mercury)
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_mercury)

    # DrawPlanet(var.planet_radius_mercury)

    # glPopMatrix() #level02

    # # 金星
    # glPushMatrix() #level02

    # glRotatef(var.rev_vel_venus * var.day, 0.0, 1.0, 0.0)
    # glTranslatef(var.orbit_radius_venus, 0.0, 0.0)
    # glRotatef(var.rot_vel_venus * var.day, 0.0, 1.0, 0.0)

    # glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_venus)
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_venus)

    # DrawPlanet(var.planet_radius_venus)

    # glPopMatrix() #level02

    # # 地球
    # glPushMatrix() #level02

    # glRotatef(var.rev_vel_earth * var.day, 0.0, 1.0, 0.0)
    # glTranslatef(var.orbit_radius_earth, 0.0, 0.0)
    # glRotatef(var.rot_vel_earth * var.day, 0.0, 1.0, 0.0)

    # glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_earth)
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_earth)

    # DrawPlanet(var.planet_radius_earth)

    # # 月
    # glPushMatrix() #level03

    # glRotatef(var.rev_vel_moon * var.day, math.cos(math.pi/3), math.sin(math.pi/3), 0.0)
    # glTranslatef(0.0, 0.0, var.orbit_radius_moon)
    # glRotatef(var.rot_vel_moon * var.day, 0.0, 1.0, 0.0)

    # glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_moon)
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_moon)

    # DrawPlanet(var.planet_radius_moon)

    # glPopMatrix() #level03

    # glPopMatrix() #level02

    # # 火星
    # glPushMatrix() #level02

    # glRotatef(var.rev_vel_mars * var.day, 0.0, 1.0, 0.0)
    # glTranslatef(var.orbit_radius_mars, 0.0, 0.0)
    # glRotatef(var.rot_vel_mars * var.day, 0.0, 1.0, 0.0)

    # glMaterialfv(GL_FRONT, GL_AMBIENT, var.mat_color_mars)
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, var.mat_color_mars)

    # DrawPlanet(var.planet_radius_mars)

    # glPopMatrix() #level02

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

def MoveSelf():
    var.horizontal += var.speed * var.horizontal_flag * math.cos(var.yaw) + var.speed * var.orthogonal_flag * math.sin(var.yaw)
    var.orthogonal += var.speed * var.horizontal_flag * math.sin(var.yaw) - var.speed * var.orthogonal_flag * math.cos(var.yaw)

def ShootBullet():
    if var.shoot_flag==1 and var.shoot_lock==0:
        for i in range(3):
            if var.shoot_array[i].shot_flag == 0:
                var.shoot_array[i].shot_flag = 1
                var.shoot_array[i].set_pos()
                var.shoot_array[i].set_vel()
                var.shoot_lock = 1
                break
    for i in range(3):
        if var.shoot_array[i].shot_flag == 1:
            var.shoot_array[i].move()
            var.shoot_array[i].judge()









