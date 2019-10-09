from functools import reduce
import numpy as np
# ------------------------------常用计算函数示例--------------------------------------------
# 卷积运算
print("----------------------------卷积运算---------------------------")
print(np.convolve([1, 2, 3], [0, 1, 0.5]))

# 随机数运算
print("----------------------------随机数运算---------------------------")
i = 0
while i < 6:
    if i < 3:
        np.random.seed(0)
        # 种子一样，生成的随机数也是一样的
        print(np.random.randn(1, 5))
    else:
        print(np.random.randn(1, 5))
        pass
    i += 1
print("------从上面6次可以看出seed的影响-------")
i = 0
while i < 2:
    print(np.random.randn(1, 5))
    i += 1
print("----跳出原来的循环，看看新的循环里有没有不同，下面想比较个8次循环的随机内容，因为前面有三个循环是一样的，所以再补充两组随机值，凑够8个----")
print(np.random.randn(2, 5))
np.random.seed(0)
i = 0
print("----新的8次循环，和之前的8次循环进行比较-----")
while i < 8:
    print(np.random.randn(1, 5))
    i += 1
print("---可以看到，在种子一样的情况下，前后两次8个依次随机生成的数是一样的---")
# 以上结果说明，随机数种子对后面的结果一直有影响。同时，加了随机数种子以后，后面的随机数组都是按一定的顺序生成的

print("============================================================")
print("---------接下来换一个种子，看一看随机生成的数据是否一样----------")
i = 0
np.random.seed(0)
while i < 3:
    print(np.random.randn(1, 5))
    i += 1
i = 0
np.random.seed(1)
i = 0
while i < 3:
    print(np.random.randn(1, 5))
    i += 1
print("----当种子一样时，不论什么时候生成的随机数都是一样的，当种子不一样时，生成的随机数自然就不同了----")
# 不论在哪台电脑上，当随机数种子参数为0和1时，生成的随机数相同。说明该参数指定了一个随机数生成的起始位置。每个参数对应一个位置。并且在该参数确定后，其后面的随机数的生成顺序也就确定了。
# 所以随机数种子的参数怎么选择？我认为随意，这个参数只是确定一下随机数的起始位置。

# ------------------numpy all()函数---------------------
a = np.array([1, 2, 3])
b = a.copy()
print((a == b).all(axis=0).mean())
c = b.copy()
c[0] = 0
print((b == c).all(axis=0).mean())


# ------------------取交集函数---------------------------
lst1 = [1, 3, 4, 3]
lst2 = [3, 1, 2, 1]
print(np.intersect1d(lst1, lst2))
# 多个集合取交集
print(reduce(np.intersect1d, ([1, 3, 4, 3], [3, 1, 2, 1], [6, 3, 4, 2])))
# 返回两个交集相交的元素的index
C, ind1, ind2 = np.intersect1d(lst1, lst2, return_indices=True)
print(C)
print(ind1)
print(ind2)


# ---------------------where函数-------------------------------------------
aa = np.arange(10)
# np.where(condition, x, y)：满足条件(condition)，输出x，不满足输出y。
print(np.where(aa, 1, -1))
print(np.where(aa > 5, 1, -1))
# np.where(condition)：只有条件 (condition)，没有x和y，则输出满足条件 (即非0) 元素的坐标
a = np.array([2, 4, 6, 8, 10])
print(np.where(a > 5))


# ------------------------argmax函数--------------------------------------------
# 假定现在有一个数组a = [3, 1, 2, 4, 6, 1]现在要算数组a中最大数的索引是多少？argmax解决的就是这类问题
a = np.array([[1, 5, 5, 2],
              [9, 6, 2, 8],
              [3, 7, 9, 1]])
print(np.argmax(a, axis=0))
print(np.argmax(a, axis=1))
