# win10下安装TensorFlow-gpu

## 版本搭配

win10+cuda10.0+cudnn7.6.4+anaconda_python3.7+tensorflow2.0

## 具体步骤

第一步，因为现在不论是TensorFlow2.0还是pytorch1.2都支持的是cuda10.0，而不完全支持cuda10.1，版本不匹配的话会有问题，因此cuda选择10.0。
如果电脑安装了visual studio 2019，那么安装cuda10.0时候会提示缺少visual studio 2017相关组件，因此需要首先安装visual studio 2017。
直接在visual studio官网上找，拉到页面最下面，找旧版本，不能下载的话，加入微软的开发者计划即可。这步下载安装过程可能比较长。

第二步: 去官网下载安装NVIDIA Driver
Select the appropriate version and click search

第三步: Install Anaconda (Python 3.7 version)

第四步: Update Anaconda
Open Anaconda Prompt to type the following command(s)
conda update conda
conda update --all

第五步: 下载安装CUDA Tookit 10.0

Choose your version depending on your Operating System

第六步: Download cuDNN Download
Choose your version depending on your Operating System. Membership registration is required.

下载之后进行解压。

Add cuDNN into Environment PATH
Add the following path in your Environment. Subjected to changes in your installation path.

第七步: 安装TensorFlow
$ pip install --upgrade pip
$ pip install tensorflow-gpu
