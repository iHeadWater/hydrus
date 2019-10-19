# HCDN

在了解GAGES和CAMELS等数据集的过程中，都会出现HCDN的名称。因此有必要补充一些对HCDN的认识。

本文内容主要参考两篇reports。分别是[HYDRO-CLIMATIC DATA NETWORK (HCDN):
A U. S. GEOLOGICAL SURVEY STREAMFLOW DATA SET FOR THE UNITED STATES FOR THE STUDY OF CLIMATE VARIATIONS, 1874-1988](https://pubs.er.usgs.gov/publication/ofr92129)和[USGS Hydro-Climatic Data Network 2009 (HCDN-2009)](https://pubs.usgs.gov/fs/2012/3047/)

HCDN是USGS Global Change Hydrology Program项目的成果，也是USGS制作的。1992年有一个版本，后来2009年又有了更新。因此，接下来分为两部分，从数据集制作动机，制作基本方法和结果几个方面介绍HCDN。

## HCDN-1992

气候变化对水资源影响是很关键的社会问题。因此，气候变化会影响极端水文事件的时空分布和季节性水平衡。通过研究已知过去气象条件下的水文特性，可以更好地了解一定气候变化下的效应。反过来，通过过去水文现象的记录，也可以发现什么时候气象通量模式发生了变化而因此气候也发生了变化。

径流和水文条件及气象通量之间的关系是十分复杂的。径流量记录反映当前气候变化的能力取决于在记录期间没有任何其他主要原因会从根本上改变径流量的模式。但是径流这一水文过程很容易被人类活动影响，这样其模式就会发生变化。不过如果气候模式变化前后都有相同的人类活动影响，那么气候影响模式也是可以分析的。

气候变化对水资源的一个重要影响是气候变化导致的降雨和温度季节性偏移会使得水文事件也发生季节性转移，而要观察到季节性的变化，径流记录的时间单位要足够小，至少要小于变化的时间尺度，因此其数据时间尺度至多只能到月尺度，并且同时还要使得人类活动的影响在其时间尺度上是可忽略的。

为了刻画气候变化较大的上世纪的径流变化，并将其与当时的气象条件进行比较分析，有必要组织一系列适合研究的径流数据。HCDN数据集就是在此背景下诞生的。

HCDN整合了很多个数据集。然后根据一套选择的标准：

- 电子形式数据；
- 覆盖全美；
- 记录至少20年；
- 记录准确；
- 至少相比于月均径流值人类活动的影响可以忽略；
- 标准观测数据。

最后选出了1659个站点到HCDN数据集。径流数据主要来自USGS的National Water Storage and Retrieval Syetem数据集，此外还包括流域信息、各类统计信息等。

## HCDN-2009

从HCDN第一版本发行以来，已经过了20余年，很多站点的情况已经发生变化，因此是否还满足当初的条件需要重新确认，数据集的更新也就是必须完成的。

由于USGS National Water-Quality Assessment(NAWQA) Program已经完成了识别reference sites的工作，编制了GAGES数据，并且在2011年更新为了GAGES-II数据，为了保持reference的一致，所以HCDN直接作为GAGES-II的reference子集的一个子集。这个子集的站点需要满足以下标准：

- 根据GAGES-II的标准，是reference的site；
- 有至少20年连续的完整径流数据，并且是经过2009年的；
- 根据Federal National Land Cover Data（NLCD） 2006，少于5%的不透水面积；
- 通过State USGS Water Science Centers的review。

最终HCDN-2009包含了743个stations。HCDN-2009数据能反映对气候敏感性，也反映对气象条件的敏感性。
