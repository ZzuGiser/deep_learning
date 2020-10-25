#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin
def plot_with_labels(lowDWeights, labels):
    plt.cla()
    X, Y = lowDWeights[:, 0], lowDWeights[:, 1]
    for x, y, s in zip(X, Y, labels):
        c = cm.rainbow(int(255 * s / 9)); plt.text(x, y, s, backgroundcolor=c, fontsize=9)
    plt.xlim(0, 1); plt.ylim(0, 1); plt.title('用户分类可视化示意图'); plt.show(); plt.pause(0.01)
def sortclass(x,y,z):
    if  (x> 0 and x < 0.5) :
        if (y>0) and (y < 0.5):
            if (z>0) and (z<0.5):
                return 1
            else:
                return 5
        else:
            if (z>0) and (z<0.5):
                return 2
            else:
                return 6
    else:
        if (y>0) and (y < 0.5):
            if (z>0) and (z<0.5):
                return 3
            else:
                return 7
        else:
            if (z>0) and (z<0.5):
                return 4
            else:
                return 8




fig = plt.figure()
ax = Axes3D(fig)
# X, Y value
X = randrange(5, 0.1, 1)
Y = randrange(5,0.1, 1)
# X, Y = np.meshgrid(X, Y)
Z= randrange(5,0.1, 1)
# height value
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='r')
# ax.plot_surface(X, Z,Y, rstride=1, cstride=1, color='g')
# ax.plot_surface(Z, Y, X, rstride=1, cstride=1, color='b')
n = 10
cValue = ['r','y','g','b','r','y','g','b']
labels=range(1,9)
for x, y, z in zip(X, Y, Z):
    s=sortclass(x,y,z)
    c = cm.rainbow(int(255 * s / 8))
    # ax.text(x, y, z,backgroundcolor=c, fontsize=9)
    ax.scatter(x,y,z,c=c)
"""
============= ================================================
        Argument      Description
        ============= ================================================
        *X*, *Y*, *Z* Data values as 2D arrays
        *rstride*     Array row stride (step size), defaults to 10
        *cstride*     Array column stride (step size), defaults to 10
        *color*       Color of the surface patches
        *cmap*        A colormap for the surface patches.
        *facecolors*  Face colors for the individual patches
        *norm*        An instance of Normalize to map values to colors
        *vmin*        Minimum value to map
        *vmax*        Maximum value to map
        *shade*       Whether to shade the facecolors
        ============= ================================================
"""

# I think this is different from plt12_contours
# ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
"""
==========  ================================================
        Argument    Description
        ==========  ================================================
        *X*, *Y*,   Data values as numpy.arrays
        *Z*
        *zdir*      The direction to use: x, y or z (default)
        *offset*    If specified plot a projection of the filled contour
                    on this position in plane normal to zdir
        ==========  ================================================
"""

ax.set_zlim(0, 1)
plt.xlim((0, 1))
plt.ylim((0, 1))


plt.show()
