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

The NLDAS-1 forcing datasets (hourly, monthly average, and monthly climatology) 可以在[Get the Data](https://ldas.gsfc.nasa.gov/data)获取。

NLDAS-1 forcing主要数据源是NCEP（National Centers for Environmental Prediction）的Eta model-based Data Assimilation System (EDAS)，一个连续循环的北美4DDA系统. 它利用3小时分析-预报周期，通过同化许多类型的观测，包括对地面压力和screen-level大气温度、湿度、U和V风分量的站内观测，得出大气状态。在40公里的网格上提供后五个变量的EDAS 3小时场，加上地面向下短波和长波辐射以及总对流降水，然后在空间上插值到NLDAS网格，在时间上插值到1小时。最后，为了考虑NLDAS和EDAS的地表高程差异，使用标准的直减率(6.5 K/km)对气温和地表压力进行地形高度调整，然后对比湿度(保持原来的相对湿度)和向下的长波辐射(新气温、比湿度)进行调整。

基于goes的太阳insolation为NLDAS-1提供了主要的insolation驱动(短波下至地表)。对于低于75度的天顶角，GOES insolation不能恢复，因此在昼/夜界线附近补充EDAS日晒。最后，基于goes的产品套件，NLDAS-1强制文件中包括了光合作用活性辐射(PAR)和表面亮度温度场。

GOES-based solar insolation (Pinker et al., 2003) provides the primary insolation forcing (shortwave down at the surface) for NLDAS-1. GOES insolation is not retrieved for zenith angles below 75 degrees and so is supplemented with EDAS insolation near the day/night terminator. Last from the GOES-based product suite, Photosynthetically Active Radiation (PAR) and surface brightness temperature fields are included in the NLDAS-1 forcing files.

NLDAS-1 precipitation forcing over CONUS is anchored to NCEP's 1/4th degree gauge-only daily precipitation analyses of Higgins et al. (2000). In NLDAS-1, this daily analysis is interpolated to 1/8th-degree, then temporally disaggregated to hourly values by applying hourly weights derived from hourly, 4-km, radar-based (WSR-88D) precipitation fields. The latter radar-based fields are used only to derive disaggregation weights and do not change the daily total precipitation. Last, convective precipitation is estimated by multiplying NLDAS-1 total precipitation by the ratio of EDAS convective to EDAS total precipitation. The Convective Available Potential Energy (CAPE) is the final variable in the forcing dataset, also interpolated from EDAS.

The dataset applies a user-defined parameter table to indicate the contents and parameter number.

The following table shows a list of parameters, their Product Definition Section (PDS) IDs, and the units:
PDS_IDs:Short_Name:Full_Name [Unit]
63:ACPCPsfc:Convective precipitation hourly total [kg/m^2]
61:APCPsfc:Precipitation hourly total [kg/m^2]
118:BRTMPsfc:Surface brightness temperature from GOES-UMD Pinker [K]
157:CAPEsfc:Convective Available Potential Energy [J/kg]
205:DLWRFsfc:LW radiation flux downwards (surface) [W/m^2]
204:DSWRFsfc:SW radiation flux downwards (surface) [W/m^2]
101:PARsfc:PAR Photosynthetically Active Radiation from GOES-UMD Pinker [W/m^2]
201:PEDASsfc:Precipitation hourly total from EDAS [kg/m^2]
202:PRDARsfc:Precipitation hourly total from StageII [kg/m^2]
1:PRESsfc:Surface pressure [Pa]
206:RGOESsfc:SW radiation flux downwards (surface) from GOES-UMD Pinker [W/m^2]
51:SPFH2m:2-m above ground Specific humidity [kg/kg]
11:TMP2m:2-m above ground Temperature [K]
33:UGRD10m:10-m above ground Zonal wind speed [m/s]
34:VGRD10m:10-m above ground Meridional wind speed [m/s]

#### NLDAS-1 model datasets

This page describes the model data for Phase 1 of the North American Land Data Assimilation System (NLDAS-1). The data are in 1/8th-degree grid spacing and range from 01 Oct 1996 to 31 Dec 2007. The temporal resolution is hourly. The file format is WMO GRIB-1.

The LSMs used in NLDAS-1 were: Mosaic, Noah, SAC, and VIC.  However, the NLDAS-1 model datasets are no longer available to the public.

NLDAS validation from NLDAS Phase 1 is available from NOAA/NCEP/EMC.

NLDAS Phase 1 model validation information can be found in Robock et al. (2003).

### NLDAS-2

#### NLDAS-2 forcing dataset

This dataset contains the forcing data for Phase 2 of the North American Land Data Assimilation System (NLDAS-2). The data are in 1/8th-degree grid spacing and range from 01 Jan 1979 to present. The temporal resolution is hourly. The file format is WMO GRIB-1.

The NLDAS-2 forcing datasets (hourly, monthly average, and monthly climatology) are available from the "Get the Data" link on the right or on the top menu.

The spatial domain, spatial resolution, computational grid, terrain height, and land mask of NLDAS-2 are identical to that in NLDAS-1, which is described in Section 2.1 of Mitchell et al. (2004).

Appendix A provides web addresses to NCEP online GRIB-1 documentation, source code, and parameter tables. In particular, readers of this document should read the discussion in Appendix A of GRIB-1 Parameter Tables.

The NLDAS-2 land-surface forcing files and land model output files use Parameter Table 130, which is oriented toward land/hydrology modeling.

The non-precipitation land-surface forcing fields for NLDAS-2 are derived from the analysis fields of the NCEP North American Regional Reanalysis (NARR).  NARR consists of: 1) a retrospective dataset starting from Jan 1979, and 2) a daily update execution at NCEP. The daily update provides a real-time NARR continuation known as the Regional Climate Data Assimilation System, or R-CDAS.

