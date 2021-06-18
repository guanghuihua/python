# 1. 一个for循环的一个非常好用的例子

示例如下：
```python
for _ in range(10):
    print("Hello world!")
```

# 2. Python中变量名后面加冒号， 函数后面加箭头

```python
def f(text:str,max_len:'int>0'=80) ->str:
    return True
```

函数声明中，`text:str`  
text 是参数 : 冒号后面  str是参数的注释。  
如果参数有默认值，还要给注释`max_len:'int>0'=80`

`->str` 是函数返回值的注释。

这些注释信息都是函数的元信息，保存在`f.__annotations__`字典中   
**需要注意，python对注释信息和f.__annotations__的一致性，不做检查
不做检查，不做强制，不做验证！什么都不做。**   
一个例子：
```python
def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("函数注释", f.__annotations__)
    print("参数值打印", ham, eggs)
    print(type(ham),type(eggs))

f("www")

# >>> 函数注释 {'ham': 42, 'eggs': <class 'int'>, 'return': 'Nothing to see here'}
# >>> 参数值打印 www spam
# >>> <class 'str'> <class 'str'>

```
解释说明：

注释的一般规则是参数名后跟一个冒号（：），然后再跟一个expression，这个expression可以是任何形式。

返回值的形式是 -> int，annotation可被保存为函数的attributes。

        注释的一般规则是参数名后跟一个冒号（：），然后再跟一个expression，这个expression可以是任何形式。   
        返回值的形式是 -> int，annotation可被保存为函数的attributes。

以上属于静态注释，还有一种方法叫做动态注释  
动态注释的原理，就是在函数中或者装饰器中动态的增加 删除 更改 注释内容    
f.__annotations__是一个字典，可以使用字典的所有操作，这样就可以动态的更改注释了  

# 3. 多行注释竟然后帮助文档的作用

python中使用三个引号作为多行注释，这个竟然会在help()是显示以起到多行注释的作用

# 4. python中 # %% 的作用

很神奇的一件事情就是在 .py 文件中使用
`# %% `可以产生像是jupter中框的作用一样，而其后可以直接调用Jupter也可以直接进行debug  
感觉非常方便

# 5. 序列解包

使用序列解包可以用非常简洁的方法完成复杂的功能。增强代码的可读性，减少代码量。

```python

>>> a, b, c = 1, 2, 3
>>> a
1
>>> b
2
>>> c
3

>>> a, b, *c = 0, 1, 2, 3
>>> a
0
>>> b
1
>>> c
[2, 3]


>>> a, b, *c = 0, 1
>>> a
0
>>> b
1
>>> c
[]

# 嵌套解包

>>> (a, b), (c, d) = (1, 2), (3, 4)

>>> a, b, c, d
(1, 2, 3, 4)
```

更有用的是在输入的时候，联合eval的`将字符串当成有效的表达式来求值并返回计算结果 `  
`input()`返回的是字符串，利用`eval()`函数可以完成多个输入赋值  
```python
x,y = eval(input("请输入两个数字，以逗号分隔："))

# 输出为
请输入两个数字，以逗号分隔：1,2
>>> x
1
>>> y
2
```