# ubuntu18.04安装pytorch1.2

## 版本搭配  

ubuntu18.04+cuda10.0+cudnn7.6.4+anaconda_python3.7+pytorch1.2

## 安装步骤

$ sudo lshw -C display | grep product
product: GP102 [GeForce GTX 1080 Ti]

首先检查GPU的兼容性，<https://developer.nvidia.com/cuda-gpus> 官网上查看compute capability是6.1  满足大于3或者3.5的要求。

然后保证安装到Ubuntu上的包是最新的，因此
$ sudo apt update
$ sudo apt upgrade #will ask you Y/n if you want to upgrade

关于NVIDIA 的驱动：
Ubuntu预装了GPU的通用驱动。这些驱动不是优化的。因此需要找到适合自己的GPU的最新的NVIDIA驱动。有几种选择：

Nvidia PPA：非常好的选择。通过使用PPA中包含的驱动达到开箱即用的效果。
Ubuntu Default recommended driver：Ubuntu能指出自己的电脑需要的NVIDIA驱动
Nouveau：NVIDIA驱动的开源实现版本。
Official NVIDIA site：和PPA的一样，但是不会自动更新，并且有时在更新、卸载或者安装中会报错。

推荐的，也是比较好的方式是使用NVIDIA PPA来安装驱动。因为有最新的NVIDIA官方驱动，也在Ubuntu上测试过，且安装过程比较平滑。
$ sudo add-apt-repository ppa:graphics-drivers/ppa
$ sudo apt-get update

此语句将PPA库添加到Ubuntu的包系统内（Ubuntu是一种Debian Linux的发行版，因此使用的是Debian的dpkg包系统，该系统提供给Ubuntu应用来安装。高级包工具（APT）使得我们能很容易的在终端与dpkg交互）。

接下来需要决定安装哪个版本的driver。去PPA库网站 https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa 上，网页拉到最下面检查版本，发现很多版本都可以；也可以在官网上检查https://www.nvidia.cn/Download/index.aspx?lang=cn，官网会给出一个版本；在命令行输入
$ ubuntu-drivers devices
可以看到给出了几个版本的驱动。
结合三者我决定选择一个都出现的版本nvidia-driver-430（事实证明貌似410更好，因为410是完美对应cuda10.0的版本）。
$ sudo apt install nvidia-driver-430

安装完毕之后需要重启电脑，直接命令行reboot即可，以使用新的显卡驱动：
$ reboot

重启之后，在命令行键入：
$ nvidia-smi
查看是否已成功安装，出现一些信息基本上就是安装成功了，显示的信息里说CUDA版本是10.1。不过根据https://zhuanlan.zhihu.com/p/73787970 别人的经验，装cuda-10.0也是可以的。 为什么一定是10.0,？因为pytorch目前支持的cuda是10.0。

为了保证驱动正常，所以有必要暂停其升级，使用以下命令：
$ sudo apt-mark hold nvidia-driver-430
nvidia-driver-390 set on hold.

To reverse this operation run:
$ sudo apt-mark unhold package_name

接下来可以安装CUDA了。

首先check下gcc和g++的版本。
$ gcc — version
gcc (Ubuntu 7.3.0–16ubuntu3) 7.3.0
$ g++ — version
g++ (Ubuntu 7.3.0–16ubuntu3) 7.3.0

安装cuda10.0和9.0不太一样。直接从官网下载
<https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=runfilelocal>
（用deb安装时我的报错了，不知道什么错误，有可能是因为cuda和driver的版本不完全匹配，所以用runfile安装了）

有提到要安装下kernel headers。（如果某个程序需要内核提供的一些功能，它就需要内核来编译程序，这个时候用的上kernel heads）。但几个也都没说。
$ sudo apt install linux-headers-$(uname -r)
执行命令即可安装，发现已经安装了。

按照官网提示安装即可，注意因为之前已经安装过驱动了，所以这里提示问是否安装驱动时（Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 XXX.XX），选择no，其他的都可以选择yes或者默认值即可。
$ sudo ./cuda_10.0.130_410.48_linux.run

重启下看看自己没有黑屏。

然后配置环境变量。
$ vim ~/.bashrc #打开配置文件
$ export PATH=/usr/local/cuda-10.0/bin:$PATH
$ export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH
$ export CUDA_HOME=/usr/local/cuda-10.0
$ source ~/.bashrc

最后验证cuda是否安装成功：
$ cd /usr/local/cuda-10.0/samples/1_Utilities/deviceQuery
$ sudo make
$ ./deviceQuery

接下来可以安装CUDNN了，可以下载最新版的对应cuda10.0版本的。
两种方法都有：
下载tar压缩包的：cudnn安装较容易只需要把文件解压后拷贝进cuda根目录即可。
下载三个deb文件的（the runtime library, the developer library, and the code samples library for Ubuntu 18.04）：
$ sudo dpkg -i libcudnn7_7.6.4.38-1+cuda10.0_amd64.deb
$ sudo dpkg -i libcudnn7-dev_7.6.4.38-1+cuda10.0_amd64.deb
$ sudo dpkg -i libcudnn7-doc_7.6.4.38-1+cuda10.0_amd64.deb 

安装完成验证是否安装成功：
Go to the MNIST example code: 
$ cd /usr/src/cudnn_samples_v7/mnistCUDNN/
Compile the MNIST example:
$ sudo make clean && sudo make
Run the MNIST example:
$ ./mnistCUDNN 
If your installation is successful, you should see Test passed!
现在已经不需要将gcc和g++降到6.X版本就可以执行。 

基础环境搭建好了之后，可以安装python的基本组件了。
首先安装anaconda，目前pytorch已经支持python3.7了。
下载linux下的安装包，执行：
$ sh Anaconda3-2019.07-Linux-x86_64.sh   #后边的文件名称是你的安装包的名称
然后一路按照默认的设置安装即可。
如果询问是否添加路径到环境变量或者是是否添加conda init，都选yes。

安装完成以后，重启终端。
先输入：
$ source ~/.bashrc
再输入：
$ python
即可看到安装成功的anaconda。

然后就可以安装pytorch了。
直接安装官网的start步骤即可。版本对应上即可。
检查是否安装成功：
$ python
$ import torch

能导入即成功。

可以先安装vscode，再测试下能不能使用GPU加速。
安装vscode直接去官网即可。然后下载对应的python插件即可使用。
$ sudo dpkg -i code_1.38.1-1568209190_amd64.deb

测试代码：
import torch as t
x = t.rand(5,3)
y = t.rand(5,3)
if t.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    print(x+y)

然后就可以运行一下程序试试了。
R2PF_LSTM_ep500_tr1_woNorm.py.
vscode不会自动调包？
