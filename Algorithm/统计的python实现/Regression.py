'''
导入statsmodels模块主要是解决线性回归问题，具体可以分为以下若干步骤
1. 导入statmodels的子模块api
2. 导入相关的因变量（被解释变量）、自变量（解释变量）的数据外，还要对自变量的数据增加一列常数项；
3. 构建相关的线性回归模型，这一步可以根据需要运用不同的线性回归模型
4. 用fit函数生成一个线性回归的结果对象，结果对象包含了回归模型的结果参数和模型诊断信息

不同的线性回归模型：
OLS -> 普通最小二乘回归
GLS -> 广义最小二乘回归
WLS -> 加权最小二乘回归
GLASAR  -> 带有自相关误差模型的广义最小二乘回归
GLM  -> 广义线性模型
RLM -> 使用M个估计量的鲁棒线性模型
mixed  -> 混合效应模型
gam  -> 广义加性模型

'''


import numpy as np
import pandas as pd
import scipy as sci
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
import statsmodels.api as sm  # 导入回归的api模块

#导入数据
df = pd.read_csv(r"D:\大三上\回归\mtcars.csv")  
X = df['mpg']
Y = df['disp']

# 对自变量的数据增加一列常数项
X_addcons = sm.add_constant(X)

# 模型训练，此处使用普通最小二乘回归模型
model = sm.OLS(endog=Y, exog=X_addcons)
result = model.fit()  # 生成一个线性回归的结果对象

plt.figure(figsize=(9,6))
plt.scatter(X,Y,c="b",marker="o")
# 生成一条拟合直线
plt.plot(X, result.params[0]+result.params[1]*X,'r-',lw=2.5)
plt.xticks(fontsize=14)
plt.xlabel("mpg")
plt.yticks(fontsize=14)
plt.ylabel("disp")
plt.title("mpg和disp的最小二乘回归")
plt.grid()
plt.show()