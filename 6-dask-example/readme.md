# Dask 

Dask是一个帮助并行计算的工具。本文件夹下内容就尝试了解并使用 它。

Dask在大于内存的数据集上提供多核执行。

可以从高和低的角度理解dask：

- 高层集合： Dask提供了高级Array，Bag和DataFrame集合，它们模仿NumPy，lists和Pandas，但可以在不适合主内存的数据集上并行操作。Dask的高级集合是大型数据集的NumPy和Pandas的替代品。
- 底层调度： Dask提供了 dynamic task schedulers 动态任务调度程序，这些schedulers可以并行执行任务图（这块和pytorch中的计算图有些类似，先构建好要算的结构，最后再一气算）。这些执行引擎为上述高级集合提供支持，但也可以为用户定义的自定义工作负载提供支持。这些调度程序的等待时间很短（大约1毫秒），并且努力在较小的内存占用空间中运行计算。Dask的schedulers是在复杂情况中直接使用threading或 multiprocessing库或其他任务计划系统（例如Luigi或IPython paralle）的替代方法。

不同的用户在不同的级别上进行操作，但了解两者都有帮助。dask-tutorial教程将交错在高层次使用dask.array和 dask.dataframe（偶数部分）和低层次使用dask graphs and schedulers之间。

如果只在一台电脑上使用dask，那么没必要进行任何配置。在单个电脑上，有Single machine scheduler，很容易用。

关于分布式计算，根据[这篇blog](https://towardsdatascience.com/set-up-a-dask-cluster-for-distributed-machine-learning-31f587b1b553)的介绍，DASK下可以通过SSH快速地连接到多台没有统一管理的电脑，以迅速地学习使用；这种方法简单但是有很多限制，而更加灵活的方法则需要更复杂的操作，比如 利用Hadoop或者kubernates等。考虑到现在Kubernate这方面教程可能比较充足，另外比较常用的 jupyter 有 jupyterhub，结合kubernete 支持多人的访问应用，还有就是相关的云计算服务付费条件下比较容易获取，所以计划还是先从单机开始，了解Dask的基本用法，这样也便于后面的程序测试，然后再在单机上尝试一下kubernetes（或者直接上云也行），再调试dask程序，最后成功之后正式上云。

不过由于Kubernete的部分涉及的计算机方面内容较多，所以学习曲线还是相当陡峭的，故了解更多前期配置和单机上的例子之后再继续这部分内容。

本文件夹内容主要包括:

- 基本概念: 了解 Dask 是什么，基本工作原理什么样，如何使用来加速计算。
- 分布式: distributed scheduler使得将计算扩展倒分布式设置很容易，这部分内容就讨论如何在distributed scheduler上运行 Dask。distributed scheduler 是推荐的执行任务的引擎，即使是对单机器计算。
- Collections: 便捷的抽象结构以处理大数据
    - bag:函数式范式的Python迭代器，如func/iter-tools和toolz -将列表/生成器泛化到大数据
    - array: 海量多维数值数据，具有Numpy功能
    - dataframes: 海量的表格数据，带有Pandas功能

## Outline

1. 基本数据结构
2. Delayed - 用于并行化通用python代码的单函数方法

## 更多链接

*  Reference
    *  [Docs](https://dask.org/)
    *  [Examples](https://examples.dask.org/)
    *  [Code](https://github.com/dask/dask/)
    *  [Blog](https://blog.dask.org/)
    *  [Dask Tutorial](https://github.com/dask/dask-tutorial)
*  Ask for help
    *   [`dask`](http://stackoverflow.com/questions/tagged/dask) tag on Stack Overflow, for usage questions
    *   [github issues](https://github.com/dask/dask/issues/new) for bug reports and feature requests
    *   [gitter chat](https://gitter.im/dask/dask) for general, non-bug, discussion
    *   Attend a live tutorial
    