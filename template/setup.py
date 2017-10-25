#!/usr/bin/python
# coding: utf-8
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
import func

import display
import reshape
import mouse
import motion
import keyboard
import init
import idle

def setup():
    glutInit(sys.argv)
    # RGBAモード、ダブルバッファリング有効、Zバッファ有効で初期化
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutCreateWindow("glut sample")
    # Windowのサイズが変わった時に呼ばれる関数を登録
    glutReshapeFunc(reshape.cb)
    # 描画時に呼ばれる関数を登録
    glutDisplayFunc(display.cb)
    # マウスボタン押し上げ時に呼ばれる関数
    glutMouseFunc(mouse.cb)
    # マウスドラッグ時に呼ばれる関数
    glutMotionFunc(motion.cb)
    # キーボードが押された時に呼ばれる関数
    glutKeyboardFunc(keyboard.cb)
    # アイドル時に呼ばれる関数
    # glutIdleFunc(idle.cb)