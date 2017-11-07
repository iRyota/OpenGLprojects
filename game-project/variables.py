#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *

from Object.bullet import *
from Object.planet import *

import math
#----------------
# グローバル変数
#----------------

# 画面の中心
center_x = 480
center_y = 360

# 再生・停止フラグ
play_flag = 1

# 視点情報
distance = 5.0
pitch = 0.0
yaw = 0.0

# マウス入力情報
mouse_button = -1
mouse_x = 0
mouse_y = 0

# 視点移動に関する情報
horizontal = 0      # 横方向移動
vertical = 0.5        # 縦方向移動
orthogonal = 4.5      # 奥行き方向移動

horizontal_flag = 0      # 横方向移動方向フラグ
vertical_flag = 0        # 縦方向移動方向フラグ
orthogonal_flag = 0      # 奥行き方向移動方向フラグ

# 弾丸発射フラグ
shoot_flag = 0

# 弾丸発射インターバル用フラグ
shoot_lock = 0

# 弾丸情報格納用の配列
shoot_array = [Bullet(), Bullet(), Bullet()]

# 惑星情報格納用の配列
planet_array = []

# 移動速さ
speed = 0.01

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




