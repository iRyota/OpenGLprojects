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
import specialkey

def setup():
    glutInit(sys.argv)
    # RGBAモード、ダブルバッファリング有効、Zバッファ有効で初期化
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(960, 720)
    glutCreateWindow("sample-planet")

    init.cb()

    # Windowのサイズが変わった時に呼ばれる関数を登録
    glutReshapeFunc(reshape.cb)
    # 描画時に呼ばれる関数を登録
    glutDisplayFunc(display.cb)
    # マウスボタン押し上げ時に呼ばれる関数
    glutMouseFunc(mouse.cb)
    # マウスドラッグ時に呼ばれる関数
    glutMotionFunc(motion.cb)
    # マウスボタンが押されていない時に呼ばれる関数
    glutPassiveMotionFunc(motion.cb_passive)
    # キーボードが押された時に呼ばれる関数
    glutKeyboardFunc(keyboard.cb)
    # キーボードが離された時に呼ばれる関数
    glutKeyboardUpFunc(keyboard.cb_up)
    # 文字キー以外の特殊キーが押された時に呼ばれる関数
    glutSpecialFunc(specialkey.cb)
    # 文字キー以外の特殊キーが離された時に呼ばれる関数
    glutSpecialUpFunc(specialkey.cb_up)
    # アイドル時に呼ばれる関数
    glutIdleFunc(idle.cb)









