# magic methods（也称 “special methods” 或 “dunder 方法”）

---

## 一、什么是 Magic Method / Dunder 方法

* 在 Python 中，magic methods（特殊方法）是 **名称以双下划线开头又以双下划线结尾** 的方法（例如 `__init__`, `__add__` 等）。
* 它们被 Python 解释器在特定操作发生时**自动调用**，而不是由用户直接手动调用。
* 它们使得你的自定义类能够与 Python 的内建语法、运算符、内置函数、协议（如迭代、上下文管理等）无缝协作。
* 这些方法是 Python 对象模型（Data Model）的核心部分。([Real Python][1])

> 在社区中常把它们称为 “magic methods” 或 “dunder methods”（即 “double underscore” 的缩写）([TutorialsTeacher][2])

---

## 二、Magic Method 的角色与分类

下面是一些常见用途的分类 + 示例方法：

| 功能 / 场景      | Magic 方法                                                              | 作用 / 描述                                                                            |
| ------------ | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 对象构造 / 生命周期  | `__new__(cls, …)`                                                     | 在 `__init__` 之前调用，负责真正创建对象（尤其对不可变类型有用）([A Java geek][3])                           |
| 初始化          | `__init__(self, …)`                                                   | 初始化对象属性等，是最常用的构造方法                                                                 |
| 析构 / 清理      | `__del__(self)`                                                       | 对象销毁前的清理逻辑（不一定总能被调用）([A Java geek][3])                                             |
| 字符串 / 表示     | `__repr__`, `__str__`                                                 | 定义对象的“官方”表示与“可读”表示，用于 `repr(obj)` / `str(obj)` / `print(obj)` 等 ([Real Python][1]) |
| 算术 / 运算      | `__add__`, `__sub__`, `__mul__`, `__truediv__` 等                      | 支持使用 `+`, `-`, `*`, `/` 等运算符重载 ([GeeksforGeeks][4])                                |
| 比较 / 相等 / 排序 | `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ne__` 等                    | 定义对象如何进行 `==`, `<`, `<=` 等比较操作 ([FreeCodeCamp][5])                                 |
| 容器 / 序列 / 映射 | `__len__`, `__getitem__`, `__setitem__`, `__iter__`, `__next__`       | 定义对象如何支持下标、迭代、长度、切片等操作 ([Real Python][1])                                          |
| 可调用对象        | `__call__(self, *args, **kwargs)`                                     | 让对象实例像函数一样被调用（`obj(...)`）([rszalski.github.io][6])                                 |
| 上下文管理        | `__enter__(self)` / `__exit__(self, exc_type, exc_val, tb)`           | 支持 `with` 语句的资源管理机制 ([rszalski.github.io][6])                                      |
| 属性访问 / 拦截    | `__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`       | 控制读写删除属性时的行为拦截机制 ([Real Python][1])                                                |
| 元类 / 类定制     | `__init_subclass__`, `__new__`（在元类中），`__prepare__` 等                  | 用于定制类创建、类继承行为等（元编程）([Real Python][1])                                              |
| 其他 / 高级用途    | `__enter__`, `__exit__`、异步相关的 `__await__`, `__aiter__`, `__anext__` 等 | 根据场景（如异步、模式匹配、缓冲协议等）用于扩展行为 ([Real Python][1])                                      |

这些方法共同使得 Python 的语义更灵活、可扩展。

---

## 三、使用 Magic Method 的原则与建议

* **不要直接调用** 魔法方法。通常应让解释器在恰当的时候自动调用。比如，不要写 `obj.__add__(other)`，而写 `obj + other`。([Real Python][1])
* **确保语义一致性**：如果重载了 `__eq__`，通常也应重载 `__hash__`（以便对象在 set / dict 中能正确工作）。
* **避免命名冲突 / 自造 dunder 方法**：不要随意使用双下划线前后包围的方法名（除非确知是 Python 官方支持的方法），否则可能与未来版本冲突或行为不被识别。
* **性能考虑**：在高频调用场景中，重写的 magic 方法逻辑要尽量高效，因为这些调用可能比你以为的“隐式操作”更加频繁。
* **遵守语义预期**：例如 `__repr__` 应尽可能返回能够重建对象的字符串（或至少是明确的调试信息），不要滥用。

---

## 四、示例代码

下面几个示例展示常见 magic 方法的用法。

### 例 1：运算 + 对象表示

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)       # 输出: Point(4, 6)
```

### 例 2：使对象可调用（`__call__`）

```python
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, delta=1):
        self.count += delta
        return self.count

c = Counter()
print(c())    # 1
print(c(5))   # 6
```

### 例 3：实现上下文管理（`with`）

```python
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

with ManagedFile('test.txt', 'w') as f:
    f.write('Hello')
# 退出 with 块后，文件自动关闭
```

### 例 4：自定义可迭代对象

```python
class MyRange:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        val = self.i
        self.i += 1
        return val

for x in MyRange(5):
    print(x)
# 输出 0,1,2,3,4
```

---

## 五、视频资源

下面是一个不错的入门视频，帮助你直观理解 magic 方法：

[Python MAGIC METHODS are easy!](https://www.youtube.com/watch?v=NwjSP1_WEfE&utm_source=chatgpt.com)

---

[1]: https://realpython.com/python-magic-methods/?utm_source=chatgpt.com "Python's Magic Methods: Leverage Their Power in Your Classes"
[2]: https://www.tutorialsteacher.com/python/magic-methods-in-python?utm_source=chatgpt.com "Magic or Dunder Methods in Python - Tutorials Teacher"
[3]: https://blog.frankel.ch/python-magic-methods/1/?utm_source=chatgpt.com "Python \"magic\" methods - part 1 - A Java geek"
[4]: https://www.geeksforgeeks.org/dunder-magic-methods-python/?utm_source=chatgpt.com "Dunder or magic methods in Python - GeeksforGeeks"
[5]: https://www.freecodecamp.org/news/python-magic-methods-practical-guide/?utm_source=chatgpt.com "How Python Magic Methods Work: A Practical Guide - freeCodeCamp"
[6]: https://rszalski.github.io/magicmethods/?utm_source=chatgpt.com "A Guide to Python's Magic Methods « rafekettler.com"
