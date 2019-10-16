# CAMELS

CAMELS数据[官网](https://ral.ucar.edu/solutions/products/camels)推荐了两篇HESS的文献，这两篇文章详细地介绍了CAMELS数据的来龙去脉。这里简要整理一下两篇文献主要内容。

## 背景

制作CAMELS数据最开始的目的在于提供一个模型性能的benchmark。

随着数据的增多和计算能力的增强，基于大样本数据开展水文研究越发常见，这里面也诞生了一批水文气象数据集。比如，MOPEX（Model Parameter Estimation Project）数据集可以提供CONUS上438个流域的观测径流和一些水文气象数据。但是，现在local的model很多（有depth），但是却少有general的model（有breadth的）。

为实现general model，整理了水文气象大数据集和建模工具来帮助理解水文模型性能的区域变化。

该数据集来自多个美国机构和研究实验室，能提供高质量高保真的数据。包括：

- 671个流域1980-2010年的多空间尺度的日驱动数据
- 日径流数据
- 基本元数据（位置、高程、大小、shapefile等）
- benchmark model performance：包括最后率定的模型参数集和各流域模型输出时间序列和相关图像。

关于模型部分，模型采用的是耦合Snow-17和SAC-SMA（Sacramento Soil Moisture Accounting）的水文模型。

## N15数据集

因为这里重点关注的是数据集的性能，因此模型的benchmark待后续有接触的时候再补充，这里只对数据集展开说明。

CAMELS数据集的前期版本是2015年那篇HESS上的文献介绍的，简称其为N15数据集。

对该数据集的介绍主要围绕制作过程展开。

### 选择流域

USGS-II数据集包括有超过9000个站点的地理空间信息。其中有一部分reference gages（详情可参考GAGES文件夹下的文档）代表了一部分minimal human disturbance的站点。在这一部分内，有一些作为HCDN（Hydro-Climate Data Network）数据集的后续版，称为HCDN-2009。

这部分数据集满足一下标准：

- 至少20年数据
- 是GAGES-II的reference gages
- 根据NLCD（National Land Cover Database）-2011数据，有少于5%的imperviousness
- 通过了local水科学中心评价的人类活动影响调查

最终得到了671个流域。分布如下图所示。
![671 basins](671basins.png)

这671个流域覆盖全美，有很广泛的水文气候条件。东南温暖湿润的流域、西南炎热干旱的流域、西北凉爽湿润的流域和东北干燥寒冷的流域都包含在内。

### 驱动数据与径流数据

因为水文模型有不同尺度空间信息作为输入，包括流域级entire watershed（lumped）、elevation bands、水文相应单元hydrologic response units（HRUs）或者grids。所以驱动数据也相应的计算到不同尺度上。

流域空间配置根据MoWS（USGS Modeling of Watershed Systems）组的水文模型的geospatial fabric建立。geospatial fabric是国家水文数据National Hydrography Data set的面向流域分析，NHD包含了USGS的径流测站点，水文相应单元边界和径流分割，而geospatial fabric则包含了其中的需要的站点及其上游流域面积和流域HRUs；

DEM数据作用于geospatial fabric数据上以创建每个流域的高程轮廓shape文件；

用由USGS的Center for Integrated Data Analytics（CIDA）开发的USGS Geo Data Portal（GDP）来生产基于面积权重的驱动数据；

Daymet数据被选为主要的gridded气象数据集来推求径流模拟所需的驱动数据。Daymet数据是日尺度的1km*1km网格的覆盖全美大陆数据集。包括温度、降雨、短波辐射、湿度、日长等；

PET数据Daymet没有，所以使用Priestly-Taylor方法进行估算；

National Land Data Assimilation System（NLDAS）12km网格数据用来提供basin lumped尺度的日驱动数据；

HCDN-2009 gages的日径流数据从USGS官网获取。

其余关于数据的细节就不再表述了，详情可参考原文。

## CAMELS数据集

CAMELS数据集全称为Catchment Attributes and Meteorology for Large-sample Studies。

相比于前述N15数据集，CAMELS数据集为671个站点主要补充了一些新属性数据集。主要六类属性：

- topography
- climate
- streamflow
- land cover
- soil
- geology

这些新的属性集和N15数据集一起构成了CAMELS数据集。

这部分的介绍从扩充N15数据集的动机及扩充内容，和CAMELS最终数据集构成两大方面展开。

### from N15 to CAMELS

流域属性是landscape的descriptors。为了表达流域的多方面，流域属性要覆盖多方面。

关于流域属性，一个成果比较丰富的方向是探索不同流域属性之间的内在联系。比如气候和地形如何影响植物生产。

流域属性还可以作为量化流域相似性的标准方法。

还有很多用流域属性来反映模型中landscape结构的研究。比如通过流域属性推求模型参数。在PUB问题上实现水文建模。还有的不只是反映到参数上，也有应用到模型结构上的。

现在大样本流域能提供更多的关于流域属性的洞察。研究不同gradients的changes，更好地从流域行为中分离出流域属性的作用。大数据还使得探索流域属性和空间模式之间关系成为可能。

构建CAMELS是为了达到以下目的：

- 使空间数据匹配流域尺度。不同的数据集有不同的空间配置，通过建立流域尺度的属性集可以拿来简化属性之间关系评估；
- 推求气候indices和水文signatures，减少水文气候数据集的维度，同时尽可能保留最多信息，即让气象驱动和径流日时间序列有丰富的信息，有通过信息的总结让流域比较更容易；
- 描述流域的land cover，soil和geology。一个目的是更好的评估数据集能多好地获取landscape关于水量存储和传输的特征
- 明确地理属性的不确定性，基于流域属性的可靠性来帮助流域选择
- 为了保证数据空间一致性，减少仅使用数据集生成模拟区域变化的风险。

#### 数据项

- Location and topography
- Climate indices
- Hydrological signatures
- Land cover characteristics
- Soil characteristics
- Geological characteristics
