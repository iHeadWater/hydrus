# hydrus

水文水资源（Hydrology and Water Resources）方面利用python做模型model、算法algorithm等科学计算工作所需的基础技能树学习。

## 主要内容

本repo不是一个一步步照做的教程，而是基于个人学习记录改编的笔记，作用是为像我一样非计算机相关专业，不需要从头到尾完全系统学习的同学提供参考，串联某些基本概念。本repo目前仍在编辑中，一直会有更新，内容常会做写调整；且可能仍有一些不通畅之处，遇错见谅。

主要涉及的内容（持续更新中）有：

1. Python基础
    - [基础环境配置](https://github.com/OuyangWenyu/hydrus/tree/master/1-basic-envir)
    - [python基础](https://github.com/OuyangWenyu/hydrus/tree/master/1-learn-python)
2. 常用科学计算库
    - [numpy](https://github.com/OuyangWenyu/hydrus/tree/master/2-numpy-examples)
    - [pandas](https://github.com/OuyangWenyu/hydrus/tree/master/2-pandas-examples)
    - [scipy](https://github.com/OuyangWenyu/hydrus/tree/master/2-scipy-example)
    - [xarray](https://github.com/OuyangWenyu/hydrus/tree/master/2-xarray-example)
3. 可视化
    - [静态可视化](https://github.com/OuyangWenyu/hydrus/tree/master/3-basic-pyviz)
    - [GIS数据可视化](https://github.com/OuyangWenyu/hydrus/tree/master/3-gis-pyviz)
    - [交互式可视化](https://github.com/OuyangWenyu/hydrus/tree/master/3-interactive-pyviz)
4. 常用算法库示例
    - [优化计算实例](https://github.com/OuyangWenyu/hydrus/tree/master/4-optimization-example)
    - [机器学习sklearn](https://github.com/OuyangWenyu/hydrus/tree/master/4-sklearn-example)
5. 加速科学计算
    - [python并行基础](https://github.com/OuyangWenyu/hydrus/tree/master/5-basic-parallel)
    - [dask](https://github.com/OuyangWenyu/hydrus/tree/master/5-dask-example)
    - [numba](https://github.com/OuyangWenyu/hydrus/tree/master/5-numba-example)
6. 科研数据获取
    - [下载数据](https://github.com/OuyangWenyu/hydrus/tree/master/6-download-data)
    
## 运行本repo步骤

下载本repo，需要本地预先下载安装好git，如果没有安装那么在[此处](https://git-scm.com/downloads)下载，并点击下载好的安装包安装，安装过程中全部选择默认配置即可。

本项目目前主要在windows 10系统下测试运行，可以直接使用如下语句安装依赖包（安装时请耐心等待，可能需要较长时间 ~10mins）。

没有安装conda的话需要先参考 https://zhuanlan.zhihu.com/p/102564715 安装miniconda并配置好环境变量，之后再运行下面的语句。推荐使用[windows终端](https://docs.microsoft.com/zh-cn/windows/terminal/)执行下面代码。

```Shell
# terminal 里 启动cmd
cmd.exe
# 下载本repo
git clone https://github.com/OuyangWenyu/hydrus.git
# 或者fork为自己的repo后，从自己的github处下载
# 进入本项目根目录
cd hydrus
conda env create -f environment.yml
# 本repo涉及的库较多，所以安装过程比较慢，为了确保环境安装正确，请耐心等待
```

安装依赖完成后，在命令行执行下面语句，默认浏览器会自动打开jupyter lab，就可以运行本repo中的程序啦：

```Shell
conda activate hydrus
jupyter lab
```

可以从这里开始：[1-basic-envir](https://github.com/OuyangWenyu/hydrus/blob/master/1-basic-envir)，如果不熟悉刚刚提到的git和jupyter lab，1-basic-envir/1-get-started.md里也有介绍。

注意如果之前已经fork过本repo了，现在本repo已经更新，而自己那边还没有过同步，那么版本就会落后于本repo，所以需要注意和上游保持一致，同步方法请参考[这里](https://github.com/waterDLut/hydrus/blob/master/1-basic-envir/1-get-started.md#fork%E5%90%8E%E5%90%8C%E6%AD%A5%E6%BA%90%E7%9A%84%E6%96%B0%E6%9B%B4%E6%96%B0%E5%86%85%E5%AE%B9)。

注意，本repo中可视化部分有涉及关于GIS方面内容，若对水文中gis的简单学习使用有兴趣，可以关注：[hydroGIS](https://github.com/OuyangWenyu/hydroGIS)。

另外，算法库示例中没有包括深度学习神经网络，这部分可以关注：[hydro-dl-basic](https://github.com/waterDLut/hydro-dl-basic)

最后**推荐**一些学科科研相关的python学习资料：

- [Earth Lab - Earth Data Science](https://www.earthdatascience.org/)
- [Software Carpentry – Teaching Basic Lab Skills for Scientific Computing](https://software-carpentry.org/lessons/index.html)
- [NumFOCUS](https://numfocus.org/)

更多内容可以关注：[awesome-python](https://github.com/vinta/awesome-python)。

## 参与贡献

1. Fork 本项目
2. 新建 xxx 分支
3. 提交代码
4. 新建 Pull Request