NARR analysis fields are 32-km spatial resolution and 3-hourly temporal frequency. Those NARR fields that are utilized to generate NLDAS-2 forcing fields are spatially interpolated to the finer resolution of the NLDAS 1/8th-degree grid and then temporally disaggregated to the NLDAS-2 hourly frequency. Additionally, the fields of surface pressure, surface downward longwave radiation, near-surface air temperature and near-surface specific humidity are adjusted vertically to account for the vertical difference between the NARR and NLDAS fields of terrain height. This vertical adjustment applies the traditional vertical lapse rate of 6.5 K/km for air temperature. The details of the spatial interpolation, temporal disaggregation, and vertical adjustment are those employed in NLDAS-1, as presented by Cosgrove et al. (2003).

The hourly land-surface forcing fields for NLDAS-2 are grouped into two GRIB files, "File A" and "File B". This is a change from NLDAS-1, which had only one hourly forcing file.

FORCING FILE A:

File A is the primary (default) forcing file. It will contain the following eleven fields (units are given in parentheses):

U wind component (m/s) at 10 meters above the surface
V wind component (m/s) at 10 meters above the surface
air temperature (K) ** at 2 meters above the surface
specific humidity (kg/kg) ** at 2 meters above the surface
surface pressure (Pa) **
surface downward longwave radiation (W/m^2) **
surface downward shortwave radiation (W/m^2) -- bias-corrected (see Appendix B)
precipitation hourly total (kg/m^2)
fraction of total precipitation that is convective (no units): from NARR
CAPE: Convective Available Potential Energy (J/kg): from NARR
potential evaporation (kg/m^2): from NARR
** indicates a field to which the aforementioned vertical adjustment is applied.

The first eight fields above are the traditional land-surface forcing fields, such as in PILPS (Project for Intercomparison of Land-Surface Process Schemes) and GSWP (Global Soil Wetness Project).

The surface downward shortwave radiation field in File A is a bias-corrected field wherein a bias-correction algorithm was applied to the NARR surface downward shortwave radiation. This bias correction utilizes five years (1996-2000) of the hourly 1/8th-degree GOES-based surface downward shortwave radiation fields derived by Pinker et al. (2003). The bias-correction algorithm is described in Appendix B.

