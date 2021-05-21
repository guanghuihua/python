#-------------np.where()的一些用法
#np.where(condition,a,b)  -->如果条件是真的，那么就是a,否则就是b
import numpy as np
X = np.arange(9).reshape(3,3)
Y = np.ones((3,3))
print(np.where(X > 5,X,Y))

print(np.where([[True,False],[True,True]],[[1,2],[3,4]],[[5,6],[7,8]]))
