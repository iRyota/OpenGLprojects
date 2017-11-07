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