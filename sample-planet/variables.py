#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *

#----------------
# グローバル変数
#----------------

# 再生・停止フラグ
flg_play = 1

# 視点情報
distance = 5.0
pitch = 0.0
yaw = 0.0

# マウス入力情報
mouse_button = -1
mouse_x = 0
mouse_y = 0

# クロック
clock_now = 0
clock_pre = 0

# 日
day = 0

light_position = [0.0, 0.0, 0.0, 1.0]
light_ambient = [1.0, 1.0, 1.0, 1.0]
light_diffuse = [1.0, 1.0, 1.0, 1.0]

mat_default_color = [1.0, 1.0, 1.0, 1.0]
mat_default_specular = [0.0, 0.0, 0.0, 0.0]
mat_default_shininess = [100.0]
mat_default_emission = [0.0, 0.0, 0.0, 0.0]

# 太陽
radius_sun = 1.0
mat_color_sun = [0.8, 0.2, 0.2, 1.0]
rot_vel_sun = 1.0 / 27.275


# 水星
mat_color_mercury = [ 0.1, 0.6, 1.0, 1.0 ]
planet_radius_mercury = 0.1
orbit_radius_mercury = 1.5
rev_vel_mercury = 1.0 / 0.241
rot_vel_mercury = 1.0 / 58.65

# 金星
mat_color_venus = [ 0.6, 1.0, 0.1, 1.0 ]
planet_radius_venus = 0.12
orbit_radius_venus = 2.0
rev_vel_venus = 1.0 / 0.615
rot_vel_venus = 1.0 / 243.0187

# 地球
mat_color_earth = [ 0.1, 0.3, 0.8, 1.0 ]
planet_radius_earth = 0.12
orbit_radius_earth = 2.5
rev_vel_earth = 1.0
rot_vel_earth = 1.0 / 0.997271

# 月
mat_color_moon = [ 0.2, 0.2, 0.2, 1.0 ]
planet_radius_moon = 0.05
orbit_radius_moon = 0.3
rev_vel_moon = 1.0 / 27.32 * 365.2564
rot_vel_moon = 1.0 / 27.32

# 火星
mat_color_mars = [ 0.6, 0.2, 0.3, 1.0 ]
planet_radius_mars = 0.09
orbit_radius_mars = 4.0
rev_vel_mars = 1.0 / 1.881
rot_vel_mars = 1.0 / 1.02595




