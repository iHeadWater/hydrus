# LDAS

LDAS全称[Land Data Assimilation System](https://ldas.gsfc.nasa.gov/)，是由NASA的Goddard Space Flight Center的Hydrological Sciences Laboratory主导的，该实验室已经开发了多个LDAS，并持续贡献了LDAS的输出长达20余年。陆地同化系统(LDAS)旨在通过整合基于卫星和地面观测的数据产品，使用先进的land surface modeling and data assimilation技术生成高质量的fields of land surface states (e.g., soil moisture, temperature) 和fluxes (e.g., evapotranspiration, runoff)。

研发此系统的动机在于：

- 水循环的地表组成部分影响atmospheric和climatic过程，同时也控制着淡水的分布，这对陆地生物非常重要；
- 水和能量状态(e.g., soil moisture and temperature)及通量(e.g., evaporation and runoff)的时空变化的合理characterization对许多科学和实际工程应用十分关键，包括天气预报，农业预报，干旱和洪水风险评估，以及提升对陆气耦合和气候变化影响的理解；
- 大量陆地和空间观测和水及能量循环相关，但是它们通常包括误差或时空gaps或者它们可能不包括我们需要的信息(比如, snow cover observations do not tell us how much water the snow contains)。

LDAS的研发方法：

- LDAS使用物理过程的复杂数值模型来整合多源地面和空间观测系统的数据来生成物理上一致性的和时空连续的fields of water and energy states和fluxes；
- LDAS运用了水循环及能源循环方面的知识填补了gaps并最小化观测的误差；
- LDAS项目(NLDAS, GLDAS, FLDAS, NCA-LDAS)是Land Information System (LIS)地表模型软件的的几个实例项目，分别针对特定的领域和目的。

LDAS的用途：

- Water resources applications
- Drought and wetness monitoring
- Numerical weather prediction studies
- Water and energy cycle scientific investigations
- Interpretation of satellite and ground-based observations
- The Goddard Earth Sciences Data and Information Services Center serves LDAS data to over 1,000 unique users each month

## GLDAS

### 项目目标

GLDAS全称Global Land Data Assimilation System，吸收基于卫星和地面观测的数据产品, 使用先进的地表建模和数据同化技术以生产最优的fields of land surface states and fluxes。该软件由土地信息系统(LIS)姊妹项目简化及并行化，驱动多个离线(不与大气耦合)地表模型，集成大量基于观测的数据，在全球范围内以高分辨率运行(2.5度到1公里)，并且能够在近乎实时的情况下产生结果。

以1公里全球植被数据为基础，采用基于植被的tiling平铺法模拟亚网格尺度变化。土壤和高程参数是基于高分辨率的全球数据集。利用基于观测的降水和向下辐射产品以及来自大气数据同化系统的最佳可用分析来驱动模型。通过这些产品的相互比较和验证来确定最佳的驱动方案。数据同化技术将包括积雪和水当量、土壤湿度、地表温度和叶面积指数在内的基于卫星的水文产品纳入其中，目前正在作为NASA能源和水循环研究(NEWS)倡议资助的后续项目的一部分实施。

GLDAS提供的高质量的全球陆地表面fields支持了当前和拟议的几项天气和气候预测、水资源应用和水循环调查。该项目产生了大量的模型和观测、全球、地表气象数据、参数图和输出，其中包括1度和0.25度分辨率的1948年至今的Noah、CLM、VIC、Mosaic和流域地表模型的模型。

## NLDAS

因为CAMELS中有用到NLDAS的数据，因此本文暂时主要关注这部分的内容。

北美土地数据同化系统(NLDAS)的目标是构建质量可控、时空一致的地表模型(LSM)数据集，这些数据集来自可用的最佳观测和再分析，以支持建模活动。具体来说，该系统旨在减少土壤水分和能量的误差，这些误差经常出现在数值天气预报模型中，降低了预报的准确性。

NLDAS目前在北美中部(北纬25-53)范围，以1/8度网格、近乎实时(约4天延迟)、小时时间步长的方式运行。NLDAS历史每小时/每月的数据集可追溯到1979年1月。NLDAS通过基于日测量的降水分析(使用第二阶段雷达数据将时间分解到小时)、偏差校正的短波辐射和地表气象学重新分析构建了一个forcing数据集，以驱动四个不同的lsm产生地表通量、土壤湿度、积雪、水流等输出。

因此，谈到NLDAS数据集，一般指的是forcing数据集和output数据集

NLDAS是多个组织之间的合作项目。NLDAS是一个核心项目，得到NOAA气候项目办公室的建模、分析、预测和预测(MAPP)项目的支持。该项目的数据可以从NASA戈达德地球科学数据和信息服务中心([GES DISC](https://disc.gsfc.nasa.gov/datasets?keywords=NLDAS))以及[NCEP/EMC NLDAS](https://www.emc.ncep.noaa.gov/mmb/nldas/)网站获得。

另外本节主要参考了两篇文献：[The multi-institution North American Land Data Assimilation System (NLDAS): Utilizing multiple GCIP products and partners in a continental distributed hydrological modeling system](https://doi.org/10.1029/2003JD003823)和[Continental-scale water and energy flux analysis and validation for the North American Land Data Assimilation System project phase 2 (NLDAS-2): 1. Intercomparison and application of model products](https://doi.org/10.1029/2011JD016048)。

NLDAS全称为North American Land Data Assimilation System。本文从数据集制作动机，数据集制作方法和数据集基本组成几个方面对NLDAS数据集做简单介绍。

### NLDAS-1

#### NLDAS-1 forcing dataset

北美陆地数据同化系统(NLDAS-1)第一阶段的forcing数据从1996年8月1日至2007年12月31日，空间分辨率1/8度网格间距，时间分辨率是每小时。文件格式为WMO GRIB-1。

NLDAS-1 forcing数据集 (hourly, monthly average, and monthly climatology) 可以在[Get the Data](https://ldas.gsfc.nasa.gov/data)获取。

NLDAS-1 forcing主要数据源是NCEP（National Centers for Environmental Prediction）的Eta model-based Data Assimilation System (EDAS)，一个连续循环的北美4DDA系统。它利用3小时分析-预报周期，通过同化许多类型的观测，包括对地面压力和screen-level大气温度、湿度、U和V风分量的站内观测，得出大气状态。在40公里的网格上提供：后五个变量，以及地面向下短波和长波辐射，还有总对流降水的EDAS 3小时场，然后在空间上插值到NLDAS网格，在时间上插值到1小时。最后，考虑到NLDAS和EDAS的地表高程差异，使用标准的直减率(6.5 K/km)对气温和地表压力进行地形高度调整，然后对比湿度(保持原来的相对湿度)和向下的长波辐射(新气温、比湿度)进行调整。

基于GOES的太阳insolation为NLDAS-1提供了主要的insolation驱动(短波下至地表)。对于低于75度的天顶角，GOES insolation不能恢复，因此在昼/夜界线附近补充EDAS日晒。最后，基于GOES的产品套件，NLDAS-1 forcing文件中包括了光合作用活性辐射Photosynthetically Active Radiation (PAR)和表面亮度温度场。

美国大陆NLDAS-1 forcing降水被固定在NCEP的1/4度仅限测量的日降水分析中。在NLDAS-1中，这种日分析被插值到1/8度，然后通过应用从基于雷达的每小时4公里(WSR-88D)降水场导出的每小时权值，在时间上分解为每小时的值。后一种基于雷达的场仅用于计算分解权值，不改变日总降水量。最后，用NLDAS-1总降水量乘以EDAS对流降水量与EDAS总降水量的比值来估计对流降水。

对流有效位能Convective Available Potential Energy(CAPE)是forcing数据集的最后一个变量，也是由EDAS插值得到的。

据集应用用户定义的参数表来指示内容和参数编号。

下表显示了参数列表、它们的产品定义部分(PDS) id和单位：

- PDS_IDs:Short_Name:Full_Name [Unit]
- 63:ACPCPsfc:Convective precipitation hourly total [kg/m^2]
- 61:APCPsfc:Precipitation hourly total [kg/m^2]
- 118:BRTMPsfc:Surface brightness temperature from GOES-UMD Pinker [K]
- 157:CAPEsfc:Convective Available Potential Energy [J/kg]
- 205:DLWRFsfc:LW radiation flux downwards (surface) [W/m^2]
- 204:DSWRFsfc:SW radiation flux downwards (surface) [W/m^2]
- 101:PARsfc:PAR Photosynthetically Active Radiation from GOES-UMD Pinker [W/m^2]
- 201:PEDASsfc:Precipitation hourly total from EDAS [kg/m^2]
- 202:PRDARsfc:Precipitation hourly total from StageII [kg/m^2]
- 1:PRESsfc:Surface pressure [Pa]
- 206:RGOESsfc:SW radiation flux downwards (surface) from GOES-UMD Pinker [W/m^2]
- 51:SPFH2m:2-m above ground Specific humidity [kg/kg]
- 11:TMP2m:2-m above ground Temperature [K]
- 33:UGRD10m:10-m above ground Zonal wind speed [m/s]
- 34:VGRD10m:10-m above ground Meridional wind speed [m/s]

#### NLDAS-1 model datasets

模型数据的网格间距为1/8度，时间范围为1996年10月1日至2007年12月31日，时间分辨率是每小时。文件格式为WMO GRIB-1。

NLDAS-1中用到的地表模型LSMs有: Mosaic, Noah, SAC, and VIC.  不过NLDAS-1模型数据集不对公众开放了。

NLDAS validation from NLDAS Phase 1 is available from NOAA/NCEP/EMC.

### NLDAS-2

#### NLDAS-2 forcing dataset

NADAS-2数据集从1979年1月1日至今，时间分辨率是**每小时**；数据的网格间距为**1/8度**。文件格式为WMO **GRIB-1**。

[GRIB-1](https://www.nco.ncep.noaa.gov/pmb/docs/on388/)是NCEP(National Centers for Environment Prediction)的一种数据格式。句首的链接里有GRIB数据的用户指导。对于给定的物理变量，GRIB数据约定分配如下:GRIB参数ID的惟一数字ID(范围1-255)、惟一的字母数字缩写(最多8个字符)和物理单位。详情可参考官网。NLDAS-2地表forcing文件和土地模型输出文件将使用[GRIB-1参数表130](https://www.nco.ncep.noaa.gov/pmb/docs/on388/table2.html#TABLE130)，该表是面向陆地/水文建模和陆地/水文物理的。

NLDAS-2 forcing数据集(每小时、每月平均和每月气候学)可从官网顶部[“获取数据”链接](https://ldas.gsfc.nasa.gov/data)获得。

NLDAS-2的空间范围、空间分辨率、计算网格、地形高度和land mask与NLDAS-1相同，可参考文献[Mitchell et al. (2004)](https://doi.org/10.1029/2003JD003823) 2.1节。

NLDAS-2的非降水地表forcing fields来源于NCEP North American Regional Reanalysis([NARR](https://www.emc.ncep.noaa.gov/mmb/rreanl/))的分析fields。NARR包括:1)从1979年1月开始的retrospective数据集，2)NCEP的每日更新。每日更新提供了一个实时的NARR延续，称为区域气候数据同化系统，或R-CDAS。

NARR分析领域为32公里空间分辨率和3小时时间频率。利用NARR场产生NLDAS-2 forcing场的方法是在NLDAS 1/8度网格的精细分辨率上进行空间插值，然后在时间上分解成NLDAS-2的小时级频率。另外，对地表压力场、地表向下长波辐射场、近地表气温场和近地表比湿度场进行垂直调整，以解释地形高度NARR场和NLDAS场的垂直差异。这一垂直调整适用传统的气温垂直递减率6.5 K/km。NLDAS-1采用的空间插值、时间分解和垂直调整的细节可参考文献[Cosgrove et al. (2003)](https://doi.org/10.1029/2002JD003118)。

NLDAS-2的每小时地表forcing场分为两个GRIB文件，“文件A”和“文件B”。这与NLDAS-1不同，NLDAS-1只有一个 小时forcing的文件。

FORCING文件A:

文件A是主要的forcing文件. 它包括11个fields：

- U wind component (m/s) at 10 meters above the surface
- V wind component (m/s) at 10 meters above the surface
- air temperature (K) ** at 2 meters above the surface
- specific humidity (kg/kg) ** at 2 meters above the surface
- surface pressure (Pa) **
- surface downward longwave radiation (W/m^2) **
- surface downward shortwave radiation (W/m^2) -- bias-corrected (see Appendix B)
- precipitation hourly total (kg/m^2)
- fraction of total precipitation that is convective (no units): from NARR
- CAPE: Convective Available Potential Energy (J/kg): from NARR
- potential evaporation (kg/m^2): from NARR

以上内容中的"**"表示应用前述垂直调整的field。

前八个fields是传统的land-surface forcing fields，比如在PILPS (Project for Intercomparison of Land-Surface Process Schemes)和GSWP (Global Soil Wetness Project).

A文件中的地表下短波辐射场是一个bias-corrected field ，其中对NARR地表下短波辐射采用了bias-corrected算法。偏置校正可参考文献[Pinker et al. (2003)](https://doi.org/10.1029/2002JD003301)，和[网页附录B](https://ldas.gsfc.nasa.gov/nldas/v2/forcing#AppendixB)。

A文件中的降水场不是NARR降水forcing，而是在NLDAS网格上直接进行的仅限计量的CPC日降水分析的时间分解的产物，包括基于广泛应用的PRISM气候学的orographic adjustment。产生这种降水forcing的方法和源数据集，包括从每日分析到每小时间隔的时间分解的细节，在[网页附录C](https://ldas.gsfc.nasa.gov/nldas/v2/forcing#AppendixC)中可查看详情。

文件A中的field给出的对流降水总量的比例是根据文件B中两个NARR降水fields估计的: NARR总降水和NARR对流降水(后者小于或等于NARR总降水和可以零)。一些陆地模型使用A文件中总降水的对流部分和/或CAPE场来估计总降水的次网格空间变异性。

A文件中的potential evaporation field是在NARR中使用文献[Mahrt和Ek(1984)](https://doi.org/10.1175/1520-0450(1984)023%3C0222:TIOASO%3E2.0.CO;2)改进的Penman scheme计算出来的。一些陆地模型(如SAC模型)需要潜在蒸发，这些模型需要潜在蒸发作为输入forcing。

FORCING文件B:

地表气动力传导surface aerodynamic conductance是地表模拟中最基本的物理过程之一，它反映了地表与上覆大气之间输送热量和水分的近地表垂直湍流的强度。

在边界层数值模拟和陆面数值模拟中，对surface aerodynamic conductance进行数值模拟的方法很多。NLDAS-1的结果显示，四种不同的土地模型在模拟的暖季surface aerodynamic conductance日变化幅度上存在惊人的差异。

大陆尺度地表模拟研究中采用的2米温湿度和10米风场是主流NWP中心数据同化/分析系统的典型产物。这种分析/同化系统中2米和10米的水平在给定的NWP中心的NWP同化模型背景中很少是明确的水平。因此，NWP中心从同化模型的最低预后水平诊断这些2米和10米的区域。2米高的温度和湿度field和10米风field的推导基于以下基础完成:

- A)相同的字段在预后模型的最低水平,通常远高于10米级别(例如,20 - 200米以上)
- B)给定模型的aerodynamic conductance的方法建模“表层”,也被称为“常通量层”——比如将给定模型的特定方法应用于物理实体，如动量的表面粗糙度长度、热的表面粗糙度长度、表层稳定性函数(如相似剖面函数)和表层参数(如混合长度)。

NLDAS-2因此提供第二个forcing文件——文件B,表面温度,湿度,和风fields的表示不是在2米和10米以上的高度NLDAS地形,而是在同一高度以上NLDAS地形。这个高度是上，NARR地形NARR预后水平最低的同化系统(即相同的高度模型地形预后水平最低的中尺度Eta模型,这是NARR的同化模型)。我们将后一个高度表示为“H”，这个高度H在水平方向上随空间变化。这种方法的动机是允许NLDAS-2中的陆地模型从表面forcing场计算它们的aerodynamic conductance，这些地面forcing场与aerodynamic conductance方法应用程序明显更独立(尽管不是完全独立)。

forcing文件B包含10个fields:

- U wind component (m/s) at H meters above the surface
- V wind component (m/s) at H meters above the surface
- air temperature (K) ** at H meters above the surface
- specific humidity (kg/kg) ** at H meters above the surface
- pressure (Pa) ** at H meters above the surface
- height H above the surface (m)
- NARR surface downward shortwave radiation (W/m^2) -- without bias-correction
- NARR precipitation hourly total (kg/m^2)
- NARR convective precipitation hourly total (kg/m^2)
- NARR aerodynamic conductance (m/s)

提供Fields 7-10还有其他如下原因：提供7和8是为了允许进行土地模拟敏感性试验，在这些试验中，文件A的太阳辐射场和降水场被直接从NARR获得的精度较低的对应场所代替。8和9是NARR field，用于推导a文件中“对流降水的分式”场。场10是由NARR得到的气动导度，可以与NLDAS-2中各陆地模型独立计算的气动导度进行比较

#### NLDAS-2 model datasets

本页描述北美陆地数据同化系统(NLDAS-2)第2阶段的模型数据。从1979年1月2日至今，数据的网格间距和范围为1/8度。时间分辨率是每小时。文件格式为WMO GRIB-1。

在NLDAS-2期间，目前有四种陆地表面模型可用数据。它们是:

- Mosaic
- Noah-2.8
- SAC
- VIC-4.0.4

NLDAS-2 Validation Information：

- Soil moisture evaluation
- Soil temperature evaluation
- Evapotranspiration evaluation
- Runoff/streamflow evaluation
- Snow evaluation
