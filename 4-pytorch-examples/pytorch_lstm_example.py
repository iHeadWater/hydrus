"""一个简单的pytorch的lstm模型的示例"""
# Author: Robert Guthrie
# 作者：Robert Guthrie

import torch
import torch.autograd as autograd  # torch中自动计算梯度模块
import torch.nn as nn             # 神经网络模块
import torch.nn.functional as F   # 神经网络模块中的常用功能
import torch.optim as optim       # 模型优化器模块

torch.manual_seed(1)

# 第一句代码生成了一个LSTM对象，LSTM类继承自RNNBase类，RNNBase类继承自Module类，
# Module类是pytorch中完成一定网络功能的基类，可以通过继承该类定义自己的神经网络。
# 自己实现神经网络时，一般要重写其forward方法。
# Module实现了__call__方法，这意味着其可被当做可调用方法使用。比如下面有用到lstm()。
# RNNBase的__init__和__forward方法都是要读一读的，理解这个及基本理解了循环网络的机制。
# lstm单元输入和输出维度都是3
lstm = nn.LSTM(3, 3)
# 生成一个长度为5，每一个元素为1*3的序列作为输入，这里的数字3对应于上句中第一个3
inputs = [autograd.Variable(torch.randn((1, 3))) for _ in range(5)]

# 设置隐藏层维度，初始化隐藏层的数据。hidden变量是一个元组，其第一个元素是LSTM隐藏层输出，另一个元素维护隐藏层的状态。
# torch.rand(1,1,3)就是生成了一个维度为(1,1,3)的以一定高斯分布生成的张量
hidden = (autograd.Variable(torch.randn(1, 1, 3)),
          autograd.Variable(torch.randn((1, 1, 3))))

for i in inputs:
    # Step through the sequence one element at a time.
    # after each step, hidden contains the hidden state.
    out, hidden = lstm(i.view(1, 1, -1), hidden)
    print(out)
    print(hidden)