The precipitation field in File A is not the NARR precipitation forcing, but is rather a product of a temporal disaggregation of a gauge-only CPC analysis of daily precipitation, performed directly on the NLDAS grid and including an orographic adjustment based on the widely-applied PRISM climatology. The methodology and source datasets for producing this precipitation forcing, including details of the temporal disaggregation from the daily analysis to hourly intervals, are given in Appendix C.

The field in File A that gives the fraction of total precipitation that is convective is an estimate derived from the following two NARR precipitation fields (which are provided in File B): NARR total precipitation and NARR convective precipitation (the latter is less than or equal to the NARR total precipitation and can be zero). The convective fraction of total precipitation and/or the CAPE field in File A are used by some land models to estimate the subgrid spatial variability of the total precipitation.

The potential evaporation field in File A is that computed in NARR using the modified Penman scheme of Mahrt and Ek (1984). Potential evaporation is needed by some land models (such as the SAC model) that require potential evaporation as an input forcing.

FORCING FILE B:

One fundamental physical process represented in land modeling is the surface aerodynamic conductance, which represents the intensity of the near-surface vertical turbulence that transports heat and moisture between the land-surface and the overlying atmosphere.

There are many approaches to modeling the surface aerodynamic conductance in boundary layer modeling in general, and in land-surface modeling. The results from NLDAS-1 showed a surprisingly large difference among four different land models in the simulated magnitude of the warm-season diurnal cycle of aerodynamic conductance.

The 2-meter temperature and specific humidity and 10-meter wind fields applied in continental-scale land-surface modeling studies are typically products of the data assimilation/analysis systems of mainstream NWP centers. The 2-meter and 10-meter levels in such analysis/assimilation systems are rarely explicit levels in the background assimilating NWP model of the given NWP center. Hence NWP centers diagnose these 2-meter and 10-meter fields from the lowest prognostic level of the assimilating model. This diagnostic derivation of 2-meter temperature and humidity fields and 10-meter wind fields is done on the basis of: A) those same fields at the model's lowest prognostic level, which is usually well above the 10-meter level (e.g., 20-200 meters above), and B) the given model's method for modeling the aerodynamic conductance of the "surface layer", also known as the "constant flux layer" -- i.e., applying the given model's particular approach to such physical entities as the surface roughness length for momentum, the surface roughness length for heat, surface layer stability functions (e.g., similarity profile functions) and surface layer parameters (e.g., mixing length).

NLDAS-2 is therefore providing a second forcing file, File B, in which the surface temperature, humidity, and wind fields are represented not at 2 meters and 10 meters above the height of the NLDAS terrain, but rather at the same height above the NLDAS terrain as the height above the NARR terrain of the lowest prognostic level of the NARR assimilation system (namely, the same height above the model terrain as the lowest prognostic level of the mesoscale Eta model, which is the assimilating model in NARR).  We shall denote the latter height as "H", and this height H varies spatially in the horizontal. The motivation for this approach is to allow land models in NLDAS-2 to calculate their aerodynamic conductance from surface forcing fields that are significantly more independent (albeit not fully independent) of the aerodynamic conductance approach applied in the assimilation/analysis system from which the surface forcing fields were derived.

Specifically then, forcing File B of NLDAS-2 will contain the following ten fields:

U wind component (m/s) at H meters above the surface
V wind component (m/s) at H meters above the surface
air temperature (K) ** at H meters above the surface
specific humidity (kg/kg) ** at H meters above the surface
pressure (Pa) ** at H meters above the surface
height H above the surface (m)
NARR surface downward shortwave radiation (W/m^2) -- without bias-correction
NARR precipitation hourly total (kg/m^2)
NARR convective precipitation hourly total (kg/m^2)
NARR aerodynamic conductance (m/s)
Fields 7-10 above are provided for additional reasons, as follows. Fields 7 and 8 are provided to permit land modeling sensitivity tests in which the solar radiation and precipitation fields of File A are replaced by their less accurate counterparts taken directly from NARR. Fields 8 and 9 are the NARR fields used to derive the field of "fraction of convective precipitation" in File A. Field 10 is the aerodynamic conductance obtained from NARR, to allow comparison with the aerodynamic conductance computed independently by each land model in NLDAS-2.

