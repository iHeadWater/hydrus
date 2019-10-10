# 利用pytorch写一个神经网络的示例——来自课程《Mordern deep learning in Python》
import matplotlib.pyplot as plt
from torch.autograd import Variable
from torch import optim
from util import get_normalized_data
import numpy as np
import pandas as pd
import torch

# 第一步是load data，这里采用的是deep learning里的hello world，即识别手写数字的数据集，来自kaggle。
# get the data,
# no need to split now, the fit() function will do it
Xtrain, Xtest, Ytrain, Ytest = get_normalized_data()

# get shapes
_, D = Xtrain.shape
K = len(set(Ytrain))

# 第二步是构建网络结构，使用pytorch构建神经网络要比直接通过numpy手写简单很多。和Keras类似，可以先构建一个sequential，然后逐层添加网络结构即可。
model = torch.nn.Sequential()
# 逐层添加网络即可，在pytorch中是采用add_module()函数。第一个参数是当前层的命名，可以取任何想要的名称。第二个参数就是该层。层要么是linear transformation，要么是activation
# 比如第一层，Linear,参数D是输入的神经元个数，第二个参数500是输出的神经元个数
model.add_module("dense1", torch.nn.Linear(D, 500))
model.add_module("relu1", torch.nn.ReLU())
model.add_module("dense2", torch.nn.Linear(500, 300))
model.add_module("relu2", torch.nn.ReLU())
model.add_module("dense3", torch.nn.Linear(300, K))
# 第三步是构建loss函数，loss函数详情可参考http://pytorch.org/docs/master/nn.html#loss-functions
loss = torch.nn.CrossEntropyLoss(size_average=True)
# 第四步是设置优化函数，Adam是一种常用的优化算法，是一种改良的GD算法。算法需要神经网络的parameters作为参数。
optimizer = optim.Adam(model.parameters())


# 第五步是定义训练过程和预测过程，这部分也是相对最难掌握的一部分。这部分相对TensorFlow和Theano都会麻烦一些。


def train(model, loss, optimizer, inputs, labels):
    """训练过程主要包括：包装输入输出到Variable变量，初始化优化函数，前向传播，反向传播，以及参数更新，详情见每步解释"""
    # 为什么要包装变量到Variable：把Tensor包装到Variable中，它就会开始保存所有计算历史。因此每次运算都会稍微多一些cost；另一方面，在训练循环外部对Variable进行计算操作相对容易。不包装也是可以计算的，并且后面的pytorch版本有柯南高就不需要Variable的这一步了
    inputs = Variable(inputs, requires_grad=False)
    labels = Variable(labels, requires_grad=False)

    # pytorch的梯度计算是累计的，这对有些神经网络是比较好的，因此这里初始化为0
    optimizer.zero_grad()

    # 直接调用model的前向函数即可得到输出
    logits = model.forward(inputs)

    # 然后计算loss
    output = loss.forward(logits, labels)

    # 接着就是进行反向传播计算
    output.backward()

    # 最后是更新参数
    optimizer.step()

    return output.item()


def predict(model, inputs):
    inputs = Variable(inputs, requires_grad=False)
    logits = model.forward(inputs)
    # argmax函数是给出axis维上数组中最大数的索引
    return logits.data.numpy().argmax(axis=1)


# 第六步定义各类超参数并开始训练过程
# 首先是将numpy变量都设置为torch中的张量，注意要指定数据类型
Xtrain = torch.from_numpy(Xtrain).float()
Ytrain = torch.from_numpy(Ytrain).long()
Xtest = torch.from_numpy(Xtest).float()

epochs = 15
batch_size = 32  # 每个batch的大小
n_batches = Xtrain.size()[0] // batch_size  # batch的个数

costs = []
test_accuracies = []
for i in range(epochs):
    cost = 0.
    for j in range(n_batches):
        Xbatch = Xtrain[j * batch_size:(j + 1) * batch_size]
        Ybatch = Ytrain[j * batch_size:(j + 1) * batch_size]
        cost += train(model, loss, optimizer, Xbatch, Ybatch)

    Ypred = predict(model, Xtest)
    acc = np.mean(Ytest == Ypred)
    print("Epoch: %d, cost: %f, acc: %.2f" % (i, cost / n_batches, acc))

    costs.append(cost / n_batches)
    test_accuracies.append(acc)

# 第七步是将训练过程可视化,# EXERCISE: plot test cost + training accuracy too。一般都是把cost和accuracy都可视化出来
# plot the results
plt.plot(costs)
plt.title('Training cost')
plt.show()

plt.plot(test_accuracies)
plt.title('Test accuracies')
plt.show()
