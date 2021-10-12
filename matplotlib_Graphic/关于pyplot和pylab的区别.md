### 关于pyplot和pylab的区别

**区别：**

Pyplot：“方便快速绘图matplotlib通过pyplot模块提供了一套和MATLAB类似的绘图API，将众多绘图对象所构成的复杂结构隐藏在这套API内部。”

pylab：“matplotlib还提供了一个名为pylab的模块，其中包括了许多NumPy和pyplot模块中常用的函数，方便用户快速进行计算和绘图，十分适合在IPython交互式环境中使用。”

**作用：**
pylab = pyplot+大部分numpy。
也就是说pylab只是提供了一个方便的导入常用包的接口。

**使用场景：**
pyplot：是因为这样可以很好地与ipython（jyupter notebook，spyder）实现很好的交互模式，既可以画图又可以进行简单的计算，使用前不需要再导入别的包，高度类似于MATLAB。

pylab：正常编程使用，因为pyplot相比pylab更加纯粹，避免开始导入不必要的包，增加程序的冗余度。

即：

```python
import matplotlib.pyplot as plt
import numpy as np

x = range(30)
y = np.sqrt(x)
plt.plot(x,y)
plt.show()
```


等同于

```python
import pylab

x = range(30)
y = pylab.sqrt(x)
pylab.plot(x,y)
pylab.show()
```




