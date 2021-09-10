# python画图的一些参数

[画图的链接](https://zhuanlan.zhihu.com/p/33270402)

## 首先是点的问题

不要总是使用list，list不方便进行科学计算，而且运算速度相对于numpy还慢，下面是几个经常用到的numpy中的数据类型
还是很有用的

```python
x = np.linspace(0,1,5)
x1 = np.matrix([[1,2],[3,4]])
x2 = np.mat([[1,2],[3,4]])
y1,y2 = np.meshgrid(x,x)  # 相当于 向量的 笛卡尔乘积，非常有用
```

## Matplotlib的简介

是一个python的 2D绘图库，它以各种硬拷贝格式和跨平台的交互

## plt的参数的介绍

linewidth  线条宽度
linestyle  线条的类型
color      颜色

## 1. Figure对象

在matplotlib中，整个图表为一个figure对象。其实对于每一个弹出的小窗口就是一个Figure对象，那么如何在一个代码中创建多个Figure对象，也就是多个小窗口呢？

下面的这个代码生成一个空白画布
```python
import matplotlib.pyplot as plt
plt.figure()
plt.show()
```

```python
x = np.linspace(-1,1,50)
y1 = x ** 2 
y2 = x * 2
#这个是第一个figure对象,下面的内容都会在第一个figure中显示
plt.figure()
plt.plot(x,y1)
#这里第二个figure对象
plt.figure(num = 3,figsize = (10,5))
plt.plot(x,y2)
plt.show()
```

这里需要注意的是：我们看上面的每个图像的窗口，可以看出figure并没有从1开始然后到2，这是因为我们在创建第二个figure对象的时候，指定了一个num = 3的参数，所以第二个窗口标题上显示的figure3。对于每一个窗口，我们也可以对他们分别去指定窗口的大小。也就是figsize参数。若我们想让他们的线有所区别，我们可以用下面语句进行修改

`plt.plot(x,y2,color = 'red',linewidth = 3.0,linestyle = '--')`

## 2. 设置坐标轴

### 在图表上设置x,y轴的取值范围

```python
plt.ylim((0,2))
plt.xlim((-2,2))
```

### 给横纵坐标设置名称：

```python
plt.xlabel("x'slabel")#x轴上的名字
plt.ylabel("y's;abel")#y轴上的名字
```

### 给坐标轴换单位
```python
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
#在对应坐标处更换名称
plt.yticks([-2,-1,0,1,2],['really bad','b','c','d','good'])
```

#### 那么如果我想把坐标轴上的字体更改成数学的那种形式：

```python
#在对应坐标处更换名称
plt.yticks([-2,-1,0,1,2],[r'$really\ bad$',r'$b$',r'$c\ \alpha$','d','good'])
```

+ 但是注意：我们如果要使用空格的话需要进行对空格的转义"\ "这种转义才能输出空格

### 更换坐标原点，坐标轴

```python

#gca = 'get current axis'
#获取当前的这四个轴
ax = plt.gca()
#设置脊梁(也就是包围在图标四周的默认黑线)
#所以设置脊梁的时候，一共有四个方位
ax.spines['right'].set_color('r')
ax.spines['top'].set_color('none')

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

```

### 设置次坐标轴

设置的时候需要注意**使用twiny是添加x轴的坐标轴**
```python
# 使用twiny是添加x轴的坐标轴
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y1 = 0.05 * x ** 2
y2 = -1 * y1

fig,ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data',color = 'g')
ax2.set_ylabel('Y2 data',color = 'b')

plt.show()
```

## 4. 设置图例

+ 如果我们没有在legend方法的参数中设置labels，那么就会使用画线的时候，也就是plot方法中的指定的label参数所指定的名称，当然如果都没有的话就会抛出异常；
+ 其实我们plt.plot的时候返回的是一个`线的对象`，如果我们想在handle中使用这个对象，就必须在返回的名字的后面加一个","号；

+ 如果一张图中有多条曲线，我们如何对它们添加图例呢
下面是两种方法，均可，但是别忘了添加`,`

```python
# 第一种方法
l1, = plt.plot(x, y1, label='linear line') # 把label设置为plt.plot()的参数
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
plt.legend(loc = 'upper right')
plt.show()


# 第二种方法
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
plt.legend(handles = [l1,l2],labels = ['up','down'],loc = 'best')  # 注意labels和曲线的对应，和 逗号 的使用
#the ',' is very important in here l1, = plt...and l2, = plt...for this step

```


对图例的样式进行更改
```python
legend = plt.legend(handles = [l1,l2],labels = ['hu','tang'],loc = 'upper center',shadow = True)
# 添加阴影，
frame = legend.get_frame()
frame.set_facecolor('r')  #设置图例阴影的颜色

```

下面是图例的一些常用的参数的设置

```python
"""legend( handles=(line1, line2, line3),
           labels=('label1', 'label2', 'label3'),
           'upper right')
    shadow = True 设置图例是否有阴影
    The *loc* location codes are::
          'best' : 0,         
          'upper right'  : 1,
          'upper left'   : 2,
          'lower left'   : 3,
          'lower right'  : 4,
          'right'        : 5,
          'center left'  : 6,
          'center right' : 7,
          'lower center' : 8,
          'upper center' : 9,
          'center'       : 10,"""
```

## 5. 如何在图形中添加注释annoation

```python
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

#-----------------------以上是要画的图形，下面介绍两种添加注释的方法----------------------


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

```

###  下面对方式一进行注释
  
```python
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
```

+ xy就是需要进行注释的点的横纵坐标；
+ xycoords = 'data'说明的是要注释点的xy的坐标是以横纵坐标轴为基准的；
+ xytext=(+30,-30)和textcoords='data'说明了这里的文字是基于标注的点的x坐标的偏移+30以及标注点y坐标-30位置，就是我们要进行注释文字的位置；
+ fontsize = 16就说明字体的大小；
+ arrowprops = dict()这个是对于这个箭头的描述，arrowstyle='->'这个是箭头的类型，connectionstyle="arc3,rad=.2"这两个是描述我们的箭头的弧度以及角度的。

### 对方式二进行注释

```python
plt.text(-3.7,3,r'$this\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})

```

## 6. 图形遮挡问题

```python

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

plt.show()
```

这个图画出来，注意图中二次函数把一次函数给遮挡住了，可以看出按照图形的逻辑，是先画出来第一张图然后画出第二张图，所以有遮挡，其中 `zorder`控制着遮挡顺序
```python
#zorder控制绘图顺序
plt.plot(x,y1,linewidth = 10,zorder = 1,label = r'$y_1\ =\ 0.1*x$')
plt.plot(x,y2,linewidth = 10,zorder = 2,label = r'$y_2\ =\ x^{2}$')
```

这张图画出来，还有一个问题，就是图还把坐标轴给挡住了，通过一些修改可以突出坐标轴问题

```python

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor = 'white',edgecolor='none',alpha = 0.8,zorder = 2))

```
+ ax.get_xticklabels()获取得到就是坐标轴上的数字；
+ set_bbox()这个bbox就是那坐标轴上的数字的那一小块区域，从结果我们可以很明显的看出来；
+ facecolor = 'white',edgecolor='none，第一个参数表示的这个box的前面的背景，边上的颜色。