Appendix A: The GRIB-1 Data Format (Documentation, Code, Parameter Tables)

The NCEP online User's Manual for the GRIB-1 data format is available here.

The NCEP web site providing Fortran-90 source code and documentation of code, as well as the NCEP GRIB-1 User's Guide, is here.

For a given physical variable, the GRIB data convention assigns the following:

a unique numeric ID known as the GRIB parameter ID (range 1-255)
a unique alphanumeric abbreviation (max of 8 characters)
required physical units.
The unique GRIB parameter IDs for given physical variables are provided in tables known as GRIB parameter tables. The GRIB-1 Parameter Tables formally recognized at NCEP are available online here.

At of Dec 2007, NCEP formally recognized five GRIB-1 Parameter Tables, namely: Table 2, Table 128, Table 129, Table 130, and Table 140. Each of these tables define up to a maximum of 255 physical variables and their corresponding unique Parameter IDs. Additionally, each table has a Part 1 and a Part 2. Part 1 is identical across all GRIB-1 Tables and provides a WMO mandated list of 128 physical parameters and their WMO-mandated unique Parameter IDs. Part 2 is defined locally by the originating center or agency and the list of physical parameters in Part 2 is often aligned with a given physical specialty. At NCEP for example, Part 2 of Table 128 is oriented somewhat toward ocean modeling and ocean physics, and Part 2 of Table 129 is oriented somewhat toward cloud microphysics.

The NLDAS-2 land-surface forcing files and land model output files will utilize GRIB-1 Parameter Table 130, which is oriented toward land/hydrology modeling and land/hydrology physics.

The parameter IDs for Part 2 of Table 130 are available online here.

The parameter IDs for Part 1 of Table 130 are identical to those of Table 2, online here.

The parameter IDs GRIB tables specific to the NLDAS-2 data as stored on the NASA Hydrology DISC can be found here.

Appendix B: Bias Correction of Downward Shortwave Radiation for NLDAS-2

The NARR downward shortwave radiation field in the NLDAS-2 forcing files ("A" files) is bias-corrected to University of Maryland Surface Radiation Budget (SRB) dataset produced under the auspices of the GEWEX Continental Scale International Project (GCIP) and GEWEX Americas Prediction Project (GAPP) (Pinker et al., 2003). Data from the GOES-8 satellite is processed using an inference model to produce hourly estimates of downward shortwave radiation fluxes. This dataset is produced on the native 1/8th-degree NLDAS grid and no interpolation is necessary. A ratio-based (Berg et al., 2003) bias correction to the reanalysis downward shortwave radiation field was completed.

Appendix C: Generation of hourly precipitation forcing for NLDAS-2

The total precipitation field contained in File A is derived from CPC daily CONUS gauge data (Higgins et al. 2000; Chen et al. 2008 - with the PRISM topographical adjustment, Daly et al. 1994), CPC hourly CONUS/Mexico gauge data (HPD, Higgins et al. 1996), hourly Doppler Stage II radar precipitation data, half-hourly CMORPH data, and 3-hourly NARR precipitation data. Reflecting the strengths of each dataset, hourly NLDAS-2 precipitation is derived by using the Doppler radar, CMORPH products, or HPD data to temporally disaggregate the daily gauge products. This process, described in detail below, capitalizes on the accuracy of the daily gauge product, and on the temporal and spatial resolutions of the Doppler radar and CMORPH products.

