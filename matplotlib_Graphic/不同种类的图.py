# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


# 散点图
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
