# GAGES(II)数据集概览

GAGES全称为Geospatial Attributes of Gages for Evaluating Streamflow，是一个径流测量数据库，用以评估美国大陆自然和人工改变下的径流条件。GAGES现在已经有了第二版，这里首先根据GAGES官方说明文档，看看GAGES都有什么数据，然后再根据GAGESII对GAGES的扩展说明详解GAGESII。

## GAGES数据集

本文这一小节主要内容是结合GAGES数据集对Ecological Archives E091-045-D1文档，即GAGES数据集说明文档进行翻译理解。

### METADATA CLASS I. DATA SET DESCRIPTORS

首先是元数据的描述。

[gages_basinchar_sep3_09.zip](http://esapubs.org/Archive/ecol/E091/045/gages_basinchar_sept3_09.zip)：该文件包括了25个使用制表符分隔号制作的txt文件，代表了流域的watershed和站点sites的特性。每个txt文件包括变量描述，每个excel文件表示了hydrologic disturbance index score calculation。这25个文件每一个都包含6785条记录，每个代表一个stream gage，由唯一的GAGE_ID标识符进行标识。

对变量的描述都在gages_basinchar_sep3_09.txt中，它包含375条记录，每一条对应一个变量。
变量类型包括：

- BasinID：指流域的一些基本属性，包括有GAGE_ID, Name, DRN_SQKM 流域面积单位平方公里, HUC , LATITUDE, LONGITUDE等；
- Bas_Classif：流域的一些额外属性，比如是否是reference的（reference的含义参考文献），再比如HYDRO_DISTURB_INDEX是基于7个变量综合计算得到的hydrologic disturbance index 分数；
- Bas_Morph:BAS_COMPACTNESS=流域的面积与周长平方比，越大的数表示流域越compact；
- Census_Block:表示流域内人口密度，基于block数据的普查；
- Census_County:表示流域内人口密度，基于county数据的普查
- Climate:关于气候的统计性质的属性，比如PPTAVG_SITE表示流域平均年降雨，还有关于气温、湿度、蒸发等各个时间尺度、维度的统计属性；
- Geology:主要是流域最主要地形的描述；
- Hydro:水文属性或统计相关的数据，比如河流分级最大级数，基流系数等属性，比如各月平均径流等统计属性；
- HydroMod_Dams:流域Dam的一些统计数据，包括Dam数，Dam密度，Dam蓄水量等；
- HydroMod_Other:其他类型的人工影响的数据，包括渠道等的统计数据；
- Infrastructure:道路密度和不透水面积比例；
- LandScape_Pat:流域内未被人类开发的土地的占比系数
- LC01_Basin:流域内各个土地利用类型的比例，包括城市、森林、农业、水域等等；
- LC_Change92_01:这类数据反映92年到01年间的土地利用的变化情况；
- LC01_Mains100:河流中心主干线左右100m缓冲区的土地利用情况；
- LC01_Mains800:河流中心主干线左右800m缓冲区的土地利用情况；
- LC01_Rip100:河流边缘100m缓冲区的土地利用情况；
- LC01_Rip800:河流边缘800m缓冲区的土地利用情况；
- Nutrient_App:化肥和动物粪便得到的氮和磷等的估计量；
- Pest_App:农药的估计量；
- Prot_Areas:流域保护区的比例；
- Reach:河道的编码；
- Regions:gage站点所在位置所属的各类划分方式得到的region，比如ecoregion，HUC 8等；
- Soils:各类型土地的土壤情况及各类统计数据；
- Topo:流域高程、坡度等地形数据。

disturb_index6785_sept3_09.xls文件提供了disturbance index scores是如何得到的。在results部分显示了每个站点的score都是七项数据的总和；
在notes部分，说明了如何计算的。
七项数据分别是：

- FRESHW_WITHDRAWAL表示每年每平方公里被取走的淡水量；
- MAJ_DDENS_2006指每100平方公里上的dam数；
- 2006_STOR - pre1950_STOR指50年到06年水库蓄水量的变化；
- sum_percent_canals_artif是人工河流的比例；
- DIS_ADJ_NEAREST_MAJ_NPDES中，NPDES表示National Pollutant Discharge Elimination System，所以该项意思是到最近的NPDES站点的距离，数字越大表示越有可能干扰；
- ROADS_KM_SQ_KM指道路密度；
- FRAGUN_BASIN from NLCD01代表未开发区域的比重。

剩余的25个文件则分别对应gages_basinchar_sep3_09.txt中描述的25个类型，详细介绍每个站点的这25类数据情况。

接下来对这些数据再分别展开叙述。

### CLASS II. RESERACH ORIGIN DESCRIPTORS

数据集的时间范围是1950-2007年。
研究GAGES数据集的主要目的是划分流域并且编辑全美的站点GIS信息。其次想要找出哪些站点是受人类影响活动较显著的。特别地，想要通过GAGES的工作找出哪些是受人类活动影响小的站点。
为此，整合了这么样的一个大数据集，描述流域自然和人为的条件及特征。介绍GAGES的这个报告的目的是描述这样一个数据集的收集方法，并提供获取数据的链接。

研究方法：

#### Gage screening and watershed boundary delineation

筛选数据。包括时间上，要有足够长；其次，流域边界要在美国境内；然后人造河流上的测点也都排除了；超大流域上的站点也排除了；最后是要能准确地划分出流域边界。

#### Calculation of watershed characteristics

使用NHDPlus 100k 尺度径流数据集来描述径流。变量包括：环境的（气候、土壤、地理、水文、地形），landscape（土地利用、ecoregions），人类活动影响特性的（基础设施、人口、当前和历史上存在的大坝、渠道、污染径流站）。gages_variable_desc_sept3_09.txt文件中都已提供详细的元数据来说明了。

定义了mainstem streamline：从NHDPlus河流数据集中可以确定的距离流量计上游很远的主要排水渠道。也就是从一个站点开始，向上游追溯，直到在源头无法确定哪一个是主干，如图所示。
![GAGES](mainstem.jpg)

在5中空间尺度上，计算土地利用类型包括整个流域，以及河道中心100及800米缓冲区，和河道边缘100-800m缓冲区。

#### Identification of reference stream gages

水文上讲reference conditions可能指代的是“least disturbed”，也可能是“best attainable”。
有很多影响河流flow regime的人类活动，包括dam，diversions，urbanization和drainage modifications，提和渠化，地下水抽水泵，以及森林退化。
有些地方，这些因素已经形成永久性影响，几乎所有河段都是disturbed；而在另一些区域，还存着undisturbed流域。
有几种关于reference condition的变种：minimally disturbed，historical，least disturbed和best attainable条件。这里将reference规定为least-disturbed condition。

使用三种方法来识别reference质量的径流测站。

##### 1.hydrologic disturbance index（以下简称HDI）

该方法是基于GIS提取的变量对人类活动的干扰进行量化。整理文献[Quantifying human disturbance in watersheds: variable selection and performance of a GIS-based disturbance index for predicting the biological condition of perennial streams](https://www.sciencedirect.com/science/article/abs/pii/S1470160X09000983)所描述的方法，如下所示。

首先，目的是量化流域内人类活动影响的程度。那么如何量化呢？首先要对人类活动的影响进行变量描述，然后再依据这些变量进行计算。

因此问题就归结为选择什么变量描述，以及如何整合这些变量进行计算。

首先，根据GIS数据选择了33个方便获取的变量。然后以USEPA分类的受影响严重(DIS)、中等（MED）、不严重（REF）的流域为率定和验证的标准。来分析哪些变量及组合和计算方法能最有效地区分受影响程度严重与不严重。

那么如何确定变量及组合的方式？

因为直接试验所有33个变量的所有组合方式计算量太大，因此要选择一些进行计算，论文选择了四个组合方式。

第一种是直接选择33个变量；

第二种叫做Reduced-Original数据集。首先计算33个变量两两之间的Spearman's rho，以此确定相关性较高的变量，选出rho>0.7的变量组合；
然后将每个变量作为可观测值排序，将disturbance、Reference当做类别变量，进行Kruskal-Wallis卡方检验，卡方越大，说明概率越小，越能拒绝disturbance和reference相同的零假设，所以卡方越大越好。
因此在相关性高的变量中选择卡方较大的值。再通过减掉卡方小的变量等操作，可以得到最后一组变量；

第三种是Reduced-Synthetic数据集。该组变量是通过PCA主成分分析算法获取的。首先基于专业知识将33个变量分成5个类别。对每一个类别利用PCA算法将其中所有变量降维到新变量上，即Principle Components(PCs)。这里选取了各个类别的第一个主成分，即每个选择了一个主维度，这样就得到了5个新变量；

第四种称作Redundant dataset。和第二种类似，不过包含了一些相关的变量做冗余，为了检验冗余的效果。即把和第二种相关的变量包含进来，得到22个变量。

有了四组变量组合后，可以确定计算方法，即如何对影响程度进行量化。

对变量代表的影响程度进行打分是常用的方法，具体而言就是基于流域人数的相对值来分配影响点数，该方法有几种变种：

第一种，range-standardize。首先变量被scale到0-10生成一组原始的disturbance值，然后利用权重，加权平均计算得到一个index。

第二种，the Percentile>0方法。对各项变量数据排序，从0开始，等距打分，然后加权平均。

第三种，the Percentile>50方法。和上述方法类似，只不过是从50开始。

至于具体的加权方法，也有三种：

第一种是权重一样；

第二种是卡方作为权重；

第三种是PC权重。

利用上述方式，最后得到的最能区分的变量组合和计算方法是：Reduced-Original数据集+Percentile>0打分+卡方权重。

最后用这一套方法计算得到的就是hydrologic disturbance index。

##### 2.用地图对每个流域进行观测

通过谷歌地图能对流域内的各项人类活动进行检验。不过这种方法不可能通过人工照顾到所有的人类活动。

##### 3.根据USGS的专家知识

有很多数据报告体现了人类活动的影响。

最后在干旱地区，还会通过灌溉量来识别被影响的径流站点。为此，通过比较径流实测值与通过水量平衡模型计估计的径流值之间的差别，估计了对径流的取水值。
如果观测与估计的径流值的比例远小于1，那么久认为取水是严重的，就不会把这个站当做reference的。

在前述数据的基础上，根据ecoregions的划分方法，将6785个流域分类到9大流域中。相似的landform/climate/land use的流域归为一类ecoregion。
然后在每个ecoregion内，分析站点的disturbed程度。最小程度的站点就是reference站点，其他所有的都是non-reference站点。
当然，随着时间变化，数据使用者可以根据自己的分析进行改进。

### CLASS III. DATA SET STATUS AND ACCESSIBILITY

这部分主要讲了数据的状态：更新时间、元数据等；

数据获取：网站、电话等。

### CLASS IV. DATA STRUCTURAL DESCRIPTORS

这部分对25个txt文件数据进行进一步的阐述。

#### 数据集文件

每个文件都有6785条记录，各自有唯一的ID。前面已经说过了，这里不再重复。

格式和存储媒介：介绍了存储格式、方式及一些字段的说明，不表。

#### 变量信息

GIS数据集没有，因此这里给出一些基本的投影信息：

Albers Equal-Area

Datum：NAD83

Spheroid：GRS1980

### CLASS V. SUPPLEMENTAL DESCRIPTORS

主要说一下结果。最后在各个ecoregion里总共识别出了1512个站点作为reference站点。差不多各个流域内占25%。

直观上看，reference的站点所属流域会更小，径流也更小，海拔更高。

最后的说明旨在告知数据使用者这里的reference选取方法是在HDI方法基础上，结合高精度遥感数据和ADR的资料进行人工校正的。
因此区域的专家是可以做出更好的分类的。

## GAGES-II Data Set

通过查阅报告<https://pubs.er.usgs.gov/publication/70046617>可知，基本的方法和GAGES应该是一致的。

### 基本信息

GAGES-II数据集提供了9322个站点的地理空间和类别数据。是GAGES的升级。GAGES-II数据都是有20年+的数据。

Reference站点基于12个主要ecoregions，选出的least-disturbed的站点。有2057个。

地理空间数据包括：从国家数据资源编辑的几百个流域特性，包括：环境特征（气候、地理、土壤、地形）和人类活动影响（土地利用，路网密度，大坝、渠道、电站等）。

数据集还包括基于年度数据报告ADR的来自USGS水科学中心的comments。

数据集还包括GIS格式的流域边界文件。

数据集包括的项目有：点shape文件，和9322个测站的总结性数据，包括流域特性，变量定义，更多细节的报告。
报告包括：流域边界shape文件，按分类的聚合ecoregion组织的。包括每个测站的mainstem stream lines。

数据集的目的：

（1）提供一个大量有测量流域全面的地理空间特性数据集；
（2）给出在12大类ecoregions中，哪些流域代表受人类影响较少的水文条件——reference gages。

### 数据质量

由USGSreview

### 空间数据

站点9322个

### 空间参考系

### 实体及属性

点属性表：gagesII_9322_sep30_2011。

属性：shape,STAID,STANAME,...

### Distribution信息

USGS贡献。

标准处理过程：

- 站点shape文件压缩，网上可下载；
- excel、word、csv文件时流域属性和update报告，可下载<https://water.usgs.gov/GIS/dsdl/basinchar_and_report_sept_2011.zip>；
- 流域边界shapefile
- Coverage格式的mainstem line coverages

### 详查数据

#### basinchar_and_report_sept_2011.zip

This zip file contains basin characteristics for stream gages that are part of "GAGES II" (an acronym for Geospatial Attributes of Gages for Evaluating Streamflow, version II).

GAGES II is an update to the original GAGES, which was published as a Data Paper on the journal Ecology's website (Falcone and others, 2010, <http://esapubs.org/Archive/ecol/E091/045/default.htm;> click "Metadata" when you get there for the report).
Although the overall methodology **did not change**, there are a number of additions and improvements, both major and minor.
The most significant improvements and changes are provided in the "What's New" section of the .docx file in this directory.

The zip file basinchar_and_report_sept_2011.zip contains the following files:

- the Word document gagesII_sept30_2011_report.docx.  This is the report describing the update.

- the spreadsheet gagesII_sept30_2011_conterm.xlsx contains the basin characteristics for the gages in the conterminous US.

- the spreadsheet gagesII_sept30_2011_AKHIPR.xlsx contains the basin characteristics for the gages in Alaska-Hawaii-Puerto Rico. This is in the same format as the maindata spreadsheet, but contains fewer worksheets and variables, because only a subset of variables were comparable and readily calculatable for those areas.

- the spreadsheet gagesII_sept30_2011_var_desc.xlsx contains the variable descriptions for all the variables in the data spreadsheets.

- the zip file spreadsheets-in-csv-format.zip.  This contains all the above data and variable descriptions in comma-separated text files, for any users who may not have access to MS Excel.

那么接下来就逐一查看这些文件。

##### gagesII_sept30_2011_report.docx

该文件主要讲述了GAGES-II数据的特点。

###### What's new

1. GAGES-II比GAGES站点多的原因在于GAGES-II纳入了很多从09年开始才active（2008年10月1日-2009年9月30日中有至少50天数据）的站点；
2. 站点包含了美国大陆主体之外的地区——阿拉斯加、夏威夷和波多黎各；
3. GAGES中只有流域属性和reference/non-reference的分类结果，而GAGES-II中又增加了流域边界和每个站点mainstem stream lines的文件。
4. 重新计算了之前6785个站点的129个的流域边界和属性；
5. 土地利用类型数据由之前更新到NLVD06；
6. 关于大坝数据，使用路陆军工程兵团09年的国家大坝列表NID新版本；
7. 增加了每个流域关于年平均降雨和气温的时间序列数据共60年；
8. 有了详细的作物类型信息；
9. 更准确的流域边界；
10. 站点径流数据由flow years matrix来说明哪些站点哪些年的径流数据是完整数据，还给出了站点径流估计占的比例；
11. 几百个mainstem stream lines得到修正；
12. 在计算Hydrologic Disturbance Index时，将ARTFLOW_PCT这一指标从index的计算中移除了；
13. 在HydroMod_Other表中给出了农业灌溉和电站的指标；
14. 35个测量河流和人工渠道并行汇聚一起的流量的测站被移除；
15. 增删改了一些变量：增加了流域中心经纬度，01-06年城市土地利用变化加入，去掉了LC_Change92_01，从Landscan数据中获取了白天和晚上的人口密度数据，增加了路网河流交叉数据，给出了流域主要植物，还有GAGE的ID和NAME改成了STAN的ID和NAME。

###### 上述new的一些准则

选择的径流站点都是有从1950年以来至少20年数据的或者现在是active的站点（一年指的是水文年从10.1-9.30）。

此外：

- 流域必须小于5万平方公里；
- 至少95%的流域面积是在美国境内的（因为US境外的GIS数据和境内的不一致）；
- 人工河流水渠上的gages被排除；
- 至少要有NHDPlus 100k stream segment的一部分是和流域有交集的；
- 必须得在一定的置信度内确定流域轮廓。

###### 流域边界轮廓

流域边界是用不同工具基于不同数据集实现的。总的来说，大部分来自NHDPlus data的Wieczorek delineations。

然后人工对9322个流域检查了至少一遍，评价数据再BOUND_QA表中。

###### 数据的组织结构

The majority of the variables given in the data worksheets for this project are based on **watershed**, **riparian-level** (all NHDPlus 100k streams in watershed), or **mainstem-level** (main channel stream in watershed) **GIS calculations**.

A number of data fields are not the result of GIS calculations, but rather the result of assembling data from other sources - for example **the ADR remarks and citations** - or as a result of our interpretation - for example **the basin classification** (reference vs. non- reference).

主要数据集被分作27个表，代表了不同类型的变量。这里结合GAGES初始版本的数据集一起给出一张表。

| 变量类型                    | GAGES | GAGES-II | 解释                                                                                 |
| --------------------------- | ----- | -------- | ------------------------------------------------------------------------------------ |
| BasinID                     | √     | √        | 站点标识                                                                             |
| Bas_Classif                 | √     | √        | 是否reference                                                                        |
| Bas_Morph                   | √     | √        | 流域几何形态                                                                         |
| Bound_QA                    | ×     | √        | **流域边界质保**                                                                     |
| Census_Block                | √     | ×        | *街道人口普查*                                                                       |
| Census_County               | √     | ×        | *镇人口普查*                                                                         |
| Climate                     | √     | √        | 气候特征                                                                             |
| Climate_Ppt_Annual          | ×     | √        | **流域年均降雨**                                                                     |
| Climate_Tmp_Annual          | ×     | √        | **流域年均气温**                                                                     |
| FlowRec                     | ×     | √        | **径流记录矩阵**                                                                     |
| Geology                     | √     | √        | 地质特征                                                                             |
| Hydro                       | √     | √        | 基于GIS的水文特征                                                                    |
| HydroMod_Dams               | √     | √        | 大坝信息                                                                             |
| HydroMod_Other              | √     | √        | 其他人为水文影响                                                                     |
| Infrastructure              | √     | ×        | *路网与不透水面积*                                                                   |
| LandScape_Pat               | √     | √        | Landscape pattern metric                                                             |
| LC01_Basin/LC06_Basin       | √     | √        | 各土地利用类型比例                                                                   |
| LC01_Mains100/LC06_Mains100 | √     | √        | 河流中心线100m缓冲区土地利用                                                         |
| LC01_Mains800/LC06_Mains800 | √     | √        | 河流中心线800m缓冲区土地利用                                                         |
| LC01_Rip100/LC06_Rip100     | √     | √        | 河流边缘100m缓冲区土地利用                                                           |
| LC01_Rip800/LC06_Rip800     | √     | √        | 河流边缘800m缓冲区土地利用                                                           |
| LC_Change92_01              | √     | ×        | *92-01年土地利用变化*                                                                |
| LC_Crops                    | ×     | √        | **NASA CDL的土地利用**                                                               |
| Nutrient_App                | √     | √        | 氮磷等估计                                                                           |
| Pest_App                    | √     | √        | 农药估计                                                                             |
| Pop_Infrastr                | ×     | √        | **人口、路网、不透水面积**                                                           |
| Prot_Areas                  | √     | √        | 保护区比例                                                                           |
| Reach                       | √     | ×        | *河道编码*                                                                           |
| Regions                     | √     | √        | 站点位置及流域占所处region比例                                                       |
| Soils                       | √     | √        | 土壤特征                                                                             |
| Topo                        | √     | √        | 地形特征                                                                             |
| X_Region_Names              | ×     | √        | **A crosswalk of codes from the "Regions" worksheet to their names or descriptions** |
注：斜体表示仅属于GAGES，加粗表示仅属于GAGES-II

上表中每一类变量的变量描述的基本信息见gagesII_sept30_2011_var_desc.xlsx，这里暂不表述。

###### 站点分类

站点分类为reference还是non-reference的方式依然遵循Falcone等人的文献（前文有）。方法和GAGES用的方法一致，但是最后结果有所不同，这里主要表述不同之处。

在HDI方法中，基于七个变量进行index的计算：

- presence of major dams in the watershed (MAJ_DDENS_2009)
- change in reservoir storage from 1950-2009 (STOR_2009 - PRE1950_STOR)
- percentage of streamlines coded canals/ditches/pipelines in the watershed (CANALS_PCT)
- road density in the watershed (ROADS_KM_SQ_KM)
- distance of stream gage to nearest major pollutant discharge site (RAW_DIS_NEAREST_MAJ_NPDES)
- county- level fresh-water withdrawal estimate (WATER_WITHDR)
- fragmentation of undeveloped land in the watershed (FRAGUN_BASIN)

也是HDI和另外两种查资料和看地图方式结合。

站点最后是被分为了12个ecoregions。主体大陆上还是9个ecoregions，如下图。然后再每个ecoregions上来分类reference。

![ecoregions](ecoregions.png)

最后也说明了，GAGES-II的分类方式不一定是最准确的。基于其他目的或者针对某些重点人类活动（比如只针对城市化），可能可以得到不同的reference sites。（比如我自己去做径流预报时候，人类活动影响不影响的reference可能会有不一样）

##### gagesII_sept30_2011_var_desc.xlsx

该文件主要包括对各数据表中各个变量的描述。

- 第一列数据是27个大类；
- 第二列是各个大类下的变量名称；
- 第三列是对变量的描述；
- 第四列表述变量的描述尺度是watershed还是site等；
- 第五列表示变量的存储数据类型，比如浮点、整型等；
- 第六列指的是数值型数据的单位；
- 第七列是时间范围；
- 第八列是获取数据的处理方式；
- 第九列是关于处理方式的额外补充说明；
- 第十列是数据源；
- 第十一列是分辨率；
- 第十二列是引用源；
- 第十三列是数据源网站。

接下来，简单看一看这27大类里面都有什么样的变量，容易了解的或之前已经提及的变量就简单带过。

- BasinID：STAID/STANAME/DRAIN_SQKM/HUC02/LAT_GAGE/LNG_GAGE/STATE/BOUND_SOURCE/HCDN-2009/HBN36/OLD_HCDN/NSIP_SENTINEL/FIPS_SITE/COUNTYNAME_SITE/NAWQA_SUID
HUC02:HUC是NHDPlus Water Resources Region大区域，由两位数字表示。比如01是New England等；
BOUND_SOURCE是指流域边界的来源，比如1代表 Wieczorek delineations；
接下来几个都是判断测站是否属某个观测network.
- Bas_Classif: CLASS/AGGECOREGION/HYDRO_DISTURB_INDX/WR_REPORT_REMARKS/ADR_CITATION/SCREENING_COMMENTS/WSC_CLASS (AK-HI-PR only)
  AGGECOREGION是level II的ecoregion。
- Bas_Morph：BAS_COMPACTNESS/LAT_CENT/LONG_CENT
- Bound_QA:BASIN_BOUNDARY_CONFIDENCE/DRAIN_SQKM/NWIS_DRAIN_SQKM/PCT_DIFF_NWIS/HUC10_CHECK
  PCT_DIFF_NWIS:这里的流域面积和NWIS数据的差别百分比。
  HUC10_CHECK：和WBD HUC10边界的对比检查。
- Climate：较多变量，不一一给出。包括降雨、气温、湿度多个角度的数据。
- Climate_Ppt_Annual：PPT1950_AVG thru PPT2009_avg (60 values)
- Climate_Tmp_Annual:TMP1950_AVG thru TMP2009_avg (60 values)
- Flow_Record:FLOW_PCT_EST_VALUES/ACTIVE09/FLOWYRS_1900_2009/FLOWYRS_1950_2009/FLOWYRS_1990_2009/wy1900 through wy2009 (110 values)
  FLOW_PCT_EST_VALUES：径流估计值占的比例；
- Geology：GEOL_REEDBUSH_DOM/GEOL_REEDBUSH_DOM_PCT/GEOL_REEDBUSH_SITE/GEOL_HUNT_DOM_CODE/GEOL_HUNT_DOM_PCT/GEOL_HUNT_DOM_DESC/GEOL_HUNT_SITE_CODE
  GEOL_REEDBUSH_DOM：根据Reed的文献得到的主要地质类型；
  GEOL_HUNT_DOM_CODE：根据Hunt的文献得到的主要地质类型编码。
- Hydro：径流密度等各类水文属性，很多，这里列出几个感兴趣的属性。
  MAINSTEM_SINUOUSITY：mainstem stream的河流曲直比；
  **HIRES_LENTIC_PCT**：被水库+湖泊/ponds占的流域面积比；
  BFI_AVE：基流系数；
  PERDUN：邓恩产流，即蓄满产流，临时饱和带产流占总径流的比例；
  PERHOR：霍顿产流，即超渗产流占总径流的比例；
  TOPWET：Topographic wetness index地形湿度指数；
  CONTACT:地下径流contact时间指数估计了下渗水在流入河流之前停留在流域饱和带的天数。
- **HydroMod_Dams**：NDAMS_2009/DDENS_2009/STOR_NID_2009/STOR_NOR_2009/MAJ_NDAMS_2009/MAJ_DDENS_2009/pre19xx_NDAMS/pre19xx_DDENS/pre19xx_STOR/RAW_DIS_NEAREST_DAM/RAW_AVG_DIS_ALLDAMS/RAW_DIS_NEAREST_MAJ_DAM/RAW_AVG_DIS_ALL_MAJ_DAMS
STOR_NID_2009：总库容；
RAW_DIS_NEAREST_DAM：离站site最近的大坝到site的直线距离。
- **HydroMod_Other**：CANALS_PCT/RAW_DIS_NEAREST_CANAL/RAW_AVG_DIS_ALLCANALS/CANALS_MAINSTEM_PCT/NPDES_MAJ_DENS/RAW_DIS_NEAREST_MAJ_NPDES/RAW_AVG_DIS_ALL_MAJ_NPDES/FRESHW_WITHDRAWAL/MINING92_PCT/PCT_IRRIG_AG/POWER_NUM_PTS/POWER_SUM_MW
  NPDES_MAJ_DENS：NPDES是National Pollutant Discharge Elimination System，因此此变量是说NPDES主要（由EPA定义）点的密度；
  FRESHW_WITHDRAWAL：每平方公里freshwater的抽取量；
  MINING92_PCT：采石场-露天矿坑-砾石坑流域土地覆盖百分比；
  PCT_IRRIG_AG：灌溉农业流域的百分比，来自USGS 2002年250-m MODIS数据；
- **Landscape_Pat**：FRAGUN_BASIN/HIRES_LENTIC_NUM/HIRES_LENTIC_DENS/HIRES_LENTIC_MEANSIZ。
  FRAGUN_BASIN：流域“未开发”土地破碎化指数，越大代表被人类活动影响越大；
  HIRES_LENTIC_NUM：从高分辨率数据获取的Lakes/Ponds和水库水体的个数。
- **LC06_Basin/LC06_Mains100/LC06_Mains800/LC06_Rip100/LC06_Rip800**：各类型土地利用的比例，不一一阐述了，主要有城市、森林、农业等；
- **LC_Crops**:各类作物的面积占流域的比例，比如谷物、棉花、大米等
- Nutrient_App：NITR_APP_KG_SQKM/PHOS_APP_KG_SQKM
- Pest_App：PESTAPP_KG_SQKM
- **Pop_Infrastr**：PDEN_2000_BLOCK/PDEN_DAY_LANDSCAN_2007/PDEN_NIGHT_LANDSCAN_2007/ROADS_KM_SQ_KM/RD_STR_INTERS/IMPNLCD06/NLCD01_06_DEV
  PDEN_DAY_LANDSCAN_2007：白天通过LandScan看到的人口密度；
  RD_STR_INTERS：河流和道路交汇的数目；
  IMPNLCD06：不透水面积占流域比例。
- Prot_Areas：PADCAT1_PCT_BASIN/PADCAT2_PCT_BASIN/PADCAT3_PCT_BASIN，三个不同保护级别区域占流域的比例。
- Regions：ECO3_SITE/HLR100M_SITE/HUC8_SITE/USDA_LRR_SITE/NUTR_ECO_SITE/ECO2_BAS_DOM/ECO3_BAS_DOM/ECO3_BAS_PCT/NUTR_BAS_DOM/NUTR_BAS_PCT/HLR_BAS_DOM_100M/HLR_BAS_PCT_100M/PNV_BAS_DOM/PNV_BAS_PCT。都是表述的站点所处的region是什么。
  ECO3_SITE：site所处的Level III的ecoregion；
  HLR100M_SITE：site所处的Hydrologic Landscape Region；
  USDA_LRR_SITE：USDA（Department of Agriculture） Land Resource Region (LRR) code
  NUTR_ECO_SITE：Nutrient ecoregion at the gage location；
  PNV_BAS_DOM：Dominant (highest % of area) Potential Natural Vegetation (PNV) within the watershed.
- Soils：土壤特征描述的是在水文group里土壤的比例，以及各个类型土壤的各项指标数据
- Topo：主要是高度和坡度数据
- X_Region_Names：提供此表只是为了方便，以便将“Regions”表中的编号与它们的名称/描述交叉。上述代码和名称的参考文献和引用已在各regions给出。

##### gagesII_sept30_2011_conterm.xlsx

gagesII_sept30_2011_conterm.xlsx和gagesII_sept30_2011_AKHIPR.xlsx分别代表的是CONUS上的和CONUS之外的数据。这里只关注gagesII_sept30_2011_conterm，gagesII_sept30_2011_AKHIPR暂时略去。csv格式的文件和前面这些文件都一样，因此也略去不表了。

该表就是CONUS上各个site的具体27个变量类型的各项数据了。

问题：STAID是站点，那么站点对应的河流是怎么定义的，河段是如何选择的？同理所属流域、各类region是如何定义的？

#### boundaries_shapefiles_by_aggeco.zip

每个ecoregion的non-reference sites各一个完整shape文件，所有reference sites一个单独的完整shape文件。

#### gagesII_9322_point_shapefile.zip

全部9322个site的shape文件

#### mainstem_line_covers.zip

coverage类型文件和shapefile一样也是一种GIS数据类型，但是和shapefile有很大不同，shapefile不能描述数据的拓扑结构，而coverage则是拓扑的。关于coverage数据类型的具体情况可参考[ArcGIS官方文档](http://desktop.arcgis.com/zh-cn/arcmap/10.3/manage-data/coverages/what-is-a-coverage.htm)给出的解释。

这里的数据类型都是coverage的。描述non-reference和reference的站点和流域河流的拓扑关系等。
