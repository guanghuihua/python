# maketrans()方法生成字符映射表，
# translate()方法是根据字符映射表替换字符。
# 这两种方法联合起来使用可以一次替换多个字符。
t = ''.maketrans('@#$','nmd')
s = "我们都有@#$光明的未来"
s.translate(t)

