# hydrus

水文水资源（Hydrology and Water Resources）方面利用python做模型model、算法algorithm等科学计算工作所需的基础技能树学习。

## 主要内容

本repo不是一个一步步照做的教程，而是基于个人学习记录改编的笔记，作用是为像我一样非计算机相关专业，不需要从头到尾完全系统学习的同学提供参考，串联某些基本概念。本repo仍有很多不通畅之处，遇错见谅。继续阅读可以从这里开始：[1-basic-envir/1-get-started.ipynb](https://github.com/OuyangWenyu/hydrus/blob/master/1-basic-envir/1-get-started.ipynb)。

主要涉及的内容（持续更新中）有：

1. Python基础
    - 基础环境配置
    - python基础
2. 常用科学计算库
    - numpy
    - pandas
    - sklearn
3. 可视化
    - 静态可视化
    - GIS数据可视化
    - 交互式可视化
4. 常用算法库示例
    - 优化计算实例
5. 神经网络算法示例
    - 常用深度学习框架
    - 一点实例
6. 科研数据获取
    - 数据爬取
7. 并行计算
    - python并行基础

本项目目前主要在windows 10系统下测试运行，可以直接使用如下语句安装依赖包（安装时需耐心等待若干分钟）。没有安装conda的话需要先参考 https://zhuanlan.zhihu.com/p/102564715 安装miniconda并配置好环境变量，之后再运行下面的语句。另外，推荐使用[windows终端](https://docs.microsoft.com/zh-cn/windows/terminal/)执行下面代码。

```Shell
conda env create -f environment.yml
```

安装依赖完成后，在命令行执行下面语句，默认浏览器会自动打开jupyter lab，就可以运行本repo中的程序啦：

```Shell
conda activate hydrus
jupyter lab
```

本repo中可视化部分有涉及关于GIS方面内容，若对水文中gis的简单学习使用有兴趣，可以关注：[hydroGIS](https://github.com/OuyangWenyu/hydroGIS)。

本repo记录的都是纯技术方面内容，其中涉及到的基本常识可以关注[elks](https://github.com/OuyangWenyu/elks)。

**推荐**一些学科科研相关的python学习资料：

- [Earth Lab - Earth Data Science](https://www.earthdatascience.org/)
- [Software Carpentry – Teaching Basic Lab Skills for Scientific Computing](https://software-carpentry.org/lessons/index.html)
- [NumFOCUS](https://numfocus.org/)

更多内容可以关注：[awesome-python](https://github.com/vinta/awesome-python)。

## 参与贡献

1. Fork 本项目
2. 新建 xxx 分支
3. 提交代码
4. 新建 Pull Request
