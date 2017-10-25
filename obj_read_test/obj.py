#!/usr/bin/python
# coding: utf-8
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
import obj

def load(fliePath):
    numVertices = 0
    numUVs = 0
    numNormals = 0
    numFaces = 0
    vertices = []
    uvs = []
    normals = []
    vertexColors = []
    faceVertIDs = []
    uvIDs = []
    normalIDs = []
    for line in open(fliePath, "r"):
        vals = line.split()
        if len(vals) == 0:
            continue
        if vals[0] == "v":
            v = map(float, vals[1:4])
            vertices.append(v)
            if len(vals) == 7:
                vc = map(float, vals[4:7])
                vertexColors.append(vc)
            numVertices += 1
        if vals[0] == "vt":
            vt = map(float, vals[1:3])
            uvs.append(vt)
            numUVs += 1
        if vals[0] == "vn":
            vn = map(float, vals[1:4])
            normals.append(vn)
            numNormals += 1
        if vals[0] == "f":
            fvID = []
            uvID = []
            nvID = []
            for f in vals[1:]:
                w = f.split("/")
                if numVertices > 0:
                    fvID.append(int(w[0])-1)
                if numUVs > 0:
                    uvID.append(int(w[1])-1)
                if numNormals > 0:
                    nvID.append(int(w[2])-1)
            faceVertIDs.append(fvID)
            uvIDs.append(uvID)
            normalIDs.append(nvID)
            numFaces += 1
    print "numVertices: ", numVertices
    print "numUVs: ", numUVs
    print "numNormals: ", numNormals
    print "numFaces: ", numFaces
    return vertices, uvs, normals, faceVertIDs, uvIDs, normalIDs, vertexColors
