import numpy as np
import pandas as pd

# pandas数据结构有两种Series&DataFrame
mySeries = pd.Series([3,-5,7,4],index=['a','b','c','d'])
data = {'Letters':['A','B','C'],'Numbers':['1','2','3'],'Names':['Lucy','Candy','Tom']}
datas = pd.DataFrame(data,columns=['Letters','Numbers','Names'],index=["One","Two","Three"])
print(datas)

# pandas读取数据
## 读取csv文件
pd.read_csv("data.csv")
## 读取excel文件
pd.read_excel("data.xls",sheet_name="Sheet1")
pd.DataFrame(data)

## 其他的读取什么json,sql,table,html等都是一样的，都是read_type

# 数据储存
df.to_csv(filename)
df.to_excel(filename)
df.to_sql(table_name,connection_object)

# 创建测试对象
pd.DataFrame(np.random.rand(20,5))


# 统计数据函数
df.info()
df.shape()
df.index()
df.columns()
df.count()
df.sum()
df.cumsum()
df.min()
df.max()
df.idxmin()
df.idxmax()
df.describe()
df.mean()
df.median()
df.quantile([0.25,0.75])
df.var()
df.std()
df.cummax()
df.cummin()
df['columnName'].cumproad()  #计算数据的累积结果

len(df)
df.isnull
df.corr()  #该函数返回列之间的相关系数



# pandas 中的选择和过滤
mySeries['columnName']
df[n:N]  # 返回第n行到N-1行的数据，类型是DataFrame

# loc应该是locate（定位）的缩写，不同的是loc是使用label（df的index）定位，而iloc是使用坐标定位
df.iloc[[m],[n]]   #返回第m行第n列的数据
df.loc[m:n]  

df['columnName'] or df.columnName
df['columnName'][n]
df['columnName'].nunique()
df['columnName'].unique()
df['columnName'].value_counts()
df.head(n)
df.tail(n)
df.sample(n)
df.sample(frac=a)  #该函数采样数据框的a倍行数据框 a in [0,1]
df.nlargest(n,'columnName') # 返回最大的前n行数据框
df[df.columnName <  n]

df[['columnName1','columnName2']]
df.loc[m:n,'columnName1':'columnName2']  #该函数返回columnName1到columnName2之间的m：n行的数据框

## 按照条件筛选
### 创建过滤条件筛选
filters = df.columnsName > "2021-7-21"
df[fileters]
### 多条件筛选
df[np.logical_and(df['columnsName1']>123,df['columnsName2']>'2021-7-21')]
#==也可以使用下面这种方法
df[df['columnsName1']>123 & df['columnsName2']>'2021-7-21']
#==
df[np.where(condition,A,B)]  #如果条件为True，就是A，否则是B


# 排序
df.sort_index()
df.sort_values('columnsName')


# 重命名一列 定义新的列 修改列明
## 修改新的列
df.rename(columns= {'Adj Close' : 'Adjclose'})
## 创建新的列
df["Difference"] = df.High - df.Low
## 改变列的名称
df.index.name = "index_name"
## 对列修改
df.columns = map(str.lower(), df.columns)
df.columns = map(str.upper(), df.columns)


# 删除
df.drop('name')  #默认按行删除
df.drop('name',axis=1)  #按列名删除

# 转换数据类型
df['columnName'] = df['columnName'].astype('dataType')

# apply函数
df.columnsName.apply(lambda x: x*2)


# pandas一些参数的重新设置
# pd.get_option OR pd.set_option
# pd.reset_option("^display")

# pd.reset_option("display.max_rows")
# pd.get_option("display.max_rows")
# pd.set_option("max_r",102)                 -> specifies the maximum number of rows to display.
# pd.options.display.max_rows = 999          -> specifies the maximum number of rows to display.

# pd.get_option("display.max_columns")
# pd.options.display.max_columns = 999       -> specifies the maximum number of columns to display.

# pd.set_option('display.width', 300)

# pd.set_option('display.max_columns', 300)  -> specifies the maximum number of rows to display.
# pd.set_option('display.max_colwidth', 500) -> specifies the maximum number of columns to display. 

# pd.get_option('max_colwidth')
# pd.set_option('max_colwidth',40)
# pd.reset_option('max_colwidth')

# pd.get_option('max_info_columns')
# pd.set_option('max_info_columns', 11)
# pd.reset_option('max_info_columns')

# pd.get_option('max_info_rows')
# pd.set_option('max_info_rows', 11)
# pd.reset_option('max_info_rows')

# pd.set_option('precision',7) -> sets the output display precision in terms of decimal places. This is only a suggestion.
# OR
# pd.set_option('display.precision',3)

# pd.set_option('chop_threshold', 0) -> sets at what level pandas rounds to zero when it displays a Series of DataFrame. This setting does not change the precision at which the number is stored.
# pd.reset_option('chop_threshold') 
