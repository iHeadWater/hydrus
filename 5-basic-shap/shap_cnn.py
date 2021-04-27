import torch, torchvision
from torchvision import datasets, transforms
from torch import nn, optim
from torch.nn import functional as F
import numpy as np
import shap

batch_size = 128
num_epochs = 2
# 将数据转移的cpu
device = torch.device('cpu')


# 模型
class Net(nn.Module):
    # 构建只看init部分就可以了

    def __init__(self):  # 构造函数

        super(Net, self).__init__()  # nn.Module的子类函数必须在构造函数中执行父类的构造函数
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 10, kernel_size=5),  # 卷积层
            nn.MaxPool2d(2),  # 池化
            nn.ReLU(),  # 采用relu激活函数
            nn.Conv2d(10, 20, kernel_size=5),
            nn.Dropout(),  # 减少过拟合，训练集中使用
            nn.MaxPool2d(2),
            nn.ReLU())

        self.fc_layers = nn.Sequential(
            nn.Linear(320, 50),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(50, 10),
            nn.Softmax(dim=1)  # nn.Softmax（）分类，就是概率，该样本属于各个类的概率 dim = 0指第一个维度，dim = 1指第二个维度，dim = 2指第三个维度，
        )

    # 将数据送到模型，模型如何处理的过程
    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(-1,
                   320)  # 在torch里面，view函数相当于numpy的reshape，x.view(-1, 320)这里-1表示一个不确定的数，就是你如果不确定你想要reshape成几行，但是你很肯定要reshape成320列，那不确定的地方就可以写成-1
        x = self.fc_layers(x)
        return x


#  model指建立好的网络模型；device指模型在哪个设备上运行，CPU还是GPU；train_loader是指数据集；optimizer用于优化；epoch指整个数据集训练的次数

def train(model, device, train_loader, optimizer, epoch):
    # 模型进入训练模式，对应的有model.eval()只有前传
    model.train()
    # 加载训练数据集合，这里一次 128 张图片以及对应的类别（0 - 9），data 是图片 shape 为[128, 1, 28, 28]，128张图片，灰度图片，像素大小为28*28。 target 是 128个图片的类别，每个用 0-9 的图片表示。
    for batch_idx, (data, target) in enumerate(train_loader):  # batch_idx为索引，（data, targe）
        data, target = data.to(device), target.to(device)  # data为图像，target为label
        # 将梯度初始化为零
        optimizer.zero_grad()
        # 前向传播求出预测的值
        output = model(data)
        # 计算当前损失
        loss = F.nll_loss(output.log(), target)
        # 反向传播，用来计算梯度
        loss.backward()
        # 更新所有参数
        optimizer.step()
        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))


def test(model, device, test_loader):
    model.eval()  # 只有前传，没有反向求梯度调参
    test_loss = 0
    correct = 0
    with torch.no_grad():  # 代表with下面的代码块，不参与反向传播，不更新参数
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output.log(), target).item()  # sum up batch loss
            pred = output.max(1, keepdim=True)[1]  # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()
    # Operator: x /= y，Meaning:  x  = x / y

    test_loss /= len(test_loader.dataset)  # 损失的平均值
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))
    # 加载训练集和测试集，pytorch 自带有 MNIST 数据集。 并且转为我们需要的格式
    # train_loader 里面就是 6000 个训练集，包含有图片和图片的标签
train_loader = torch.utils.data.DataLoader(
    # 数据加载器，结合了数据集合取样器，并且可以提供多个线程处理数据集。在训练模型时使用到此函数，用来把训练数据分成多个小组，此函数每次抛出一组数据。直至把所有的数据都抛出。就是做一个数据的初始化
    datasets.MNIST('mnist_data',  # 表示MNIST加载到本目录下
                   train=True,  # 表示是否加载数据库的训练集，false的时候加载测试集
                   download=True,  # 表示是否自动下载MNIST数据集
                   transform=transforms.Compose([
                       transforms.ToTensor()])),
                       batch_size = batch_size,shuffle = True)



# test_loader 里面就是 1000 个训练集，包含有图片和图片的标签
test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('mnist_data', train=False, transform=transforms.Compose([
        transforms.ToTensor()
    ])),
    batch_size=batch_size, shuffle=True)
#构建模型，并送到CPU中加速
model = Net().to(device)
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)

for epoch in range(1, num_epochs + 1):
    train(model, device, train_loader, optimizer, epoch)
    test(model, device, test_loader)
# since shuffle=True, this is a random sample of test data
#iter()函数获取这些可迭代对象的迭代器。然后我们可以对获取到的迭代器不断使⽤next()函数来获取下⼀条数据。
batch = next(iter(test_loader))
images, _ = batch
background = images[:100]
test_images = images[100:110]
#print(test_images)
# shap.DeepExplainer是用于解释深度学习模型的
#shap.KernelExplainer可用于解释所有的模型，尽管它运行时间比其他解释器时间长一点，但是它能够给出一个近似的的Shap values.
e = shap.DeepExplainer(model, background)
shap_values = e.shap_values(test_images)
# print(shap_values)
#numpy.swapaxes(arr, axis1, axis2)arr：输入的数组; axis1：对应第一个轴的整数 ;axis2：对应第二个轴的整数 ;将数组arr所对应的axis1轴和axis2轴交换位置 即可
shap_numpy = [np.swapaxes(np.swapaxes(s, 1, -1), 1, 2) for s in shap_values]
# print(shap_numpy)
test_numpy = np.swapaxes(np.swapaxes(test_images.numpy(), 1, -1), 1, 2)
shap.image_plot(shap_numpy, -test_numpy)
print(test_images)


