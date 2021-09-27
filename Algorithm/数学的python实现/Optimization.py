#-*- coding:utf-8 -*-
# 《最优化：建模、算法与理论》 刘浩洋等 P23 1.4题

import numpy as np
import matplotlib.pyplot as plt
import pylab 
import scipy as sci 

# 定义函数序列
def fun(x:list)->int :  # 此处使用了注释， x: 和  -> 都是注释的作用，没有强制作用
    return pow(x[0],2) + pow(x[1],2)

# 定义点列
def series(k:int) -> np.array:
    return (1+pow(0.5,k))*np.array([np.sin(k),np.cos(k)])

def seriesplot(k):
    X_k = list(map(series,range(1,k+1)))
    Y = []
    for i in range(len(X_k)):
        Y.append(X_k[i][1])
    pylab.plot([i+1 for i in range(k)],Y)
    plt.scatter([i+1 for i in range(k)],Y,s=15,c="orange",alpha=0.8)
    plt.show()
    # pylab.plot([i for i in range(k)],list(map(series,range(k))))



def f(k):
    X = [i+1 for i in range(k)]
    Y = []
    for i in range(k):
        Y.append(fun(series(i+1)))
    pylab.plot(X, Y)
    plt.scatter(X,Y,s=10,alpha=0.8)
    plt.xlabel("k")
    plt.ylabel("f(x^k)")
    plt.show()

# 使用匿名函数lambda+map的组合能够减少代码量
g = lambda x : pow(0.5,x)+1
ff = lambda x : np.sin(x)*(pow(0.5,x)+1)

if __name__ == "__main__":
    # print(list(map(fun,[[1,23]])))
    # seriesplot(300)
    plt.plot([i for i in range(100)],list(map(g,[i+1 for i in range(100)])))
    plt.plot([i for i in range(100)],list(map(ff,[i+1 for i in range(100)])),c="red")
    plt.scatter([i for i in range(100)],list(map(ff,[i+1 for i in range(100)])),c="red")
    plt.show()