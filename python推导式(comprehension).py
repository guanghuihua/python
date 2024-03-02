# 推导式

# 1. zip()函数
## 功能： 将多个迭代器Iterator对象 或者可迭代对象中的元素压缩在一起，返回一个zip对象
## zip对象既是一个可迭代对象也是一个迭代器对象

names = ["Tony", "Tom", "Gray", "Lisa"]
grades = [11,22,31,21]
chart1 = zip(names, grades)
print(list(chart1))

chart2 = zip(enumerate(grades), names)
print(list(chart2))

chart3 = zip(range(3), names)
print(list(chart3))

chart4 = zip(names)
print(list(chart4))


# 字典方法
## setdefault() 
## 如果字典中包含参数key对应的键，则返回该键对应的值；否则以参数key的值为键，以参数default的值为该键对应的值，在字典中插入键-值对元素，并返回该元素的值部分。

abbrevation = {'WAN':"Wide Area Network", 'CU':"Control Unit", 'LAN':"Local Area Netword"}
print(abbrevation.setdefault('CU'))

abbrevation.setdefault('FTP',"File Transfer Protocol")
print(abbrevation)


abbrevation.setdefault('cu')
print(abbrevation)

## update()
## update()方法将另一个字典中的所有键值对一次性地添加到当前字典中，如果两个字典中存在有相同的键，则以另一个字典中的值更新当前字典。

abbrevation = {'WAN':"Wide Area Network", 'CU':"Control Unit", 'LAN':"Local Area Netword"}
temp = {'CU':"Control unit", 'FTP':"File Transfer Protocal"}
abbrevation.update(temp)
print(abbrevation)

## get()方法
## get()方法返回指定键所对应的值，如果键不存在则返回默认值，默认值为None，也可以自己指定


abbrevation = {'WAN':"Wide Area Network", 'CU':"Control Unit", 'LAN':"Local Area Netword"}
print(abbrevation.get('WAN'))  # 返回键'WAN'对应的值 Wide Area

abbrevation.get('WAN',"键不存在")
temp = abbrevation.get('wan' )  # 如果键不存在，那么返回None
print(temp)

temp2 = abbrevation.get('wan','键不存在')  # 键'wan'不存在，返回第二个参数"键不存在"
print(temp2)

# 练习题
## 追加刘冰的成绩70，将张三、王五的成绩分别修改为50和48
## 查找所有高于平均分的同学姓名和成绩

grades = {"张三": 45, "李四": 78, "王五": 40, "周流": 96, "赵启": 65, "孙膑": 90, "郑宇": 78, "吴施": 99, "董勤": 60,"颖慧": 99}
grades.setdefault('刘冰',70) #添加刘冰同学成绩
grades.update({'王五':48,'张三':50})  # 成绩进行修改

mean = sum(grades.values())/len(grades.values())
print("The mean value is %f "%mean)
res = [(name,grade) for name,grade  in grades.items() if grades.get(name) > mean ]
print(res)


# 字典推导式和列表推导式 的使用方法类似，只不过将中括号变成大括号，并且需要两个表达式，一个生成键，一个生成值，两个表达式之间使用冒号分隔，最后生成的是字典
## 列表name存储若干人的名字
## name= ['Bob','Tom','Alice','Jerry','Wendy','Smith']
## 列表score在对应的位置上存储这些人的成绩
## score=[86,78,98,90,47,80]
## (1)以名字为键、成绩为值组成新字典grades_01并输出。
## (2)以名字为键、成绩为值组成新字典grades_02，新字典中的键值对只包含成绩80及以上的。
## (3)在上面生成的字典dd中挑出成绩及格的组成新字典grades_03并输出。

name= ['Bob','Tom','Alice','Jerry','Wendy','Smith']
scores=[86,78,98,90,47,80]
score_01 = {name:score for name,score in zip(name,scores)}
score_02 = {name:score for name,score in zip(name,scores) if score >= 80 }
print("成绩为80分及以上 \n ",score_02)
score_03 = {name:score for name,score in zip(name,scores) if score >= 60}
print("Pass:  \n ",score_03)

