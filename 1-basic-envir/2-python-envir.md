# python环境配置

本文的内容框架主要参考了[Setting Up a Python Development Environment with and without Docker](https://nickjanetakis.com/blog/setting-up-a-python-development-environment-with-and-without-docker)，下面每小节又各有参考（详见下文）。

程序开始前一个很重要的环节就是 setting up your computer 。总的来说，包括以下几个部分：

1. What code editor should I use? 用什么编辑器
2. How do I install Python? 如何安装Python
3. How do I install my app’s dependencies? 如何安装程序依赖包 （如果不用docker基本上到这小节的前半部分就够了）
4. How do I install required external services? 如何安装必须的外部服务
5. How do I run my application? 如何运行自己的程序

## What Code Editor Should I Use?

python中比较常用的IDE有pycharm和vscode，都可以。这里推荐pycharm，windows下安装直接下载安装包：https://www.jetbrains.com/pycharm/download/#section=windows ，点击安装即可。没有特别用途，下载免费的 Community版 就够了。

Ubuntu下可以使用这个链接: https://www.jetbrains.com/pycharm/download/#section=linux 下载安装包。

然后解压文件：

```Shell
# 注意后面日期自行对应下载的版本
tar -xzf pycharm-community-20xx.x.x.tar.gz
```

使用tar -xzf pycharm-community-20xx.x.x.tar.gz -C <指定文件夹> 可以解压到指定文件夹下，当然也可以解压后再移动到指定文件夹下，比如：

```Shell
mv pycharm-community-20xx.x.x ../programs/pycharm-community-20xx.x.x
```

然后可以进入文件夹打开软件：

```Shell
cd ../programs/pycharm-community-20xx.x.x/bin
sh pycharm.sh
```

这时候稍等一会儿，会弹出pycharm的界面，提示配置pycharm。可以一直默认。

如果想让pycharm后台运行，那么可以执行下列代码：

```Shell
sh pycharm.sh &
```

然后在命令行敲回车，就可以打开新的对话了。

如果不想要.Pycharmxxx 系统配置文件在默认文件夹下，那么可以参考：[PyCharm 占用过大 C 盘空间，system 配置文件迁移](https://www.cnblogs.com/jingsupo/p/11616205.html) 配置。

首先，先将你的.PyCharm2018.3文件复制到你想放的文件夹下。

然后利用PyCharm 里的 Help/Edit Custom Properties 的选项新建 idea.properties 文件

之后在创建的文件夹下进行如下修改，当然除了 system 之外，还可以配置其他路径将其他内容也进行迁移。

``` config
# custom PyCharm properties

idea.config.path=${user.home}/.PyCharm20xx.x/config
idea.system.path=${user.home}/.PyCharm20xx.x/system
# idea.plugins.path=${idea.config.path}/plugins
# idea.log.path=${idea.system.path}/log
```

比如我的是：idea.config.path=/mnt/sdc/wvo5024/.PyCharm20xx.x/config

然后将原文件夹下的system文件夹删除即可，注意不要删除config文件夹，因为这个idea.properties 文件就在这个文件夹下。

## Install Python

首先安装python，个人建议直接安装anaconda或者miniconda，README中已经提供安装参考了，也可以参考[这里](https://github.com/waterDLut/WaterResources/blob/master/tools/jupyterlab&markdown.md#12-jupyterlab%E5%90%AF%E5%8A%A8)，这里就不赘述了。

这里简单补充下pip和conda的相关概念。主要参考了anaconda的文章：[Understanding Conda and Pip](https://www.anaconda.com/understanding-conda-and-pip/)

conda 和 pip 通常被认为是差不多的。然而虽然它们很多功能重叠，但它们被设计是用于不同的目的。

Pip 是一个python包官方推荐的从[Python Package Index, PyPI](https://pypi.org/)安装包的工具。Pip 以wheels或source distributions的形式安装 打包的python 软件。从源码安装，即后者source distribution需要系统有兼容的解释器和需要的库。

Conda是一个跨平台的包和环境管理器，它是从Anaconda repository 和 anaconda cloud 安装和管理conda 包。conda包是二进制包，所以不需要解释器来安装，并且conda安装的不仅限于python软件，也可以是C或者C++库，或者R包等。

这就是两者的一个主要区别，即pip安装python包，而conda安装任何语言的包。在使用pip之前，必须要安装有python解释器。而conda不仅可以安装python包，还可以安装python解释器。

两者的另一个区别是conda能创建独立的环境，在各独立环境中，可以安装各自的python版本和包。这在数据科学工具中很有用，因为不同工具的依赖可能会有冲突。而pip需要依赖于一些工具来创建独立环境，比如virtualenv或venv。还有一些像pipenv，poetry和hatch的工具，它们包装了pip和virtualenv来提供简易的使用方法。

pip和conda在安装依赖时也有不同。安装包时，pip安装以递归序列的循环来安装依赖包，不能保证同时满足所有依赖包的安装。如果按顺序较早安装的包与按顺序较晚安装的包有不兼容的依赖项版本，则可能导致环境以微妙的方式被破坏。而conda使用了可满足性(SAT)求解器来验证安装在环境中的所有包的所有要求都能得到满足。这个check会花费一些时间，但是能防止出现错误的安装。只要包 元数据关于依赖的内容是正确的，conda就能产出正确的工作环境。

用conda可以安装的包 有 anaconda repo里超过1500个库以及anaconda cloud中的可以从包括 conda-forge 和 bioconda 等channel（通道或频道）处获取的数千个包。conda有很多不同的通道，什么意思呢？这里简单补充下，根据[conda-forge 的 introduction](https://conda-forge.org/docs/user/introduction.html)，conda团队打包了很多包并以默认channel的形式提供给所有的用户。但是如果想要使用的包不在默认通道中，用户就要创建自己的channel，而这时候找包，想要实现不同channel包能兼容且channel一直有维护等是比较难做到的，但conda-forge是一个专用通道，它能帮助轻松解决这些问题，简而言之，用conda的话，优先用它就行了。

尽管conda中可以有这么多的工具包可用，但是相比于PyPI上的超过15万可用包而言仍然是很小的。如果有些工具包只能通过pip来安装，考虑到conda和pip的相似性，混合使用这两种工具来创建计算环境也不奇怪了，不过混合使用时需要注意一些事项，稍后更详细介绍。

一个表格简单总结下conda和pip的比较：

| |conda|pip|
|-|-|-|
|manages |binaries|wheel or source|
|can require compilers|no|yes|
|package types|any|Python-only|
|create environment|yes, built-in|no, requires virtualenv or venv|
|dependency checks|yes|no|
|package sources|Anaconda repo and cloud|PyPI|

## Getting Your Python App Running without Docker

关于docker是什么可以不用管，因为这一节是不会用到它的。

接下来，就是如何安装所需程序包。比如numpy，pandas等，也有 required external services 比如你的数据库。

先说如何安装依赖工具包。当然你可以使用pip或者conda一个个地安装。但是一个一个地安装显然是比较慢的，最关键的是，可能会有两个不同项目使用同一个包不同版本的情况，那就很麻烦了。所以就有人开发了一个叫做 Virtual Environment 的东西--Virtualenv，这个python工具可以为每个项目创建一个虚拟环境，这样项目互相之间就不会影响了。接下来记录下Virtual Environment及其相关的内容。因为conda和pip的方式不同，所以下面分开记录，个人根据自己的情况自己选择工具，各有优劣，比如对于conda，因为是跨语言的，所以有些外部依赖可以容易安装，但是会有很多python包不在conda中，需要混合使用pip；而pip虚拟环境中就能随意安装python包，但是它的问题是有可能有些外部依赖会导致python包不能安装成功，这对于经常需要一些外部依赖的水文水资源相关计算来说确实不是很方便。个人建议可以优先使用conda来配置虚拟环境，当conda安装不了的时候再用pip补充。更多建议可以参考：[Conda: Myths and Misconceptions](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)；当然如果更愿意用 pip，或者有些重要的工具（比如 tensorflow）推荐使用pip安装，那么可以直接看[virtual-environment和pipenv](https://github.com/OuyangWenyu/hydrus/blob/master/1-basic-envir/2-python-envir.md#virtual-environment-%E5%92%8C-pipenv)

### Conda Environment

本小节先简单介绍下conda的使用的一些意见，尤其是和pip混合使用时要注意的内容，然后再看看具体如何用conda管理environment。

根据前面第二节的介绍可以看出，根据anaconda的意见，是能用conda就用conda，不够的时候再用pip。关于在conda中使用pip，再补充一些内容，参考：[Using Pip in a Conda Environment](https://www.anaconda.com/using-pip-in-a-conda-environment/)

混合使用conda和pip有时候会遇到一些问题，这是因为conda不会控制它不安装的包，如果conda 在pip之后安装，可能会overwrite一些包，这可能会破坏pip安装的内容。类似的pip也会破坏conda的。有一些方式可以避免在同时使用conda和pip时遇到环境被破坏的情况。

一种就是只用conda，如果需要的软件不是作为conda包提供的，那么可以使用conda build为上述软件创建包。对于PyPI上可用的项目，conda skeleton命令(它是conda-build的一部分)经常生成一个配方，可以使用该配方创建一个conda包，而几乎不需要修改。

为所有需要的附加软件创建conda包是将数据科学环境放在一起的一种可靠的安全方法，但如果环境中包含大量仅在PyPI上可用的包，则可能成为一种负担。在这些情况下，**仅在通过conda安装了所有其他需求之后才使用pip是最安全的做法**。此外，应该使用“仅在需要时才升级策略”的参数来运行pip，以防止对通过conda安装的包进行不必要地升级。这是运行pip时的默认值，注意最好不更改它。

如果希望使用pip与conda包一起安装软件，那么最好将此安装**安装到专门构建的conda环境中**，以保护其他环境不受pip可能进行的任何修改的影响。Conda环境彼此隔离，允许安装不同版本的包。许多用户仅依赖于通过安装Anaconda或Miniconda创建的根conda环境。如果这个环境充斥着pip和conda安装，那么恢复起来就会困难得多。另一方面，创建独立的conda环境允许您轻松地删除和重新创建环境，而不会危及您的核心conda功能。

一旦使用pip将软件安装到conda环境中，conda将不知道这些更改，并可能进行破坏环境的修改。与先运行conda、pip再运行conda不同，更可靠的方法是使用合并后的conda需求创建一个新环境，然后运行pip。可以在删除旧环境之前测试这个新环境。再次强调，造成问题的主要是pip的状态性。由于安装包的顺序而存在的状态越多，就越难以保持正常工作。

对于经常重新创建的环境，将conda和pip包需求存储在文本文件中是一个很好的实践。包需求可以通过文件参数提供给conda，通过-r或需求提供给pip。可以将包含conda和pip需求的单个文件导出或提供给conda env命令来控制环境。这两种方法的优点是，描述环境的文件可以检入版本控制系统并与他人共享。

总之，在结合使用conda和pip时，最好使用一个隔离的conda环境。只有在使用conda来安装尽可能多的包之后，才能使用pip来安装任何剩余的软件。如果需要对环境进行修改，最好创建一个新环境，而不是在pip之后运行conda。在适当的时候，conda和pip需求应该存储在文本文件中，比如本项目下的environment.yml文件。

总结下，就是：

- Use pip only after conda
    - install as many requirements as possible with conda, then use pip
    - pip should be run with –upgrade-strategy only-if-needed (the default)
    - Do not use pip with the –user argument, avoid all “users” installs
- Use conda environments for isolation
    - create a conda environment to isolate any changes pip makes
    - environments take up little space thanks to hard links
    - care should be taken to avoid running pip in the “root” environment
- Recreate the environment if changes are needed
    - once pip has been used conda will be unaware of the changes
    - to install additional conda packages it is best to recreate the environment
- Store conda and pip requirements in text files
    - package requirements can be passed to conda via the –file argument
    - pip accepts a list of Python packages with -r or –requirements
    - conda env will export or create environments based on a file with conda and pip requirements

了解了以上概念，现在根据conda官方文档[Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)，看看如何管理环境。

接下来就以为本项目创建环境为例

如果仅运行本repo，就用项目README.md中说的环境文件安装即可，以下内容就**不要执行了**，这里记录下列是为了给其他项目的环境构建做一个指导。

在本项目文件夹下打开terminal，输入：

```Shell
conda create --name hydrus
```

输入y即可创建。创建的环境存储在 anaconda3\envs 文件夹下。如果没有指定python环境，那么默认的使用的和安装的anaconda一样的python版本，这里指定使用的是python3.7。要创建一个特定的python版本环境可以使用如下代码：

```Shell
$ conda create --name hydrus python=3.7
```

根据提示可以看到执行以下语句可进入hydrus环境：

```Shell
$ conda activate hydrus
```

如果你没能进入，那可能是terminal环境有点问题，如果你是windows那就重新打开终端试试，如果是Ubuntu，那么就重新加载下.bashrc文件。

进入hydrus环境后，执行以下语句可以退出hydrus环境。

```Shell
conda deactivate
```

还可以指定environment的安装环境，比如下列命令会在当前目录下创建一个叫做envs的子文件夹：

```Shell
conda create --prefix ./envs python=3.9
```

这时候进入环境的命令需要使用全名（安装后会有提示），比如我在Ubuntu下为项目建立了独立环境：

```Shell
conda activate /mnt/xxx/hydrus/envs
```

这在需要单独为一个项目创建单独的环境时尤其有用，如果你的anaconda或者miniconda的文件夹所在硬盘空间够，就不要折腾了，直接创建 hydrus 环境即可。

激活hydrus环境后，就可以进入jupyter lab了。注意，如果直接进入cmd，输入jupyter lab，那么进入的还是外边安装的anaconda的jupyter lab，所以这里要在hydrus环境下安装jupyter：

```Shell
$ conda install -c conda-forge jupyterlab
```

然后再执行：

```Shell
$ jupyter lab
```

现在可以在命令行里看到：

![](pictures/Picture3.png)

可以看到启动的jupyter lab是hydrus环境下的，接下来就可以在jupyter lab中操作了，jupyter lab 导航页面如下所示：

![](pictures/Picture2.png)

可以看到，能打开终端，能新建notebook，txt文件等。以下没有特别说明，终端操作都是在jupyter lab中打开的终端上进行，打开一个终端，输入：

```Shell
$ conda env list
```

可以看到已经处于hydrus环境下了。

接下来可以使用代码安装package，比如

```Shell
conda install -n hydrus scipy
```

如果需要指定版本，可以使用如下语句：

```Shell
conda install -n hydrus scipy=0.15.0
```

如果在创建环境时，就指定安装包，可以使用类似如下语句：

```Shell
conda create -n hydrus python=3.6 scipy=0.15.0 astroid babel
```

也可以通过environment.yml文件来创建环境。手动创建文件的方式可以参考：[Creating an environment file manually](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually)

示例可直接看本项目的environment.yml文件。可以先删除刚刚创建的虚拟环境：

```Shell
conda remove --name hydrus --all
```

如果是删除./envs文件夹，可以直接手动删除即可。

然后在项目文件夹下执行以下语句就可以创建环境hydrus了，直接使用下列语句：

```Shell
conda env create -f environment.yml
```

进入虚拟环境并查看当前环境是否安装正确：

```Shell
conda activate hydrus
conda env list
```

如果更改了environment.yml文件的内容后需要更新环境，则可以运行：

```Shell
conda env update --file environment.yml  --prune
```

--prune参数表示删除不再需要的依赖包。
 
如果需要复制环境，则可以使用：
 
```Shell
conda create --name hydrus-clone --clone hydrus
```

如果在conda中使用pip，首先在conda中安装pip：

```Shell
conda install -n hydrus pip
conda activate hydrus
```

然后就可以使用pip了。比如安装 matplotlib：

```Shell
pip install matplotlib
```

除了前面说的手动写yml文件，还可以直接使用conda导出。在hydrus环境下，使用下列代码可以生成新的environment.yml文件：

```Shell
$ conda env export > environment.yml
```

环境会同时导出conda和pip安装的包（如果pip安装了包），但是这个导出的环境一般会非常详细复杂，所以一般还是建议手动设置好environment.yml。

另外，可以看到环境文件里有用到conda-forge channel，这个频道是我们水资源等地球科学相关专业都会经常用的一个conda频道。这里建议直接看看earthlab的github项目：[earth-analytics-python-env](https://github.com/earthlab/earth-analytics-python-env)的environment.yml文件，就知道了，对应的博客：[Lesson 4. Set Up Your Conda Earth Analytics Python Environment Setup earth analytics environment](https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/)

注意根据[conda-forge Tips & tricks](https://conda-forge.org/docs/user/tipsandtricks.html#how-to-fix-it) 的说明，conda-forge和conda并不完全兼容，因此有时候，**需要将前后顺序钉死，conda-forge在前**，这样才能避免出现安装错误，否则很可能报错（个人实践中暂时没有碰到问题，所以下面的.condarc文件仅供参考）。

执行以下语句，系统会自动为你创建一个.condarc 文件:

```Shell
conda config --add channels conda-forge
```

.condarc文件内容如下：

``` code
channel_priority: strict
channels:
  - conda-forge
  - defaults
```

.condarc文件在我的win10上，是在 C:\Users\xxx下 ，即用户的主目录下，如果没有channel_priority: strict，在终端执行以下语句可以固定顺序：

```Shell
conda config --set channel_priority strict
```

另外，如果需要清理conda的包，可以使用conda clean 命令，conda clean --help 看看自己需要哪个指令，这在自己的硬盘空间不够的时候还是很有用的。

**如果不需要用docker，也不用pip的environment，到这里就够了，不必再往下看了，下面都是针对实际项目中使用pipenv及docker的。**

进入下一节：[1-learn-python/1.1-basic-python.ipynb](https://github.com/OuyangWenyu/hydrus/blob/master/1-learn-python/1.1-basic-python.ipynb)

### Virtual Environment 和 Pipenv

在开发Python应用程序的时候，系统安装的Python3只有一个版本。所有第三方的包都会被pip安装到Python3的site-packages目录下。

如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python 3。如果应用A需要ruanjian 2.7，而应用B需要ruanjian 2.6怎么办？

这种情况下，**每个应用可能需要各自拥有一套“独立”的Python运行环境**。**virtualenv**就是用来为一个应用**创建一套“隔离”的Python运行环境**。

python3.3之后可以直接使用python自带的 venv，用法和virtualenv 差不多，将下面代码中的“virtualenv ”换成“python -m venv ”即可，不过细节可能不同，这里没有尝试，所以就不多说了，还是以virtualenv为主。

在一切开始之前，需要安装python和pip，这点和前面的conda 做法不太一样。可以先安装一个所需版本的python，比如最新版的 Python 3.7： 3.7.9 。

首先，从[python网站](https://www.python.org/downloads/)下载该版本，win10下面直接下载 Windows x86-64 executable installer 安装包即可。

然后点击安装包进行安装，直接选择给出的第一项点击安装即可，下面勾选项一个都不用勾选，可以都取消。即不需要配置python环境（也可以勾选配置，无所谓），因为我们可能在不同的虚拟环境中需要不同版本的python，因此这里没必要指定好python环境，不过如果想方便，也可以配置好，但注意要将python文件根目录、Scripts目录名以及**Library\bin**三个文件路径都放入环境变量下。记住刚刚安装的位置，比如我的是在：C:\Users\hust2\AppData\Local\Programs\Python\Python37，在C:\Users\hust2\AppData\Local\Programs\Python\Python37\Scripts 文件夹里有pip工具。

在pip的文件夹下打开命令行,然后用pip安装virtualenv：

``` bash
pip install virtualenv
```

然后，假定我们要开发一个新的项目，需要一套独立的Python运行环境，可以这么做：

第一步，在本文件所在的文件夹下打开命令行，创建目录：

```bash
mkdir myproject
cd myproject
```

第二步，用virtualenv创建一个独立的Python运行环境（如前所述，没有配置环境变量，所以这里直接用了绝对路径），环境命名为venv；如果需要指定python版本，则用安装的python来作为-p参数的值，如下所示：

```Shell
C:\Users\hust2\AppData\Local\Programs\Python\Python37\Scripts\virtualenv venv -p C:\Users\hust2\AppData\Local\Programs\Python\Python37\python.exe
```

如果想要删除刚刚创建的虚拟环境，因为我们什么也没装，直接删除venv文件夹就行了。

新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用下面的命令激活该环境：

```Shell
.\venv\Scripts\activate
```

可以观察命令行，注意到命令提示符变了，**有个(venv)前缀**，表示当前环境是一个名为venv的Python环境。如果想要更新pip环境，可以使用如下命令：

```Shell
python -m pip install --upgrade pip
```

然后可以正常安装各种第三方包，比如安装 numpy：

``` Shell
pip install numpy
```

在venv环境下，用pip安装的包都被安装到venv这个环境下，系统Python环境不受任何影响。也就是说，venv环境是专门针对myproject这个应用创建的。

如果想要退出当前的venv环境，可以使用deactivate命令：

```Shell
deactivate 
```

此时就回到了正常的环境，现在pip或python均是在系统Python环境下执行。

以上可知，完全**可以针对每个应用创建独立的Python运行环境**，这样就可以对每个应用的Python环境进行隔离。那virtualenv是如何创建“独立”的Python运行环境的呢？原理很简单，就是把系统Python复制一份到virtualenv的环境，用命令 .venv/bin/activate进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。

另外还有一个重要的文件requirements.txt必须一提，接下来的内容参考：[What is the python requirements.txt?](https://www.idkrtm.com/what-is-the-python-requirements-txt/)

如果浏览github上的python项目，经常会看到它。它就是一个指定运行项目所需的python packages 的。一般是在项目根目录下。一个requirements.txt形如：

```requirements.txt
pyOpenSSL==0.13.1
pyparsing==2.0.1
python-dateutil==1.5
```

每行对应一个package，然后是它的版本号。版本号也很重要，毕竟版本变化之后，容易出bug。

在刚才的venv虚拟环境下使用下面的命令即可生成requirements.txt文件。

``` Shell
pip freeze >requirements.txt
```

可以看到已经安装的所有库以及其版本（这里只试装了一个numpy，因此只有一个numpy==xxx）。

如果转移到一个新的环境下，可以直接根据requirements.txt安装库，创建好virtual environment，然后激活环境，再在环境中执行下述操作即可。

1. 打开终端
2. 进入 requirements.txt 所在的文件夹
3. 运行： pip install -r requirements.txt

最后，前面已经说了，pip是不能安装非python的外部依赖的，所以如果有些库需要额外安装，还需要提前手动处理好。

前面提到了pip和virtualenv，其实还有一个更强大的工具pipenv，接下来就记录下其基本内容，不过根据一些介绍：https://zhuanlan.zhihu.com/p/81568689 ，这些更高级工具貌似稳定性略差了一些，所以个人建议还是优先使用底层的工具较好，所以到这pip工具的使用学习也可以结束了，如果需要pipenv再了解后续内容。

以下内容主要参考了：[pipenv使用指南](https://crazygit.wiseturtles.com/2018/01/08/pipenv-tour/)，[Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/) 以及 [Pipenv——最好用的python虚拟环境和包管理工具](https://www.cnblogs.com/zingp/p/8525138.html)等。

首先，简单概述下，pipenv是**Python官方推荐的包管理工具**。可以说，它**集成了virtualenv, pip和pyenv三者的功能**。其目的旨在集合了所有的包管理工具的长处，如: npm, yarn, composer等的优点。

它能够**自动为项目创建和管理虚拟环境**，从Pipfile文件添加或删除安装的包，同时生成Pipfile.lock来锁定安装包的版本和依赖信息，避免构建错误。

pipenv主要解决了如下问题:

- 不用再单独使用**pip和virtualenv**, 现在它们**合并**在一起了
- **不用再维护requirements.txt**, 使用**Pipfile和Pipfile.lock**来代替
- 可以使用多个python版本(python2和python3)
- 在安装了pyenv的条件下，可以自动安装需要的Python版本

接下来，看看pipenv的来龙去脉。首先明确pipenv解决了什么问题？

#### Problems that Pipenv Solves

从上面说到的requirements.txt说起，比如在requirements中有flask==0.12.1，虽然指定了flask的版本，但是flask的依赖的版本是没有指定的，如果直接使用上一节说到的pip install安装的话，都会安装最新版的依赖。这可能会导致一些小问题。这就是real issue：**the build isn’t deterministic**。 即给定相同的requirements.txt文件，安装的库却可能是不同的。

比较常用的解决方法是上一节也提到过的freeze，这样就能获取所有的库及其版本号。执行之后，将结果copy到requirements.txt即可。然而，这个方法却有另外的问题。

因为，旧版本可能会有bug，有可能某个版本的依赖是需要及时更新补丁的，如果用了freeze的办法得到requirements文件，现在就需要手动修改一下某个依赖库。实际上，很多时候也并不需要一直保持在现有的版本下，很多依赖库使用最新版本可能更好更安全。这一部分的问题就是：**How do you allow for deterministic builds for your Python project without gaining the responsibility of updating versions of sub-dependencies?**

答案就是Pipenv。

现在再看另一个问题。当处理多个项目时，如果项目A需要django 1.9版本，另一个项目B需要django 1.10版本。那么这时候就需要使用前面提到的 virtual environment 来处理。工具就是venv 。现在Pipenv是包含了venv 的功能的。

然后还有一个Dependency Resolution。什么意思？加入 requirements.txt 文件中有如下代码：

```python requirements
package_a
package_b
```

假如package_a有依赖 package_c>=1.0，而package_b 有依赖 package_c<=2.0. 那么现在就是要求package_c (being >=1.0 and <=2.0) 。现在想要工具自动选择一个合适的版本，这就是“dependency resolution.”现在如果在requirements文件中加入下列语句：

```python requirements
package_c>=1.0,<=2.0
package_a
package_b
```

不过如前所述，如果package_a改变了它的requirement，那么按照指定的requirements安装可能会出错。

所以需要更加智能的安装工具，在不明确指定子依赖的情况下，能选择满足所有条件的库安装。

#### Pipenv Introduction

``` Shell
pip install pipenv
```

安装了pipenv之后，就可以忘记pip了。因为它可以完全替代pip。它还会引入两个文件，一个Pipfile，替代requirements.txt，另一个是Pipfile.lock来执行deterministic builds。

Pipenv整合了pip和virtualenv，可以让我们以简单的方式使用。

比如创建一个virtual environment，在项目的根目录下，打开命令行，然后直接使用一下语句即可：

```Shell
pipenv shell
```

该语句会为该项目创建好一个同名虚拟环境，并在该项目文件夹下创建一个Pipfile文件，然后现在的命令行下已经处在该项目的虚拟环境下了。

Pipfile是替代 requirements.txt 的。其语法是TOML的，关于TOML，可以参考：[TOML 教程 - 可能是目前最好的配置文件格式](https://zhuanlan.zhihu.com/p/50412485) ，总之是一个比较新的配置文件的格式。

如果不小心创建错了，想要删除，则可以在同一个文件夹下执行下面语句：

```Shell
pipenv --rm
```

删除之后，Pipfile还在，如果不想要的话，手动删除即可。

接下来就可以安装包了。首先可以看看虚拟环境下有什么包已经安装了：

```Shell
pipenv graph
```

上述语句可以查看所有包依赖情况。

安装package语句类似如下形式：

```Shell
pipenv install numpy
```

一旦安装了一个package, pipenv就会再生成一个Pipfile.lock文件。

Pipfile.lock是确保 deterministic builds 的，是一个JSON文件。其中有指定子依赖的版本。

如果想要卸载安装的package，使用下面语句：

```Shell
pipenv uninstall numpy
```

卸载所有：

```Shell
pipenv uninstall --all
```

如果想要安装的是pytest，并且只想让它在测试开发的时候才用，生产时候不适用，可以加上--dev参数：

```Shell
 pipenv install pytest --dev
```

如果想要将库推到生产环境下，需要锁定下安装环境：

```Shell
pipenv lock
```

这样，Pipfile.lock就不要再手动修改了。以上就是利用pipenv的一些基本操作。

查看有哪些虚拟环境，对应项目在哪，可以使用下列语句：

```Shell
pipenv --venv
pipenv --where
```

退出当前的虚拟环境直接使用：

```Shell
deactivate
```

如果想重新进入某个虚拟环境，可以用pipenv --venv找到该环境，比如/home/owen/.local/share/virtualenvs/hydrus--ORegRFb，然后使用类似如下代码即可：

```Shell
. /home/owen/.local/share/virtualenvs/hydrus--ORegRFb/bin/activate
```

如果不需要将自己的项目打包发布，那么到这就ok了。

如果需要在IDE中配置虚拟环境，比如在Pycharm中配置，可以参考官网的步骤：[Pipenv environment](https://www.jetbrains.com/help/pycharm/pipenv.html)，但是我按照官方的没成功，因为没有.local/bin文件夹，这是因为我个人安装pipenv的时候，用的是anaconda下的pip，所以pipenv是安装在ananconda的文件夹下面了，在ananconda/bin文件夹下即可看到pipenv的可执行文件。

注意首先在项目文件夹下创建虚拟环境（项目根目录下终端执行 pipenv shell），然后再到pycharm的该项目下，将pipenv添加到interpreter路径中。

如果需要发布自己的项目，即做一个可以让别人import来使用的代码包，可以使用setup.py ，一般的工作流是这样的：

- setup.py
- install_requires keyword should include whatever the package “minimally needs to run correctly.”
- Pipfile
- Represents the concrete requirements for your package
- Pull the minimally required dependencies from setup.py by installing your package using Pipenv:
    - Use pipenv install '-e .'
    - That will result in a line in your Pipfile that looks something like "e1839a8" = {path = ".", editable = true}.
- Pipfile.lock
- Details for a reproducible environment generated from pipenv lock

#### pipenv 基本使用

这部分总结下前面introduction的内容，记录下如何生成pipfile和pipfile.lock，以及如何根据这些文件，快速在一个新环境下配置好依赖包。

这部分参考了：[Pipenv一键搭建python虚拟环境](https://www.jianshu.com/p/1441169b3dbe).

首先，安装pipenv。为了方便使用, 建议全局安装：

```Shell
pip install pipenv
```

进入你项目根目录文件夹，打开终端，执行：

```Shell
pipenv install
```

如果你已经有了pipfile和pipfile.lock文件，那么pipenv不仅会创建一个虚拟环境，还会安装pipfile.lock中的依赖包。如果没有，那pipenv会生成虚拟环境，并创建一个pipfile文件。

然后你每次使用pipenv安装依赖的时候，pipfile都会自动更新。

安装好你的依赖包，之后，使用：

```Shell
pipenv lock
```

就会生成你的pipfile.lock文件，这样你换到另一个环境下，也能很快地按照依赖包了。

如果需要卸载虚拟环境，进入项目根目录，使用下述方式：

```Shell
pipenv --rm
```

## Installing external services

前面说完了关于依赖包的安装，接着说说installing external services的事。

如果你存储数据到数据库中了，那么数据库很可能会用到一些服务，比如MySQL，Postgres，Redis等。比如要用Postgres，那么你就要在电脑上安装它。还要注意由于你可能使用的操作系统不同，因此安装的情况也不一样。所以，要每个情况单独处理。因为我个人暂时以科研用的数据为主，即通常见到的是 txt/csv/hdf5/netcdf等格式的文件，不太需要使用数据库，所以就不具体举例了。

总之，安装好外部程序之后，就可以运行自己的代码程序了。如果你开发web服务端软件的话，你就知道有一些关于微服务的事，你可能有很多服务，管理这些服务还需要一些设置的，不知道就算了，不重要。

总之，就是如果你需要很多外部程序，完成前面python及其环境的安装之后，还是有很多麻烦事。这也就是为什么要使用docker的motivation之一。

docker 部分放在了本文件夹下的 3-python-docker.md 文件中。
