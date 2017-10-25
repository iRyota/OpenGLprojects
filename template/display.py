#!/usr/bin/python
# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *

from func import *
import variables as var

# callback
def cb():
    # OpenGLバッファのクリア
    glClearColor(0.0, 0.5, 0.5, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 三角形描画開始
    glBegin(GL_TRIANGLES)
    # 左下
    glVertex(-1, -1)
    # 右下
    glVertex(1, -1)
    # 上
    glVertex(0, 1)
    # 三角形描画終了
    glEnd()

    # OpenGL描画実行
    glFlush()
    # glutダブルバッファ交換
    glutSwapBuffers()