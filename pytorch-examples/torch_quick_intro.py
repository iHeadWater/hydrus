from __future__ import print_function
import torch
# 构建一个 5x3 的矩阵, 未初始化的:
x = torch.Tensor(5, 3)
print(x)
# 构建一个随机初始化的矩阵:
x = torch.rand(5, 3)
print(x)
# 获得 size:
print(x.size())
# 加法
y = torch.rand(5, 3)
print(x + y)

print(torch.add(x, y))

result = torch.Tensor(5, 3)
torch.add(x, y, out = result)
print(result)

# 可以用类似Numpy的索引来处理所有的张量！
print(x[:, 1])

# 改变大小: 如果你想要去改变tensor的大小, 可以使用 torch.view:
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())

# 转换一个 Torch Tensor 为 NumPy 数组
a = torch.ones(5)
print(a)

b = a.numpy()
print(b)
# 查看 numpy 数组是如何改变的.a和b是绑定的
a.add_(1)
print(a)
print(b)

# 看改变 np 数组之后 Torch Tensor 是如何自动改变的
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out = a)
print(a)
print(b)

# 可以使用 .cuda 方法将 Tensors 在GPU上运行.
# 只要在  CUDA 是可用的情况下, 我们可以运行这段代码
if torch.cuda.is_available():
    b = b.cuda()
    print(b + b)


import torch
from torch.autograd import Variable

# 创建 variable（变量）:

x = Variable(torch.ones(2, 2), requires_grad = True)
print(x)

# variable（变量）的操作:

y = x + 2
print(y)

# y 由操作创建,所以它有 grad_fn 属性.

print(y.grad_fn)

# y 的更多操作

z = y * y * 3
out = z.mean()

print(z, out)

# 梯度 我们现在开始了解反向传播, out.backward() 与 out.backward(torch.Tensor([1.0])) 这样的方式一样

out.backward()

# 但因 d(out)/dx 的梯度
# 你应该得到一个 4.5 的矩阵. 让我们推导出 out Variable “o”. 我们有 o=1/4∑izi, zi=3(xi+2)^2 和 zi∣∣xi=1=27. 因此, ∂o/∂xi=32(xi+2), 所以 ∂o∂xi∣∣xi=1=9/2=4.5.
print(x.grad)

# 你可以使用自动求导来做很多有趣的事情
x = torch.randn(3)
# torch.norm(input, p=2) → float
#
# 返回输入张量input 的p 范数。
#
# 参数：
#     input (Tensor) – 输入张量
#     p (float,optional) – 范数计算中的幂指数值
x = Variable(x, requires_grad = True)

y = x * 2
print(y.data)
print(y.data.norm())

while y.data.norm() < 1000:
    y = y * 2

print(y)

gradients = torch.FloatTensor([0.1, 1.0, 0.0001])
y.backward(gradients)

print(x.grad)

# 上面整个用计算图的思路去理解就很简单了

""" 神经网络可以使用 torch.nn 包构建.
 
 autograd 实现了反向传播功能, 但是直接用来写深度学习的代码在很多情况下还是稍显复杂,
  torch.nn 是专门为神经网络设计的模块化接口. nn 构建于 Autograd 之上, 
 可用来定义和运行神经网络. nn.Module 是 nn 中最重要的类, 
 可把它看成是一个网络的封装, 包含网络各层定义以及 forward 方法, 
调用 forward(input) 方法, 可返回前向传播的结果.

一个典型的神经网络训练过程如下:

    定义具有一些可学习参数(或权重)的神经网络
    迭代输入数据集
    通过网络处理输入
    计算损失(输出的预测值与实际值之间的距离)
    将梯度传播回网络
    更新网络的权重, 通常使用一个简单的更新规则: weight = weight - learning_rate * gradient

"""
# 定义一个网络:
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 卷积层 '1'表示输入图片为单通道, '6'表示输出通道数, '5'表示卷积核为5*5
        # 核心
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 仿射层/全连接层: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        #在由多个输入平面组成的输入信号上应用2D最大池化.
        # (2, 2) 代表的是池化操作的步幅
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # 如果大小是正方形, 则只能指定一个数字
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # 除批量维度外的所有维度
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()
print(net)