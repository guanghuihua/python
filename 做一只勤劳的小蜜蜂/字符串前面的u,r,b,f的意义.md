```python
### 字符串前面加上4个字母u,r,b,f的含义
# 加u     后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
# 加r     去掉反斜杠的转移机制。
# 加b     b" "前缀表示：后面字符串是bytes 类型。
# 加f     以 f开头表示在字符串内支持大括号内的python 表达式

u"我是含有中文字符组成的字符串。"
# >>> '我是含有中文字符组成的字符串。'

print(r'\n \n \n \n')  # 表示一个普通生字符串 \n\n\n\n，而不表示换行了
# >>> \n \n \n \n

response = b'<h1>Hello World!</h1>'   # b' ' 表示这是一个 bytes 对象
print(response)
# >>> b'<h1>Hello World!</h1>'

#在 Python3 中，bytes 和 str 的互相转换方式是
print(str.encode('utf-8'))
print(bytes.decode(b'utf-8'))
# >>> b'utf-8'
# >>> utf-8

import time
t0 = time.time()
time.sleep(1)
name = 'processing'
# 以 f开头表示在字符串内支持大括号内的python 表达式
print(f'{name} done in {time.time() - t0:.2f} s') 

# >>> processing done in 1.02 s

```