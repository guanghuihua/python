# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 随机初始化参数
np.random.seed(0)
W1 = np.random.randn(2, 3)  # 输入层到隐藏层的权重
b1 = np.random.randn(3)     # 隐藏层的偏置
W2 = np.random.randn(3, 1)  # 隐藏层到输出层的权重
b2 = np.random.randn(1)     # 输出层的偏置

# 输入数据
X = np.array([[1.0, 2.0]])  # 一批大小为1的输入数据
y_true = np.array([[0.0]])  # 目标数据

# 定义学习率
learning_rate = 0.01

# 存储损失值的列表
losses = []

# 迭代优化
for epoch in range(1000):
    # 前向传播
    z1 = np.dot(X, W1) + b1    # 隐藏层输入
    a1 = np.maximum(0, z1)     # ReLU 激活函数
    z2 = np.dot(a1, W2) + b2   # 输出层输入
    y_pred = z2                # 没有激活函数，因为这里假设的是线性回归问题

    # 计算损失
    loss = np.mean((y_pred - y_true) ** 2)  # 均方误差损失函数
    losses.append(loss)  # 将损失值添加到列表中
    
    # 反向传播
    # dL/dz2
    grad_z2 = 2 * (y_pred - y_true) / len(X)  # 损失对输出层输入的梯度
    # dL/dW2
    grad_W2 = np.dot(a1.T, grad_z2)           # 损失对隐藏层到输出层权重的梯度
    # dL/db2
    grad_b2 = np.sum(grad_z2, axis=0)         # 损失对输出层偏置的梯度
    # dL/da1
    grad_a1 = np.dot(grad_z2, W2.T)           # 损失对隐藏层输出的梯度
    # dL/dz1
    grad_z1 = grad_a1 * (z1 > 0)              # 损失对隐藏层输入的梯度
    # dL/dW1
    grad_W1 = np.dot(X.T, grad_z1)            # 损失对输入层到隐藏层权重的梯度
    # dL/db1
    grad_b1 = np.sum(grad_z1, axis=0)         # 损失对隐藏层偏置的梯度

    # 更新参数
    W1 -= learning_rate * grad_W1
    b1 -= learning_rate * grad_b1
    W2 -= learning_rate * grad_W2
    b2 -= learning_rate * grad_b2

    # 打印损失
    if epoch % 100 == 0:
        print(f'Epoch {epoch}: Loss {loss}')

# 绘制损失曲线
plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.show()

# 打印最终的参数值
print('Final parameters:')
print('W1:', W1)
print('b1:', b1)
print('W2:', W2)
print('b2:', b2)