# 字典推导式
## 使用字典推导式进行双循环的时候遇到的问题
num = {i:j for i in range(5) for j in range(5)}
print(num)


# 上面字符推导式的原理和这个是一样的
num = {}
for i in range(5):
    for j in range(5):
        num[i] = j
print(num)

## 从键盘输入一个字符串，统计字符出现的次数
### string = input("请输入一句话：")
### letter_counts = {i:string.count(i) for i in string}
### for i in letter_counts:
###    print("字符 %c 出现了 %d"%(i,letter_counts(i)))

# 集合是一组对象的集合。
## 集合由各种类型的不可变对象组成，但任何元素之间没有任何顺序，并且元素都不重复。
## Python提供了集合类型set，用于表示大量无序元素的集合。

vehicle = {"car","ship","plane","bus","train"}
print("vehicle的数据类型是：",type(vehicle))
vehicle = set([ "car","ship","plane","bus","train"])
print("vehicle的数据类型是：",type(vehicle))

## 空的集合只能通过set()来创建，不能通过{}来创建，因为{}是用来创建空的字典

## 集合中不能有重复元素，所以可以根据集合来去重
vehicle = {"car","helicptor","bus","train","car","ship","plane","bus","train"}
print(vehicle)
print(type(vehicle))

## 集合、列表都有推导式，但是元组没有推导式
tempList = [i*2 for i in (1,2,3,4,5,1,3,4,3,1)]
print(tempList)
tempSet = {i*2 for i in (1,2,3,4,5,1,2,4,3,1)}
print(tempSet)

# 生成器推导式
## 生成器推导式用法与列表推导式类似，把列表推导式的方括号改成圆括号
## 与列表推导式最大的不同点就是生成器推导式的结果是一个生成器对象，类似于迭代器(Iterator)
## 生成器对象可以通过for循环或者__next__()方法、next()函数进行遍历，也可以转换为列表或元组，但是不支持使用下标访问元素，已经访问过的元素也不支持再次访问。
## 当所有元素访问结束之后，如果想再次访问就必须重新创建该生成器对象。

gen = (int(i/3) for i in range(10) if i%3 == 0)
type(gen)
print(gen)
list(gen)

gen = (int(i/3) for i in range(10) if i%3 == 0)
gen.__next__()
next(gen)
try:
    gen.__next__()
except:
    print("由于对于生成器已经访问过的元素也不支持再次访问，所以当所有元素访问结束之后，如果想再次访问就必须重新创建该生成器对象。")

gen = (int(i/3) for i in range(10) if i%3 == 0)
for i in gen:
    print(i,end = ' ')


# split()和map()函数的混合使用
m = input("请输入x,y: ")
print(m.split(","))
x,y = list(map(int,m.split(',')))
print(x,y)

# 序列解包 Sequence Unpacking 是python语言赋值语句的一种技巧和方法 
## 1. 多变量同时赋值
x,y,z = "a","b","c"
##这种方法并不限于列表和元组，而是适用于任意序列类型（甚至包括字符串和字节序列）。
## 只要赋值运算符左边的变量数目与序列中的元素数目相等，你都可以用这种方法将元素序列解包到另一组变量中。
a,b,c=(1,2,3)
print(a,b,c)
# 可以利用 * 表达式获取单个变量中的多个元素，只要它的解释没有歧义即可。
a,b,*c=(1,2,3,4,5,6,7)
print(a,b,c)
a,*b,c=(1,2,3,4,5,6,7)
print(a,b,c)
a,*b,c=1,2
print(a,b,c)   #如果左边变量比右边变量多，带*变量默认变为空值
(a,b),(c,d)=(1,2),(3,4)    #嵌套解包
print(a,b,c,d)

#实战
string='ABCDEFG'
b=string
for i in range(7):
    a,*b=b
    print(a,b)

x,y = eval(input("请输入两个数字，以逗号分隔："))

'''
输出为
请输入两个数字，以逗号分隔：1,2
>>> x
1
>>> y
2
'''