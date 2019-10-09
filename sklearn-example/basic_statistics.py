"""sklearn常用的一些统计类的方法"""
from sklearn import preprocessing
import numpy as np

""" 预处理数据的方法总结（使用sklearn-preprocessing）"""
# 1. 标准化：去均值，方差规模化
# Found array with dim 3. the scale function expected <= 2 只能处理二维以下的数据
# 创建一组特征数据，每一行表示一个样本，每一列表示一个特征
# Standardization标准化:将特征数据的分布调整成标准正太分布，也叫高斯分布，也就是使得数据的均值维0，方差为1.
# 标准化的原因在于如果有些特征的方差过大，则会主导目标函数从而使参数估计器无法正确地去学习其他特征。
# 标准化的过程为两步：去均值的中心化（均值变为0）；方差的规模化（方差变为1）。
# 在sklearn.preprocessing中提供了一个scale的方法，可以实现以上功能。
x = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])
# 将每一列特征标准化为标准正太分布，注意，标准化是针对每一列而言的
x_scale = preprocessing.scale(x)
print(x_scale)

"""交叉验证KFold与StratifiedKFold是有区别的"""
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold

# KFold交叉采样：将训练/测试数据集划分n_splits个互斥子集，每次只用其中一个子集当做测试集，剩下的（n_splits-1）作为训练集，进行n_splits次实验并得到n_splits个结果。
# StratifiedKFold分层采样，用于交叉验证：与KFold最大的差异在于，StratifiedKFold方法是根据标签中不同类别占比来进行拆分数据的。
# X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]])
X = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]], [[13, 14], [15, 16]]])
# y = np.array([0, 1, 2, 3, 4, 5, 6, 7])
# y = np.array([0, 0, 1, 1])
y = np.array([0, 1, 2, 3])

# skf = StratifiedKFold(n_splits=2)
# n_splits是交叉验证分的个数，也是每个子集包含多少个元素的计算依据
skf = KFold(n_splits=3)
print(skf.get_n_splits(X, y))
print(skf)
# 交叉验证的X、y的维度需要注意，X：array-like, shape (n_samples, n_features)，当X维度较高时，split操作对应的是最外层的两个维度
for train_index, test_index in skf.split(X, y):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    print("X训练集：", X_train)
    print("X测试集：", X_test)
    print("y训练集：", y_train)
    print("y测试集：", y_test)
