# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


# ------------------------------------------------散点图-----------------------------------
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)   
# arctan2()和arctan()的区别可以百度，其中arctan2()需要输入两个数组，正切值是两数组中的比值

plt.scatter(X,Y,s = 75,c = T,alpha = .5)

plt.xlim((-1.5,1.5))
plt.xticks([])    # 去掉x轴标签
plt.ylim((-1.5,1.5))
plt.yticks([])    # 去掉y轴标签
plt.show()


# -------------------------------------------柱状图------------------------------

n = 12
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5,1.0,n)
#facecolor:表面的颜色;edgecolor:边框的颜色
plt.bar(X,+Y1,facecolor = '#9999ff',edgecolor = 'white')
plt.bar(X,-Y2,facecolor = '#ff9999',edgecolor = 'white')
#描绘text在图表上
# plt.text(0 + 0.4, 0 + 0.05,"huhu")
for x,y in zip(X,Y1):
    #ha : horizontal alignment
    #va : vertical alignment
    plt.text(x + 0.01,y+0.05,'%.2f'%y,ha = 'center',va='bottom')

for x,y in zip(X,Y2):
    # ha : horizontal alignment
    # va : vertical alignment
    plt.text(x+0.01,-y-0.05,'%.2f'%(-y),ha='center',va='top')

plt.xlim(-.5,n)
plt.yticks([])
plt.ylim(-1.25,1.25)
plt.yticks([])
plt.show()





# -----------------------------------------Contour等高线图----------------------------
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    #the height function
    return (1-x/2 + x**5+y**3) * np.exp(-x **2 -y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
#meshgrid函数用两个坐标轴上的点在平面上画网格。
X,Y = np.meshgrid(x,y)

#use plt.contourf to filling contours
#X Y and value for (X,Y) point
#这里的8就是说明等高线分成多少个部分，如果是0则分成2半
#则8是分成10半
#cmap找对应的颜色，如果高=0就找0对应的颜色值，
plt.contourf(X,Y,f(X,Y),8,alpha = .75,cmap = plt.cm.hot)

#use plt.contour to add contour lines
C = plt.contour(X,Y,f(X,Y),8,colors = 'black',linewidth = .5)

#adding label
plt.clabel(C,inline = True,fontsize = 10)

#ignore ticks
plt.xticks([])
plt.yticks([])

plt.show()


# -------------------------------网格图-------------------------------
#image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)



# for the value of "interpolation"，check this:
# http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
# for the value of "origin"= ['upper', 'lower'], check this:
# http://matplotlib.org/examples/pylab_examples/image_origin.html

#显示图像
#这里的cmap='bone'等价于plt.cm.bone
plt.imshow(a,interpolation = 'nearest',cmap = 'bone')# ,origin = 'up')  运行的之后这里报错了，所以先放在这里
#显示右边的栏
plt.colorbar(shrink = .92)

#ignore ticks
plt.xticks([])
plt.yticks([])

plt.show()



# ----------------------------------------3D图--------------------------------
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
#X Y value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
#hight value
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
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
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
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
ax.set_zlim(-2, 2)
plt.show()