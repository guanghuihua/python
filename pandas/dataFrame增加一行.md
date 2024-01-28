# DataFrame三种方法添加一行

```
主要是三种方法
df.loc[len(df)] = ...
df.append(...)
pd.concat(df,...)
需要注意的是，如果添加的是DataFrame，那就要考虑index是否匹配的问题，否则容易出现 '交错添加'的问题
```
转载自[博客](https://shenzq.com/how-to-add-row-to-pandas-dataframe.html)


`concat`, `df.lo` 都可以往 Pandas DataFrame 中添加行，但它们都存在性能的问题。本文在介绍前两种方法的基础上，着重介绍一种高性能的做法。

假设我们有这样一个 DataFrame

```
   seq
0    1
1    2
2    3
```

创建这个 DataFrame 的代码如下

`df = pd.DataFrame({"seq":[1,2,3]})`
这个 DataFrame 有3个元素，现在我们要往里面添加第4个元素，值为4。

用 `concat` 添加的方法如下
```python
df2 = pd.DataFrame({"seq":[4]})
df = pd.concat([df, df2], ignore_index=True)
```
我们打印 df, 会发现它变成了这样
```
   seq
0    1
1    2
2    3
3    4
```
最下面这一行就是我们刚刚添加的行。

另一种往 DataFrame 添加行的方法，是用 `df.loc `添加行，具体如下
```python
df = pd.DataFrame({"seq":[1,2,3]})
df.loc[len(df)] ={"seq": 4}
```
我们打印一下 df，会发现 df 变成了
```
   seq
0    1
1    2
2    3
3    4
```
和上面的结果一模一样。

看上去 `concat` 和 `df.loc` 都可以往 DataFrame 里添加行，那它们的性能怎么样呢？

下面我们就来测试一下。

我们分别用 `concat` 和` df.loc` 来构建一个10000行的 DataFrame。这个 DataFrame 长下面这样
```
       seq
0        0
1        1
2        2
3        3
4        4
...    ...
9995  9995
9996  9996
9997  9997
9998  9998
9999  9999

[10000 rows x 1 columns]
```
我们用添加行的方式来构造这样一个 DataFrame，并测试使用 `concat` 和 `df.loc` 各需要多少时间。

`concat` 性能
我们从空的 DataFrame 开始，用` concat `每次往里面添加一行，代码如下
```pyhton
import pandas as pd
import time

row_num = 10000
start = time.perf_counter()
df = pd.DataFrame({"seq": []})
for i in range(row_num):
    df1 = pd.DataFrame({"seq": [i]})
    df = pd.concat([df, df1])
end = time.perf_counter()
print("elapsed time: {}".format(end-start))
```
上面的代码使用` time.perf_counter()` 记录了程序开始的时间和结束时间，两者的差就是程序运行的时间。

运行上面的程序会输出

`elapsed time: 3.3971026440000003`


`df.loc `性能
同样的，我们测试一下` df.loc `添加行的性能
```pyhton
start = time.perf_counter()
df = pd.DataFrame({"seq": []})
for i in range(row_num):
    df.loc[i] = i
end = time.perf_counter()
print("elapsed time: {}".format(end-start))
```
运行上面的程序输出

`elapsed time: 8.133717991`
可以看到，无论是` concat `还是` df.loc `，性能都不高，都要花费数秒的时间。

那有没有性能高的做法呢？答案是有的。下面我们来介绍第三种方法，也是推荐的做法。

推荐的做法
这种方法是先把每一行的内容存成字典，把所有的字典添加到一个列表中，然后使用这个列表创建 df，代码如下
```python
start = time.perf_counter()
rows = []
for i in range(row_num):
    rows.append({"seq": i})
df = pd.DataFrame(rows)
end = time.perf_counter()
print("elapsed time: {}".format(end-start))
```
运行程序输出

`elapsed time: 0.007482828000000552`
可以看到，这种做法的性能比` concat` 提升了几百倍，比` df.loc 更是提升了千倍以上。
