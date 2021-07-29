import matplotlib.pyplot as plt
import matplotlib as mpl

# 下面两句是 支持中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 如何一次命令画多张图（不是子图）
plt.figure()
plt.plot(x,y1)
plt.figure()
plt.plot(x,y2)
plt.show()