Over CONUS, CPC PRISM-adjusted 1/8th-degree daily gauge analyses serve as the backbone of the NLDAS-2 hourly precipitation forcing. In Mexico, where this dataset is unavailable, CPC's 1-degree (1/4th-degree after 2001) North American daily gauge product is used instead. In NLDAS-2, these gauge-only daily precipitation analyses are first processed to fill in any missing values, and then are temporally disaggregated into hourly fields. This is accomplished by deriving hourly disaggregation weights from NWS real-time, 4-km Stage II and 8-km CMORPH hourly precipitation analyses. Stage II data is available from 1996 to the present, while CMORPH data is available from 2002 to the present. The Stage II product consists of WSR-88D Doppler radar-based precipitation estimates that have been bias-corrected using hourly multi-agency gauge data (Fulton et al. 1998), and mosaicked into a national product over the contiguous United States (CONUS) by NCEP/EMC (Baldwin and Mitchell, 1997). This CONUS mosaic of the Stage II product is interpolated to 1/8th-degree and any gaps in radar coverage (which total on average 13% of the area of the CONUS and are due to lack of radar coverage or equipment maintenance) are filled in with nearest neighbor Stage II data from within a 2-degree radius. If no Stage II data are available, then CMORPH data are used instead. CMORPH data is also used over the Mexican portion of the NLDAS domain which is outside of the Stage II's region of coverage. When CMORPH data is unavailable, such as before 2002, the 2 X 2.5 degree CPC Hourly Precipitation Dataset (HPD) is used. If HPD is also unavailable, NARR data is used instead. Details of the precipitation gauges used in the CPC analyses can be found here, which also links to a map of the gauges that ever provided data for these analyses, with about half of these gauges still active in the real-time data production.

The above hourly fields are then divided by fields of their respective daily totals to create hourly temporal disaggregation weights representing the proportion of the 24-hour total precipitation which fell in each hour. If the daily total is zero in an area of non-zero CPC precipitation, hourly weights are set to 1/24 to spread the precipitation evenly over the entire day. These hourly weights are then multiplied by the daily gauge-only CPC precipitation analysis to arrive at temporally disaggregated hourly NLDAS-2 fields. Since the Stage II, CMORPH, HPD, and NARR data are only used to derive the hourly disaggregation weights, a daily summation of these hourly NLDAS-2 precipitation fields will exactly reproduce the original CPC daily precipitation analyses. Since daily gauge and hourly precipitation data is sparse over Canada, NARR precipitation is used over all Canadian regions within the NLDAS domain. Rather than have an abrupt cutoff at the United States border, a 1-degree wide blending area is used. In this region, precipitation forcing consists of a weighted combination of the precipitation datasets discussed above.

Starting on 01 January 2012, NLDAS-2 transitioned from the unified CPC precipitation product to an operational CPC precipitation product, as the previous product was no longer being generated. The primary difference between the products is that the interpolation algorithm has changed (as the input precipitation gauge information is the same). For the unified CPC product from 1979 to 2011, the Inverse Distance method was used, with missing values replaced using a precipitation climatology. For the operational CPC product from 2012 to present, the Optimal Interpolation method (OI) is used, with missing values replaced using the value from the nearest station. This difference in the interpolation method has shown some differences in the behavior of precipitation, especially right on the U.S.-side of the border with Mexico, in western mountainous regions, and along coastlines.

The different precipitation products (by year and location) used for generation of hourly NLDAS-2 precipitation is summarized in the table below. Unfortunately, due to data availability and the quasi-operational nature of NLDAS, complete continuity of the data over all times/locations is not possible. Additionally, the number and location of the precipitation gauge observations stations has varied over the NLDAS-2 record. For details, please see Figure 2 in Mo et al. 2012 and this presentation by Chen and Xie. For known issues with the NLDAS-2 precipitation, please see this FAQ and answer.

#### NLDAS-2 model datasets

This page describes the model data for Phase 2 of the North American Land Data Assimilation System (NLDAS-2). The data are in 1/8th-degree grid spacing and range from 02 Jan 1979 to present. The temporal resolution is hourly. The file format is WMO GRIB-1.

There are currently four land-surface models with data available over the NLDAS-2 period. They are:
