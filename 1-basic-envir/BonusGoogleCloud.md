# Google Cloud 

google为了推广自己的云服务，有google cloud + colab + tensorflow + google earth engine的套装操作。另外，如果自己的数据量不是特别大，那么拿到这个平台上试运行也会死一个不错的选择。本文主要参考了：[Google Colab Free GPU Tutorial](https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d)，[苦逼学生党的Google Colab使用心得](https://zhuanlan.zhihu.com/p/54389036),[3 个相见恨晚的 Google Colaboratory 奇技淫巧！](https://zhuanlan.zhihu.com/p/56581879)等资料，以简单了解谷歌云平台和Colab在线编辑器的基本内容，关于tensorflow，本repo下后续会有一些介绍，关于google earth engine，在[hydroGIS](https://github.com/OuyangWenyu/hydroGIS)中有介绍。

## Introduction to Colab

直接抄一段：
Google Colab is a free cloud service and now it supports free GPU!
You can;
improve your Python programming language coding skills.
develop deep learning applications using popular libraries such as Keras, TensorFlow, PyTorch, and OpenCV.

简而言之，就是一个带GPU的云端开发环境。

因为Cloab是在Google drive上工作的，因此首先，在Google drive上创建一个文件夹来让其使用，比如我创建了一个Colab Notebooks文件夹。

在该文件夹下，右键，选择“更多”－“关联更多应用”，搜索colab，并关联。如果关联上了还看不到，可参考以下引用的评论中的表述：

```
何笑鸥修改时间：2019年9月5日
看到有小伙伴即使关联本应用，在谷歌云端硬盘的新建目录下仍然看不到它。我的办法是：
1. 转到页面：https://colab.research.google.com/notebooks/welcome.ipynb
2. 单击菜单栏偏下方的“复制到云端硬盘”
3. 进入自己的谷歌云端硬盘(drive.google.com)，可以看到出现一个黄色的文件夹，叫做Colab Notebooks，双击打开，里面有文件名为'“欢迎使用Colaboratory”的副本‘
4. 这时候再单击云端硬盘的“新建”-“更多”，就能看到“Google Colaboratory”项了。
```

如果还不行，就用新文件夹，留一个空白的colab文件用来复制粘贴即可。


### Running Python Codes

其使用方法和jupyter notebook是很像的。在左上角选择“+代码”，“+文本”可以分别添加代码和文本。注意colab貌似对中文的支持并不友好，所以尽量使用英文。

简单的代码可以直接运行即可。这里重点说下关于导入第三方模块和从github clone代码等操作。

### 选择GPU

然后选择硬件，直接 Edit（修改） > Notebook settings（笔记本设置） 或 Runtime>Change runtime type，然后选择GPU作为Hardware accelerator（硬件加速器）即可。

### 安装库

因为Tensorflow本身就是Google的，所以不用安装，可以直接用。直接使用tensorflow官方文档给的[初学者教程](https://www.tensorflow.org/tutorials/quickstart/beginner)即可。

因此,这里以pytorch的安装为例,不过colab上也有torch已经安装了.不过依然可以自己安装,这部分参考了:[使用Google Colab训练PyTorch神经网络](https://tiangexiao.github.io/2019/01/06/%E4%BD%BF%E7%94%A8Google-Colab%E8%AE%AD%E7%BB%83PyTorch%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C/),可以查看云端的系统/python版本/cuda版本,然后再根据pytorch官网上的推荐进行安装,可以发现,以 !开头的命令是可以执行操作系统的指令,以 %开头的命令表示魔法指令.colab没有原装conda,不过有pip和apt包管理器.

### 上传并使用数据文件

可以使用以下命令调用笔记本中的文件选择器：

``` python
from google.colab import files
uploaded = files.upload()
```

运行之后，我们就会发现单元 cell 下出现“选择文件”按钮.

也可以直接传入谷歌云盘。

在指定之前先用!ls命令查看一下云端自动分配的默认文件目录，云端默认的文件根目录是datalab.

```
! ls
```

详细的操作可以参考[官方文档](https://colab.research.google.com/notebooks/welcome.ipynb)。

### Clone github文件到Colab

clone文件到colab中直接使用!git clone命令即可，不过colab上运行的都是jupyter notebook文件，因此，对于工程性质的python项目，需要采用另外的方式。其实，Colab就是一个云端运行机器学习算法的jupyter文件的平台。

### Debug in Colab

在colab中的debug和在jupyter notebook中的类似，

## 使用Google Cloud Platform

虽然colab很好,但是还是在一个电脑上操作可能更舒服一些,这里从GCP的安装开始,这部分主要参考了:[薅羊毛，Google Cloud免费使用一年以及详细教程说明](https://www.luofan.net/post/112.html).

先完成第一个步骤－－试用GCP。然后创建一个项目。

接下来可以参考官方的[tensorflow文档](https://cloud.google.com/ml-engine/docs/tensorflow/getting-started-training-prediction?hl=zh-cn)，确保GCP已启动结算功能，并启用AIPlatform。

进入项目，首先，进入实例创建页面，点击快速入门简介，边看边操作，按照官方的提示要求做即可。

接下来参考[视频](https://www.bilibili.com/video/av31141381/)快速搭建深度学习环境，首先要升级下账号（免费的），才能在“IAM和管理”界面修改配额（quotas）。然后参考视频介绍即可。申请GPU配额的话，需要等两天才有回复，所以就先耐心等待了。可以通过配额页面的当前使用量看自己的机器配额情况。

在等待GPU申请的过程中，可以下载安装Google Cloud SDK来使用，这是一个用于管理托管在GCP上的资源和应用的工具。
