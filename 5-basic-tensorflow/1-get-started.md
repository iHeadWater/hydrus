# Tensorflow 环境安装

记录下如何安装 tensorflow。

## Win10下安装CPU版本Tensorflow

主要参考了tensorflow官方文档：[使用 pip 安装 TensorFlow](https://tensorflow.google.cn/install/pip#windows)

使用官方推荐的 pip 模式安装。

第一步，在系统上安装Python环境。

下载安装 Microsoft Visual C++ 可再发行软件包。

因为从 TensorFlow 2.1.0 版开始，此软件包需要 msvcp140_1.dll 文件，而该可再发行软件包随附在 Visual Studio 2019 中， 所以就选择安装 Visual Studio 2019 一次搞定：https://visualstudio.microsoft.com/zh-hans/downloads/

目前最新版本就是 Visual Studio 2019，安装社区版即可，下载的是一个安装工具，直接运行即可。安装时间略长，请耐心等待。

在弹出的安装选项中自由选择即可，个人也不太确定需要安装哪些，这里推荐安装下“使用 C++ 的桌面开发”， 选中这项，然后点击“安装”即可。

python安装安装可以选择anaconda，网上教程较多，比如：https://blog.csdn.net/ychgyyn/article/details/82119201

首先，下载anaconda安装包：https://repo.anaconda.com/download/ ，点击下载即可。

然后安装，一路默认即可（也可以指定安装位置），安装完成后，配置 anaconda 环境：在Path变量下加入如下条目（D:\ProgramData\Anaconda3 是个人anaconda安装根目录）。

```Path
D:\ProgramData\Anaconda3
D:\ProgramData\Anaconda3\Scripts
D:\ProgramData\Anaconda3\Library\lib
```

个人遇到了改环境变量之后，命令行不见得情况，参考这个得到了解决：http://www.xitongcheng.com/jiaocheng/dnrj_article_59107.html

第二步，创建虚拟环境。

使用 virtualenv，利用requirements.txt 文件，安装虚拟环境。方法如下：

首先，安装 virtualenv，任意位置打开cmd，执行：

```Shell
pip install virtualenv
```

由于最新版本的anaconda对应的python是3.8，而本项目需要python3.7.4，所以为了创建 python 3.7.4 环境，需要另外下载python 3.7.4

进入python官方网站：https://www.python.org/downloads/ ，找到3.7.4版本，点击“Download”进入该版本页面，选择“Windows x86-64 executable installer”下载安装。

安装的时候不必配置环境变量，自定义安装，确定自己的安装位置并记录，比如个人安装位置：D:\ProgramData\Python\Python37 。

最后一步记得启用长路径，按照tensorflow官方安装指南个网站的要求是这个网站：https://superuser.com/questions/1119883/windows-10-enable-ntfs-long-paths-policy-option-missing ，不过个人电脑上没看到这一项，而python安装的时候恰好有“取消长度限制”的选项，所以在这里就点击一下喽。

项目根目录下打开cmd工具，然后执行下面的命令创建python3.7(.4)的虚拟环境：

```Shell
virtualenv venv -p D:\ProgramData\Python\Python37\python.exe
```

激活虚拟环境：

```Shell
.\venv\Scripts\activate
```

在虚拟环境中安装软件包，这里直接使用 requirements.txt 安装（目前只有tensorflow2.1和一个pydot工具，如果需要其他pip包，可以在requirements.txt中自行添加）。

首先升级pip工具：

```Shell
python -m pip install --upgrade pip
```

然后安装依赖包。

首先安装外部依赖包，手动安装下GraphViz： https://www.graphviz.org/download/ 。

直接下载Executable Packages 并安装即可，选择Stable Windows install packages，在10/msbuild/Release/Win32 下载zip包。

解压到指定的文件夹 比如 个人是：D:\ProgramData\Graphviz

然后将该环境配置到环境变量中，方法和前面 anaconda 配置环境类似，把下面的路径加入Path即可。

D:\ProgramData\Graphviz\bin
配置后可能需要重启下，看后面执行完会不会报错，有问题就重启。

接下来安装python依赖包。

```Shell
pip install -r requirements.txt
```

这样就完成环境配置了。

下面是GPU版本的安装，不是本repo必需。

## Ubuntu18.04下安装TensorFlow-gpu

安装cuda和cudnn的步骤和pytorch下的方法一致，这里就不再重复了。可以重新检查下自己的cuda和cudnn版本。

看看自己的显卡信息：

``` Shell
$ nvidia-smi
NVIDIA-SMI 418.67       Driver Version: 418.67       CUDA Version: 10.1 
...
``` 

上面这个cuda version可能不是你安装的，因为这里是说这个驱动匹配的cuda version

然后看看gcc和g++，比如我的一个版本：

``` Shell
$ gcc --version
gcc (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609
$ g++ --version
g++ (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609
``` 

可以看看cuda版本，比如：

```Shell
$ cat  /usr/local/cuda/version.txt
CUDA Version 10.0.130
```

还可以查看cudnn是否安装：

```Shell
$ cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
cat: /usr/local/cuda/include/cudnn.h: No such file or directory
```

如果结果是上面这样的，说明cudnn没有安装好，可以看看cudnn是否已经下载：

```Shell
$ cat /usr/include/cudnn.h | grep CUDNN_MAJOR -A 2
#define CUDNN_MAJOR 7
#define CUDNN_MINOR 5
#define CUDNN_PATCHLEVEL 1
...
```

如上所示，是7.5.1版本，说明cudnn已经下载了，但是还没往cuda里面放。如果你没有权限安装，那么就要通知管理员来安装了。

然后安装tensorflow（未完待续）

## win10下安装TensorFlow-gpu

版本搭配：win10+cuda10.0+cudnn7.6.4+anaconda_python3.7+tensorflow2.0 （有待更新）

第一步，因为现在TensorFlow2.0支持cuda10.1，不过我这里的尝试比较老了，cuda选择了10.0。
如果电脑安装了visual studio 2019，那么安装cuda10.0时候会提示缺少visual studio 2017相关组件，因此需要首先安装visual studio 2017。
直接在visual studio官网上找，拉到页面最下面，找旧版本，不能下载的话，加入微软的开发者计划即可。这步下载安装过程可能比较长。

第二步: 去官网下载安装NVIDIA Driver
Select the appropriate version and click search

第三步: Install Anaconda (Python 3.7 version)

第四步: Update Anaconda
Open Anaconda Prompt to type the following command(s)

```Shell
conda update conda
conda update --all
```

第五步: 下载安装CUDA Tookit 10.0

Choose your version depending on your Operating System

第六步: Download cuDNN Download
Choose your version depending on your Operating System. Membership registration is required.

下载之后进行解压。

Add cuDNN into Environment PATH
Add the following path in your Environment. Subjected to changes in your installation path.

第七步: 安装TensorFlow

```Shell
$ pip install --upgrade pip
$ pip install tensorflow-gpu
```

接下来看看在一个已经安装过cuda和cudnn的win10电脑上如何使用pipenv安装tensorflow。

首先检查cuda和cudnn的版本：

打开cmd，输入：

```Shell
$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Sun_Jul_28_19:12:52_Pacific_Daylight_Time_2019
Cuda compilation tools, release 10.1, V10.1.243
```

可以看到cuda的版本是10.1，接下来看看cudnn，因为是cuda10.1，所以进入cuda10.1的文件夹:C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\include，找到cudnn.h，文本编辑器打开就可以看到：

```Shell
...
#define CUDNN_MAJOR 7
#define CUDNN_MINOR 6
#define CUDNN_PATCHLEVEL 4
...
```

如上图所示，我的是7.6.4版本。

接下来使用pipenv来安装tensorflow。首先建好一个项目，进入项目根目录。执行:

```Shell
$ pipenv isntall
```

这时候就会创建虚拟环境了。

然后在这里面安装tensorflow。根据现在最新的tensorflow版本情况，可以使用pip install tensorflow 方便的安装，这里使用pipenv install来安装：

```Shell
$ pipenv install tensorflow
```