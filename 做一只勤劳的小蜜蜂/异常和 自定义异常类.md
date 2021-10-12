# 异常（异常是python对象） 和 自定义异常类

Python提供了**异常**和**断言**来处理程序在运行过程中出现的异常和错误  

## 什么是异常？

分清楚程序发生异常和程序执行错误，它们完全是两码事， 
程序由于错误导致的运行异常，是需要程序员想办法解决的； 
但还有一些异常，是程序正常运行的结果，比如用 raise 手动引发的异常。
异常是在程序执行过程中发生的影响程序正常执行的一个事件。 
当Python检测到一个错误时，解释器就会指出当前流已无法继续执行下去，这时候就出现了异常。
**异常是指因为程序出错而在正常控制流以外采取的行为。 ** 
（原来异常的设计是一个有用的东西，有了异常之后程序出错就会终止，而不会出现正常控制流以外采取的行动）

**异常是Python对象**，当Python无法正常处理程序时就会抛出一个异常。 
（看柳青老师ppt中有 `BaseException`是所有异常的基类，而`Exception`是常规错误的基类，所以python中的很多异常都是`BaseException`的派生类）

一旦Python脚本发生异常，程序需要捕获并处理它，否则程序会终止执行。 
异常处理使程序能够处理完异常后继续它的正常执行，不至于使程序因异常导致退出或崩溃。 
**语法错误和逻辑错误不属于异常**,但有些语法错误往往会导致异常，例如由于大小写拼写错误而访问不存在的对象。  

异常分为两个阶段：  

+ 第一个阶段是引起异常发生的错误；  
+ 第二个阶段是检测并处理阶段。 
  当程序出现错误，python会自动引发异常，也可以通过raise显式地引发异常。

## python中的标准异常

有很多种，具体可以百度或者上网盘看ppt

## 捕获与处理异常

    try:
    	<可能出现异常的语句块> 
    except <异常类名字name1>：
            <异常处理语句块1>   
        #如果在try部份引发了'name1'异常，执行这部分语句
    except <异常类名字name2>，<数据>:
            <异常处理语句块2>   
        #如果引发了'name2'异常，获得附加的数据
    …
    except:
        <异常处理语句块n>   
        #如果引发了异常，但与上述异常都不匹配，执行此语句块    ### 感觉这一条还是不太熟练
    else:
            <else语句块>
        #如果没有上述所列的异常发生，执行else语句块
    finally:
        <始终执行的语句块>

try/except语句用来检测try语句块中的异常，让except语句捕获异常信息并处理。 
如果不想在异常发生时结束程序，只需要在try里捕获它，并在except中处理捕获到的异常。 
try中的语句块先执行。 
如果try语句块中的某一语句执行时发生异常，Python就跳到except部分， 
从上到下判断抛出的异常对象是否与except后面的异常类相匹配，并执行第一个匹配该异常的except后面的语句块，异常处理完毕。 
如果异常发生了，但是没有找到匹配的异常类别，**则执行不带任何匹配类型的except语句后面的语句块**，异常处理完毕。  

示例代码  

```python
try:
    #正常执行的代码
    pass
except <错误1>:
    #抛出错误1时执行的代码
    pass
except <错误2>:
    #抛出错误2时执行的代码
    pass
except <错误3, 错误4>:
    #抛出错误3或者错误4时执行的代码
    pass
except Exception as result:
    print("未知错误类型：{}".format(result))
else:
    #没有异常才会执行的代码
    pass
finally:
    #无论是否有异常都会执行的代码
    print("程序结束")
```

## 异常的传递

当函数/方法执行出现异常会将异常传递给函数/方法的调用一方
如果传递到主程序，仍然没有异常处理程序才会被终止
注意：
**在开发中，可以在主函数中增加异常捕获，这样在主函数中调用的其他函数，只要出现异常，都会传递到主函数的异常捕获中
这样就不需要在代码中，增加大量的异常捕获能够保证代码的整洁**
示例

```python
def demo1():
    return int(input("请输入一个整数："))
 
 
def demo2():
    return demo1()
 
def main():
    try:
        print(demo2())
    except ValueError:
        print("请输入正确的整数")
    except Exception as result:
        print("未知错误 %s" % result)
 
main()
```

## 自定义异常类

仅仅使用标准模块中的异常类通常不能满足系统开发的需要
有时候需要自定义一些异常类
系统无法识别自定义的异常类，只能在程序中显式地使用raise抛出异常
可以通过扩展BaseException类或其子类来创建自定义异常类
`BaseException`是所有异常的基类

### raise的作用

raise 语句的基本语法格式为：
        

        raise [exceptionName [(reason)]]

其中，用 [] 括起来的为可选参数，其作用是指定抛出的异常名称，以及异常信息的相关描述。如果可选参数全部省略，则 raise 会把当前错误原样抛出；如果仅省略 (reason)，则在抛出异常时，将不附带任何的异常描述信息。   
也就是说，raise 语句有如下三种常用的用法：  

1. raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。  
2. raise 异常类名称：raise 后带一个异常类名称，表示引发执行类型的异常。  
3. raise 异常类名称(描述信息)：在引发指定类型的异常的同时，附带异常的描述信息。  

示例如下

```python
>>> raise
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    raise
RuntimeError: No active exception to reraise
>>> raise ZeroDivisionError
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    raise ZeroDivisionError
ZeroDivisionError
>>> raise ZeroDivisionError("除数不能为零")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    raise ZeroDivisionError("除数不能为零")
ZeroDivisionError: 除数不能为零
```

需要注意的是，就算是直接raise也会触发异常`RuntimeError`

### 理解异常是一个类

通过一个例子来体会

```python
>>> class ShortInputError(Exception):
...     def __init__ (self,length,atleast):
...         Exception.__init__(self)       
...         self.length = length
...         self.atleast = atleast
...
>>> try:
...     s = "123456"
...     if len(s) <10:
...         raise ShortInputError(len(s),10)
... except ShortInputError as result:
...     print("长度至少是{}".format(result.atleast))
... else:
...     print("没有异常")
...
长度至少是10
```

从这个例子很容易看出来，其中ShortInputError是一个派生类，基类是Exception，在这个例子中，如果s的长度小于10，就会抛出ShortInputError，然后异常就会被try捕获，然后通过except匹配，如果匹配上的话，输出带有具体信息的异常


## 断言与上下文管理

断言与上下文管理是两种比较特殊的异常处理方式，在形式上比异常处理结构要简单一些。 
断言是申明表达式为真的判定。如果表达式为假则抛出异常。 
断言语句可以理解为raise-if-not语句，用来测试表示式，如果返回值为假，则触发异常。 
如果断言成功，则程序不采取任何措施，否则触发AssertionError异常。 
断言的语法格式如下：
	assert expression [, arguments]


注意一下三条命令就可以明白`assert`的作用

```python
>>> assert 1+1 ==2
>>> assert 1+1 !=2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> assert 1+1 !=2,"错误"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: 错误
```

