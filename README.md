# hydrus

水资源water resource方面利用python做模型model、算法algorithm和开发software development等工作所需的基础**技能**树学习。

## 主要内容

本repo不是一个一步步照做的教程，而是基于个人学习记录改编的笔记，所以更多的作用是为像我一样非计算机科班，不需要从头到尾完全系统学习的同学提供参考，串联一些基本概念。本repo仍有很多不通畅之处，遇错见谅。继续阅读可以从这里开始：[1-basic-envir/1-get-started.ipynb](https://github.com/OuyangWenyu/hydrus/blob/master/1-basic-envir/1-get-started.ipynb)。

主要涉及的内容（持续更新中）有：

- 1.Python基础
    - 基础环境配置
    - python基础
- 2.常用科学计算库
    - numpy
    - pandas
    - sklearn
- 3.可视化
    - 静态可视化
    - GIS数据可视化
    - 交互式可视化
- 4.常用算法库示例
    - 优化计算实例
- 5.神经网络算法示例
    - 常用深度学习框架
    - 一点实例
- 6.科研数据获取
    - 数据爬取

目前完整的conda安装列表如下所示，你可以直接用现在的environment.yml文件安装，如果这个环境配置不成功，可以直接运行下面的安装语句。

```Shell
conda create --name hydrus python=3.7
conda activate hydrus
conda config --add channels conda-forge
# 修改.condarc：固定conda-forge 和 defaults 的顺序后，执行：
conda config --set channel_priority strict
conda install -c conda-forge jupyterlab
conda install -c conda-forge flask
conda install -c conda-forge numpy
conda install -c conda-forge pandas
conda install -c conda-forge xlrd
conda install -c conda-forge xarray
conda install -c conda-forge dask
conda install -c conda-forge scikit-learn
conda install -c conda-forge matplotlib
conda install -c conda-forge seaborn
conda install -c conda-forge cartopy
conda install -c conda-forge geopandas
conda install -c conda-forge geoplot
conda install -c conda-forge plotly=4.5.2
conda install -c plotly plotly-geo=1.0.0
conda install -c conda-forge bayesian-optimization
conda install -c conda-forge platypus-opt
# 如果直接使用cpu版，本repo中暂时就只使用cpu了
conda install pytorch torchvision cpuonly -c pytorch
# 如果是GPU，首先要根据 5-basic-pytorch-tensorflow/1-get-started.ipynb 中内容配置好机器
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
conda install skorch
conda env export > environment.yml
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
