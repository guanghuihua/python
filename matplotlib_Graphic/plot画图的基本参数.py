# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

# 下面两句是 支持中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 关于取点，不要还是用list，使用numpy，后面进行向量运算什么的更方便，而且计算也更快
x = np.linspace(0,1,5)
x1 = np.matrix([[1,2],[3,4]])
x2 = np.mat([[1,2],[3,4]])
y1,y2 = np.meshgrid(x,x)  # 相当于 向量的 笛卡尔乘积，非常有用


# -----------------------如何一次出现多个窗口--------------------

# 在matplotlib中，整个图表为一个figure对象。
# 其实对于每一个弹出的小窗口就是一个Figure对象，那么如何在一个代码中创建多个Figure对象，也就是多个小窗口呢？
x = np.linspace(-1,1,50)
y1 = x ** 2 
y2 = x * 2
#这个是第一个figure对象,下面的内容都会在第一个figure中显示
plt.figure()
plt.plot(x,y1)
#这里第二个figure对象
plt.figure(num = 3,figsize = (10,5))
plt.plot(x,y2,color = 'red',linewidth = 3.0,linestyle = '--')
plt.show()



# -----------------------对坐标轴进行设置--------------------
x = np.linspace(-1,1,50)
y = x *2
y1 = x **2

# 更改x,y的取值范围
plt.xlim((0,2))
plt.ylim((-2,2))

# 设置坐标轴名称
plt.xlabel("x'slabel")#x轴上的名字
plt.ylabel("y's;abel")#y轴上的名字

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
#在对应坐标处更换名称
# plt.yticks([-2,-1,0,1,2],['really bad','b','c','d','good'])
plt.yticks([-2,-1,0,1,2],[r'$really\ bad$',r'$b$',r'$c\ \alpha$','d','good'])

## 更改坐标原点的位置
#gca = 'get current axis'
#获取当前的这四个轴
ax = plt.gca()
#设置脊梁(也就是包围在图标四周的默认黑线)
#所以设置脊梁的时候，一共有四个方位
ax.spines['right'].set_color('r')
ax.spines['top'].set_color('none')  # 在这个例子中，坐标轴使用的是'bottom'和'left'的轴，对'top'设置为无色，而'right'设置为红色显示这条命令的作用

#将底部脊梁作为x轴
ax.xaxis.set_ticks_position('bottom')
#ACCEPTS:['top' | 'bottom' | 'both'|'default'|'none']

#设置x轴的位置(设置底的时候依据的是y轴)
ax.spines['bottom'].set_position(('data',0))
#the 1st is in 'outward' |'axes' | 'data'
#axes : precentage of y axis
#data : depend on y data

ax.yaxis.set_ticks_position('left')
# #ACCEPTS:['top' | 'bottom' | 'both'|'default'|'none']

#设置左脊梁(y轴)依据的是x轴的0位置
ax.spines['left'].set_position(('data',0))

plt.plot(x,y,color='green',linewidth = 3)
plt.plot(x,y1,color='red',linestyle = "--")
plt.show()

# -----------------------对坐标轴进行设置--------------------
# 图例简单的使用
x = np.linspace(-1,1,50)
y1 = x ** 2 
y2 = x * 2
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
plt.legend(loc = 'upper right')  #简单的设置legend(设置位置)，位置在右上角
plt.show()


l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')

plt.legend(handles = [l1,l2],labels = ['up','down'],loc = 'best')
legend = plt.legend(handles = [l1,l2],labels = ['hu','tang'],loc = 'upper center',shadow = True)
frame = legend.get_frame()
frame.set_facecolor('r')#或者0.9...
plt.show()


# -----------------------在图形上添加注释--------------------


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 2*x + 1

plt.figure(num = 1,figsize =(8,5))
plt.plot(x,y,c="r")

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#将底下的作为x轴
ax.xaxis.set_ticks_position('bottom')
#并且data，以y轴的数据为基本
ax.spines['bottom'].set_position(('data',0))

#将左边的作为y轴
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

print("-----方式一-----")
x0 = 1
y0 = 2*x0 + 1
plt.plot([x0,x0],[0,y0],'k--',linewidth = 2.5)
plt.scatter([x0],[y0],s = 50,color='b')
plt.annotate(r'$2x+1 = %s$'% y0,
            xy = (x0,y0),
            xycoords = 'data',
            xytext=(+30,-30),
            textcoords = 'offset points',
            fontsize = 16,
            arrowprops = dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))

print("-----方式二-----")
plt.text(-3.7,3,r'$this\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})

plt.show()



# -----------------------解决图形遮挡问题--------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 0.1*x
y2 = x**2

plt.figure()
#zorder控制绘图顺序
plt.plot(x,y1,linewidth = 10,zorder = 1,label = r'$y_1\ =\ 0.1*x$')
plt.plot(x,y2,linewidth = 10,zorder = 2,label = r'$y_2\ =\ x^{2}$')

plt.ylim(-2,2)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor = 'white',edgecolor='none',alpha = 0.8,zorder = 2))

# <a list of 9 Text xticklabel objects>
# <a list of 9 Text yticklabel objects>

plt.show()

