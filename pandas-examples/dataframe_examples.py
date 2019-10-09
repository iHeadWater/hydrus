import pandas as pd
import numpy as np
from matplotlib import pyplot

"""对dataframe进行分组的例子"""
salaries = pd.DataFrame({
    'name': ['BOSS', 'Lilei', 'Lilei', 'Han', 'BOSS', 'BOSS', 'Han', 'BOSS'],
    'Year': [2016, 2016, 2016, 2016, 2017, 2017, 2017, 2017],
    'Salary': [999999, 20000, 25000, 3000, 9999999, 999999, 3500, 999999],
    'Bonus': [100000, 20000, 20000, 5000, 200000, 300000, 3000, 400000]
})
print(salaries.columns)
print(salaries.info())
print(salaries.describe())
salaries = salaries[['name', 'Year', 'Salary', 'Bonus']]
# 定顺序
print(salaries)
# 对dataframe按name进行分组
group_by_name = salaries.groupby('name')
# 获取分组后的某一组
se_temp = group_by_name.get_group('Lilei')
print(se_temp)
print(se_temp.describe())
# 循环各组，并将名字在给定的序列中的group添加到数组中
config = pd.Series({'names': ['Lilei', 'BOSS']})
dfs = []
for name, group in group_by_name:
    print(name)
    if name in config['names']:
        dfs.append(group)

for i in range(len(dfs)):
    # 如果没有把name和group分开，那么dfs[i]的类型会是tuple，key为name，value是group，可参考接下来的输出
    print(type(dfs[i]))
    print(dfs[i])

# 如果没有把name和group分开，那么dfs[i]的类型会是tuple，key为name，value是group
dfs_s = []
for group in group_by_name:
    dfs_s.append(group)
for i in range(len(dfs_s)):
    print(type(dfs_s[i]))
    print(dfs_s[i])

"""pandas与numpy数据结构之间的转换"""
# pandas dataframe与numpy array之间的转换
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df)
# df转换为ndarray
print(np.array(df))
# 读取某一列数据，两种方式均可
print(df['A'])
print(df.loc[:, 'A'])
# 一列数据转换为ndarray
print(np.array(df['A']))
# Series转ndarray
# Creating the Series
sr = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio'])
# Create the Index
index_ = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']
# set the index
sr.index = index_
# return numpy array representation
result = sr.as_matrix()
# Print the result
print("series转为ndarray：")
print(result)
# Print the series
print(sr)

"""读取csv等文件"""
# 如果遇到“UnicodeDecodeError: 'utf8' codec can't decode byte....”错误，用记事本另存csv文件时，将“编码”设置为‘UTF-8’即可
dataset = pd.read_csv('Sheet1.csv')
print(dataset)
# header指定某行的值作为各列的列名，1表示第二行，如果是None，则从第一行开始就是数据。
dataset = pd.read_csv('Sheet1.csv', header=1)
print(dataset)
# 因为给定的数据格式，各人有各自的一套，所以具体情况具体分析。比如，这里dataset的第一列可以去掉，即得到所有数据，删除列时，用drop函数，加参数axis=1，不加则表示删除行
dataset1 = dataset.drop(['旬平均'], axis=1)
print(dataset1)

"""专业方面，很多数据都是把年月或者年旬或者年日分别当做行和列，在计算时，需要进行处理，把时间变为一列或一行，即把几列或行的数组拼接起来
即将[1 2;2 3]的数据变为[1 2 2 3]，pandas的concat和numpy的concatenate类似。最后把行名index统一换成日期，构成时间序列Series"""
df = pd.DataFrame({"a": range(3), "b": range(3), "c": range(3)})
# iloc获取的数据格式为Series
se = df.iloc[:, 0]
# 获取dataframe的列数：df.shape[1]
for i in range(1, df.shape[1]):
    print("拼接第" + str(i) + "列:")
    se_temp = df.iloc[:, i]
    se = pd.concat([se, se_temp])
    print(se)
# 如果一开始没有给series起名，比如从csv读取出来时是dataframe，拼接之后没办法再给Series起名，但是又需要给它起名，那么只能采取重新构造一个series的方式来命名
se = pd.Series(se, name="aaaaaaa")
print(se)
# 把每行名称换为日期
print("index换为日期：")
rng = pd.date_range('2011-1-1', periods=9, freq='H')
print(rng)
se.index = rng
se = pd.Series(se, name="bbbbb")
print(se)

"""几列字符串拼为一列字符串"""
# 结构很简单: 第一列的名称.str.cat(第二列的名称)
df = pd.DataFrame({"a": range(3), "b": range(3), "c": range(3)})
df['a'] = df.iloc[:, 0].apply(str) + "-" + df['b'].apply(str) + "-" + df['b'].apply(str)
# 拼接之后，只留下特定的几列
df = df[['a', 'c']]
print(df)

# 取出某列的第几行
print(df['a'][0])
# df行数
print(df.shape[0])

"""多个Series拼接"""
# 初始化的时候不起名，后面rename没有用
a = pd.Series([1, 2], name='aa')
rng1 = pd.date_range('2011-1-1', periods=2, freq='D')
a.index = rng1
print(a)
b = pd.Series([2, 3, 4])
rng2 = pd.date_range('2011-1-2', periods=3, freq='D')
b.index = rng2
c = pd.Series([5, 6])
rng3 = pd.date_range('2011-1-1', periods=2, freq='D')
c.index = rng3
series1 = pd.concat([a, b], axis=1)
# 拼接时，给各列取名
print(series1)
df2 = pd.concat([series1, c], axis=1)
print(df2)

"""重新命名各列"""
new_col = ['new1', 'new2', 'new3']
df2.columns = new_col
print(df2)

"""交换列的位置"""
order = ['new2', 'new1', 'new3']
df2 = df2[order]
print(df2)

"""取dataframe指定多行列 slice操作"""
# 取多行
print(df2.iloc[0:2])
# 取多列
print(df2.iloc[:, 0:2])
# 取多行多列
print(df2.iloc[0:2, 0:2])
# 行用数字取，列用名字取
print(df2.iloc[0:2]['new1'])

"""按日期取值并处理"""
print(df2)
print(type(df2.index))
print('---------获取2011年前两天的数据-----------')
# 获取某段日期内的数据
print(df2['2011-01-01':'2011-01-02'])

"""给Series作slice操作"""
arr = [1, 2, 3, 4]  # 创建数组
series_1 = pd.Series(arr)
series_1.index = ['a', 'b', 'c', 'd']
print("------------------Series查询操作----------------------")
print(series_1['a'])
print(series_1[['a', 'b']])
print(series_1[series_1 > 2])
print(series_1[:2])
print(series_1['a':'c'])

"""给Series作折线图"""
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print(ts)
pyplot.plot(ts.index, ts.values, color='red', label='testing accuracy')
pyplot.show()
