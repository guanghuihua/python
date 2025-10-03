# Some tricks in python

1. `# %%` python interactive window
[Jupyter code cells](https://code.visualstudio.com/docs/python/jupyter-support-py)

2. 在 Python 函数定义里，参数列表后面的 -> 用来标注“返回值类型”或更泛化的描述（函数注解的一部分），语法是：

    ```python
    def func(x: int) -> str:
        ...
    ```

    这里 `-> str` 表示这个函数按约定返回一个字符串。它只是类型提示，不会强制类型检查，但配合 IDE、静态分析工具、mypy 等可以提升可读性和可靠性。

3. syntactic sugar
4. magic method
