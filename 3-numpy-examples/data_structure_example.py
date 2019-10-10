import numpy as np
# -----------数据结构示例-----------------
"""numpy向量"""
# NumPy向量默认行向量
features = np.array([0.49671415, -0.1382643, 0.64768854])
print(features)
# 对于一维数组，转置之后仍为一维数组
print(features.T)
# 可以用array[:,None]来创建列向量
print(features[:, None])

"""拼接数组"""
# 水平拼接
a = np.arange(10)
b = np.repeat(1, 10)
print(a)
print(b)
# 方法一
print(np.concatenate([a, b]))
# 方法二
print(np.hstack([a, b]))

"""广播运算"""
# 广播运算只在某些情况下可用，比如：
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2])
# 当维度不同的向量想要对齐，并在不足处补0时，不可以使用广播
length_zero = max(arr1.size, arr2.size) - min(arr1.size, arr2.size)
zeros = np.zeros(length_zero)
if arr1.size > arr2.size:
    arr_new = np.hstack([arr2, zeros])
    print(arr_new + arr1)
else:
    arr_new = np.hstack([arr1, zeros])
    print(arr_new + arr2)
