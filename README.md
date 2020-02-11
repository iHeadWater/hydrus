# hydrus

水资源water resource方面利用python做模型model、算法algorithm和开发software development等工作所需的基础**技能**树学习。了解本repo请从这里开始：[1-basic-envir/1-get-started.ipynb](https://github.com/OuyangWenyu/hydrus/blob/master/1-basic-envir/1-get-started.ipynb) 开始。本repo不是一个一步步照做的教程，而是基于个人学习记录改编的笔记，所以更多的作用是为像我一样非计算机科班，不需要从头到尾完全系统学习的同学提供参考，串联一些基本概念。本repo仍有很多不通畅之处，遇错见谅。

## 主要内容

主要涉及的内容有：

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

目前完整的conda安装列表如下所示，你可以直接用现在的environment.yml文件安装，不过要先修改下prefix，如果这个环境配置不懂可以先不管，直接从1-basic-envir/1-get-started.ipynb开始即可。因为最开始本项目是在python3.7下开始的，有些库在3.8及之后的版本安装也不是太顺利，所以就选择python3.7了。

```Shell
conda create --name hydrus python=3.7
conda activate hydrus
conda config --add channels conda-forge
# 修改.condarc：固定conda-forge 和 defaults 的顺序后，执行：
conda config --set channel_priority strict
conda install -c conda-forge jupyterlab
conda install -c conda-forge rpy2
conda install -c conda-forge numpy
conda install -c conda-forge pandas
conda install -c conda-forge scikit-learn
conda install -c conda-forge matplotlib
conda install -c conda-forge seaborn
conda install -c conda-forge cartopy
conda install -c conda-forge geopandas
conda install -c conda-forge geoplot
conda install -c conda-forge bokeh
conda install -c conda-forge bayesian-optimization
conda install -c conda-forge platypus-opt
conda install pytorch torchvision cpuonly -c pytorch
conda env export > environment.yml
```

本repo中可视化部分有涉及关于GIS方面内容，若对水文中gis的简单学习使用有兴趣，可以关注：[hydroGIS](https://github.com/OuyangWenyu/hydroGIS)。

本repo记录的都是纯技术方面内容，其中涉及到的基本常识可以关注[elks](https://github.com/OuyangWenyu/elks)。

更多内容可以关注：[awesome-python](https://github.com/vinta/awesome-python)。

## 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request
