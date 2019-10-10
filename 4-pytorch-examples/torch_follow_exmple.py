# 跟着例子学习PyTorch

# 先使用 numpy 实现网络。
# Numpy 提供了一个n维的数组对象, 并提供了许多操纵这个数组对象的函数.
#  Numpy 是科学计算的通用框架; Numpy 数组没有计算图, 也没有深度学习, 也没有梯度下降等方法实现的接口.
# 但是我们仍然可以很容易地使用 numpy 生成随机数据 并将产生的数据传入双层的神经网络,
#  并使用 numpy 来实现这个网络的正向传播和反向传播:

# -*- coding: utf-8 -*-
import numpy as np

import torch

import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt

# N 是一个batch的样本数量; D_in是输入维度;
# H 是隐藏层向量的维度; D_out是输出维度.
N, D_in, H, D_out = 64, 1000, 100, 10

# 创建随机的输入输出数据
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

# 随机初始化权重参数
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(500):
    # 前向计算, 算出y的预测值
    h = x.dot(w1)
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)

    # 计算并打印误差值
    loss = np.square(y_pred - y).sum()
    print(t, loss)

    # 在反向传播中, 计算出误差关于w1和w2的导数
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)

    # 更新权重
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2

# Numpy 是一个伟大的框架, 但它不能利用 GPU 加速它数值计算.
#  对于现代的深度神经网络, GPU 往往是提供 50倍或更大的加速,
# 所以不幸的是, numpy 不足以满足现在深度学习的需求.
# 介绍一下最基本的 PyTorch 概念: Tensor .
# PyTorch Tensor 在概念上与 numpy 数组相同:
# Tensor 是一个n维数组, PyTorch 也提供了很多能在这些 Tensor 上操作的函数.
#  像 numpy 数组一样, PyTorch Tensor 也和numpy的数组对象一样不了解深度学习,计算图和梯度下降；
# 它们只是科学计算的通用工具.
# 然而不像 numpy, PyTorch Tensor 可以利用 GPU 加速他们的数字计算.
#  要在 GPU 上运行 PyTorch 张量, 只需将其转换为新的数据类型.

# 将 PyTorch Tensor 生成的随机数据传入双层的神经网络. 就像上面的 numpy 例子一样,
# 我们需要手动实现网络的正向传播和反向传播:
# -*- coding: utf-8 -*-


dtype = torch.FloatTensor
dtype = torch.cuda.FloatTensor  # 取消注释以在GPU上运行

# N 批量大小; D_in是输入尺寸;
# H是隐藏尺寸; D_out是输出尺寸.
N, D_in, H, D_out = 64, 1000, 100, 10

# 创建随机输入和输出数据
x = torch.randn(N, D_in).type(dtype)
y = torch.randn(N, D_out).type(dtype)

# 随机初始化权重
w1 = torch.randn(D_in, H).type(dtype)
w2 = torch.randn(H, D_out).type(dtype)

learning_rate = 1e-6
for t in range(500):
    # 正向传递：计算预测y
    h = x.mm(w1)
    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)

    # 计算并打印loss
    loss = (y_pred - y).pow(2).sum()
    print(t, loss)

    # 反向传播计算关于损失的w1和w2的梯度
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.t().mm(grad_y_pred)
    grad_h_relu = grad_y_pred.mm(w2.t())
    grad_h = grad_h_relu.clone()
    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)

    # 使用梯度下降更新权重
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2

# torch和numpy
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
print(
    '\nnumpy', np_data,
    '\ntorch tensor', torch_data,
    '\ntensor to array', tensor2array
)

# 进行计算的时候 numpy和torch的方式也有所不同
data = np.array([[1, 2], [3, 4]])
tensor = torch.FloatTensor(data)

print(
    '\nnumpy:', data.dot(data),
    '\ntorch:', torch.mm(tensor, tensor)
)

# variable变量
variable = Variable(tensor, requires_grad=True)

t_out = torch.mean(tensor * tensor)
v_out = torch.mean(variable * variable)

print(t_out)
print(v_out)

v_out.backward()
# v_out=1/4*sum(variable*variable) d(v_out)/d(variable)=variable/2
print(variable.grad)

print(variable)

print(variable.data)

print(variable.data.numpy())

# fake data
x = torch.linspace(-5, 5, 200)  # x data (tensor) ,shape=(100,1)
x = Variable(x)
x_np = x.data.numpy()  # 为了画图，转换为numpy的数据形式

y_relu = F.relu(x).data.numpy()
y_sigmoid = F.sigmoid(x).data.numpy()
y_tanh = F.tanh(x).data.numpy()
y_softplus = F.softplus(x).data.numpy()

# plt.figure(1, figsize=(8, 6))
# plt.subplot(221)
# plt.plot(x_np, y_relu, c='red', label='relu')
# plt.ylim((-1, 5))
# plt.legend(loc='best')
#
# plt.subplot(222)
# plt.plot(x_np, y_sigmoid, c='red', label='sigmoid')
# plt.ylim((-0.2, 1.2))
# plt.legend(loc='best')
#
# plt.subplot(223)
# plt.plot(x_np, y_tanh, c='red', label='tanh')
# plt.ylim((-1.2, 1.2))
# plt.legend(loc='best')
#
# plt.subplot(224)
# plt.plot(x_np, y_softplus, c='red', label='softplus')
# plt.ylim((-0.2, 6))
# plt.legend(loc='best')

# plt.show()

# 关系拟合
# unsqueeze见文档（不知道什么用法的都去查文档，文档很清楚）
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor),shape=(100,1)
y = x.pow(2) + 0.2 * torch.rand(x.size())  # noisy y data (tensor), shape=(100, 1)
print(x)
print(y)
# 用 Variable 来修饰这些数据 tensor
x, y = Variable(x), Variable(y)


# 画图
# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()

# 建立神经网络
class Net(torch.nn.Module):  # 继承 torch 的 Module
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()  # 继承 __init__ 功能
        # 定义每层用什么样的形式
        self.hidden = torch.nn.Linear(n_feature, n_hidden)  # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)  # 输出层线性输出

    def forward(self, x):  # 这同时也是 Module 中的 forward 功能
        # 正向传播输入值, 神经网络分析出输出值
        x = F.relu(self.hidden(x))  # 激励函数(隐藏层的线性值)
        x = self.predict(x)  # 输出值
        return x


net = Net(1, 10, 1)
print(net)  # net 的结构

# 训练神经网络，optimizer 是训练的工具
optimizer = torch.optim.SGD(net.parameters(), lr=0.5)  # 传入 net 的所有参数, 学习率
loss_func = torch.nn.MSELoss()  # 预测值和真实值的误差计算公式 (均方差)

plt.ion()  # 画图
plt.show()
for t in range(100):
    prediction = net(x)  # 喂给 net 训练数据 x, 输出预测值

    loss = loss_func(prediction, y)  # 计算两者的误差

    optimizer.zero_grad()  # 清空上一步的残余更新参数值
    loss.backward()  # 误差反向传播, 计算参数更新值
    optimizer.step()  # 将参数更新值施加到 net 的 parameters 上
    # 接着上面来
    if t % 5 == 0:
        # plot and show learning process
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data[0], fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)
