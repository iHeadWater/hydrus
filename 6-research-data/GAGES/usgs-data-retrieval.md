# USGS-R:dataRetrieval程序

## 前提

USGS的数据获取程序是用R程序写的，所以必须折腾一下R语言了。
关于R语言以及相应IDE的具体的安装使用方式参考环境配置环节的说明文件。

## dataRetrieval介绍

以下关于USGS和EPA水文水质数据的retrieval函数的信息参考<https://owi.usgs.gov/R/dataRetrieval.html>

### Introduction

What is dataRetrieval?

- dataRetrieval是一个R包，用来get USGS（United States Geological Survey 美国地质调查局）/EPA（Environmental Protection Agency 美国国家环境保护局） water data into R

Where does the data come from?

- US Geological Survey water data
  - National Water Information System (NWIS)
- Water Quality Portal
  - USGS
  - EPA (EPA Storage and Retrieval Data Warehouse = STORET)
  - USDA
  - more being added….

What does dataRetrieval do to the data?

How to discover data?

- Examples will be provided

### Overview

dataRetrieval：发现、访问、获取和格式化water data。

![dataRetrieval](dataRetrieval.png)

数据源：来自National Water Information System（后面简称NWIS，主要是USGS的数据）和Water Quality Portal（后面简称WQP，包括来自USGS、EPA、USDA（ U.S. Department of Agriculture 美国农业部）和Federal，State，Tribal，Local等机构数据）。

数据类型：USGS的NWIS中包括Streamflow, Peak Flow, Rating Curves（水位-流量曲线）, Groundwater, Water Quality等各类数据；WQP包括Water Quality数据；

元数据：站点信息和参数信息。

时间序列数据类型：实时型数据，日累计数据，离散数据。

数据格式：RDB, WaterML1, WaterML2, WQX.

输出：Data Frame, Site Attributes, Parameter Attributes, Appropriate Column Types, Properly formatted dates and times, Time zone/ Daylight Savings（夏令时） baked in

### Installation

可直接通过CRAN库安装稳定版本。可在脚本中输入下面语句；在vs2017中可以简便地通过选择“R 工具” > “窗口” > “程序包”，搜索安装。

``` R
install.packages("dataRetrieval")
```

### dataRetrieval Help

使用该包时首先需要导入。

``` R
library(dataRetrieval)
```

每个函数都有help文件，使用如下所示代码即可查看：

``` R
?readNWISuv
```

在VS2017中，在右下角即可查看。

### USGS NWIS Overview

Unit Data:

- 按收集时的频率存储的数据 —— 比如15min
- 一般可追溯到2007年(相比之前120天的时间范围大大改善!)
- 包括当前实时数据

Daily Data:

- 日累计数据，比如均值、最小、最大
- 包括径流、地下水位、和水质传感器数据
- 这些数据可以追溯几十年

Discrete Data：

- 水质数据
- 地下水位
- 水位-流量曲线
- Surfacewater measurements
- Peak flow

Meta Data

- Site information
- Parameter information

### USGS Basic Web Retrievals

USGS用多种codes表示basic retrievals：

- Site ID(通常8或15位)
- Parameter Code（5位）
  - Full list：<https://help.waterdata.usgs.gov/code/parameter_cd_query?fmt=rdb&inline=true&group_cd=%>
- Statistic Code(对日数据值)
  - Full list:<https://help.waterdata.usgs.gov/code/stat_cd_nm_query?stat_nm_cd=%25&fmt=html>

#### Parameter Code

dataRetrieval包括一个叫parameterCdFile的数据集，利用该数据集可查看USGS的parameter codes。示例代码：

``` R
parameterCdFile <- parameterCdFile
names(parameterCdFile)
```

比如查带有“phosphorus”的parameter codes：

```R
phosCds <- parameterCdFile[grep("phosphorus",
                                parameterCdFile$parameter_nm,
                                ignore.case=TRUE),]

nrow(phosCds)
```

#### readNWISuv函数

知道一个站点编号，参数标号，和起始终止时间，就可以读取数据。
比如discharge (parameter code = 00060) data for the Yahara River at Windsor, WI (an inlet to Lake Mendota).

```R
siteNo <- "05427718"
pCode <- "00060"
start.date <- "2014-10-01"
end.date <- "2015-09-30"

yahara <- readNWISuv(siteNumbers = siteNo,
                     parameterCd = pCode,
                     startDate = start.date,
                     endDate = end.date)
```

#### renameNWISColumns函数

查看上例中的数据yahara的列：

```R
names(yahara)
```

```R
## [1] "agency_cd"        "site_no"          "dateTime"
## [4] "X_00060_00011"    "X_00060_00011_cd" "tz_cd"
```

列的名称都是基于参数和统计编号的. In many cases, you can clean up the names with a convenience function renameNWISColumns:

```R
yahara <- renameNWISColumns(yahara)
names(yahara)
```

``` R
## [1] "agency_cd"    "site_no"      "dateTime"     "Flow_Inst"
## [5] "Flow_Inst_cd" "tz_cd"
```

#### Explore Data

查看前几行数据

```R
head(yahara)
```

查看数据每列的总结信息

```R
summary(yahara)
```

数据的属性查看，还可以查看相关网页：

``` R
names(attributes(yahara))
url <- attr(yahara, "url")
```

绘制数据：

``` R
library(ggplot2)
ts <- ggplot(data = yahara,
             aes(dateTime, X_00060_00000)) +
      geom_line()
ts
```

绘制中Use attributes for metadata:

```R
parameterInfo <- attr(yahara, "variableInfo")
siteInfo <- attr(yahara, "siteInfo")
  
ts <- ts +
      xlab("") +
      ylab(parameterInfo$parameter_desc) +
      ggtitle(siteInfo$station_nm)
ts
```

#### 更多获取数据函数

类似readNWISuv的函数有一下一些：

| 函数名         | 数据项            |
| -------------- | ----------------- |
| readNWISuv     | Unit              |
| readNWISdv     | Daily             |
| readNWISgwl    | Groundwater Level |
| readNWISmeas   | Surface-water     |
| readNWISpeak   | Peak Flow         |
| readNWISqw     | Water Quality     |
| readNWISrating | Rating Curves     |
| readNWISpCode  | Parameter Code    |
| readNWISsite   | Site              |

### USGS Advanced Retrievals

#### readNWISdata函数

还有一个readNWISdata函数单独存在。
允许用户指定要调用的函数。(这个使用比较方便)

Available services:

- Unit (service = "iv")
- Daily (service = "dv")
- Groundwater levels (service = "gwlevels")
- Surface-water measurements (service = "measurement")
- Water Quality (service = "qw")
- Site (service = "site")

```R
siteNo <- "05427718"
pCode <- "00060"
start.date <- "2014-10-01"
end.date <- "2015-09-30"

yahara2 <- readNWISdata(siteNumbers = siteNo, parameterCd = pCode,
                     startDate = start.date, endDate = end.date,
                     service = "uv")
```

#### Discover Data

知道site number找数字容易，但是如果不知道可以去网页上查找：

- NWIS Mapper: <http://maps.waterdata.usgs.gov/mapper/index.html>
- 环境数据discovery和transformation工具：<http://cida.usgs.gov/enddat/dataDiscovery.jsp>
- dataRetrieval：Become familiar with the possibilities of the web services <http://waterservices.usgs.gov/>
在dataRetrieval这个网站的左上栏里有各类数据的概览，点击可查看详细信息。

#### 高阶版使用readNWISdata函数

比如：look for long-term USGS phosphorous data in Wisconsin:

```R
?readNWISdata
pCode <- c("00662","00665")
phWI <- readNWISdata(stateCd="WI", parameterCd=pCode,
                     service="site", seriesCatalogOutput=TRUE)
library(dplyr)
phWI.1 <- filter(phWI, parm_cd %in% pCode) %>%
            filter(count_nu > 300) %>%
            mutate(period = as.Date(end_date) - as.Date(begin_date)) %>%
            filter(period > 15*365)
```

可以在地图上查看数据：

```R
library(leaflet)
leaflet(data=phWI.1) %>%
  addProviderTiles("CartoDB.Positron") %>%
  addCircleMarkers(~dec_long_va,~dec_lat_va,
                   color = "red", radius=3, stroke=FALSE,
                   fillOpacity = 0.8, opacity = 0.8,
                   popup=~station_nm)
```

如果报错，就安装相应的包，比如我尝试的时候缺少leaflet和yaml包，安装即可。

其他一些例子

```R
dataTemp <- readNWISdata(stateCd="OH", parameterCd="00010", service="dv")

instFlow <- readNWISdata(sites="05114000", service="iv",
                   parameterCd="00060",
                   startDate="2014-05-01T00:00Z",endDate="2014-05-01T12:00Z")

instFlowCDT <- readNWISdata(sites="05114000", service="iv",
                   parameterCd="00060",
                   startDate="2014-05-01T00:00",endDate="2014-05-01T12:00",
                   tz="America/Chicago")

bBoxEx <- readNWISdata(bBox=c(-83,36.5,-81,38.5), parameterCd="00010")

waterYear <- readNWISdata(bBox=c(-83,36.5,-81,38.5), parameterCd="00010",
                  service="dv", startDate="2013-10-01", endDate="2014-09-30")

wiGWL <- readNWISdata(stateCd="WI",service="gwlevels")
meas <- readNWISdata(state_cd="WI",service="measurements",format="rdb_expanded")
```

### Water Quality Portal

- Multiple agencies
  - USGS data comes from the NWIS database
  - EPA data comes from the STORET database (this includes many state, tribal, NGO, and academic groups)
- WQP brings data from all these oranizations together and provides it in a single format
- Much more verbose output than NWIS
- To get non-NWIS data, need to use CharacteristicName instead of parameter code.

Much like the convenience functions for NWIS, there's a simple function for retrievals if the site number and parameter code or characteristic name is known.

```R
sitePH <- phWI.1$site_no[1]

nwisQW <- readNWISqw(sitePH, "00665")
ncol(nwisQW)
## [1] 36
wqpQW <- readWQPqw(paste0("USGS-",sitePH),"00665")
ncol(wqpQW)
## [1] 65
Explore these results in RStudio.
```

#### Censored Data:NWIS

Censored data is particularly important for water quality data. Two examples of censored data are:

- Left-censored - the data is less than the detection level of the measurement technique
- Right-censored - the data is greater than the upper-limit of the measurement technique

NWIS data makes identifing this data easy using the column result_cd.

#### Censored Data:WQP

There's a little more work for WQP data. The following table has renamed the columns for space considerations.

Non-NWIS data might have different ways to indicate censoring.

#### Water Quality Portal Retrieval: readWQPdata

The true value of the Water Quality Portal is to explore water quality data from different sources.

Become familiar with the possibilities of the web services <http://www.waterqualitydata.us/>

There's not a function in WQP that returns period of record information like we did above via NWIS data…(that feature may be implemented in the future)

The following function returns sites that have collected phosphorus data in Wisconsin. There's no way to know if that site has collected one sample, or thousands.

```R
phosSites <- whatWQPsites(statecode="WI",characteristicName="Phosphorus")
```

（其余水质数据相关内容暂时略过）

### Time/Time zone discussion

The arguments for all dataRetrieval functions concerning dates (startDate, endDate) can be R Date objects, or character strings, as long as the string is in the form "YYYY-MM-DD"

In R, one vector (or column in a data frame) can only have ONE timezone attribute
Sometimes in a single state, some sites will acknowledge daylight savings and some don't
dataRetrieval queries could easily span timezones
Therefore, dataRetrieval converts all date/times to UTC.

The user can specify a single timezone to override UTC. The allowable tz arguments are listed on the next slide

#### Allowable timezones

| tz                  | Name                               | UTC_offset | UTC_DST |
| ------------------- | ---------------------------------- | ---------- | ------- |
| America/New_York    | Eastern Time                       | -05:00     | -04:00  |
| America/Chicago     | Central Time                       | -06:00     | -05:00  |
| America/Denver      | Mountain Time                      | -07:00     | -06:00  |
| America/Los_Angeles | Pacific Time                       | -08:00     | -07:00  |
| America/Anchorage   | Alaska Time                        | -09:00     | -08:00  |
| America/Honolulu    | Hawaii Time                        | -10:00     | -09:00  |
| America/Jamaica     | Eastern Standard Time(year-round)  | -05:00     | -05:00  |
| America/Managua     | Central Standard Time (year-round) | -06:00     | -06:00  |
| America/Phoenix     | Mountain Standard Time(year-round) | -07:00     | -07:00  |
| America/Metlakatla  | Pacific Standard Time(year-round   | -08:00     | -08:00  |

### Verbose and Progress

Use tools from the httr package to get data transfer information, and/or a progress bar on long-running retrievals.

### More information

- dataRetrieval
  - These slides:<http://usgs-r.github.io/dataRetrieval>
  - Report issues and ask questions:<https://github.com/USGS-R/dataRetrieval/issues>
- NWIS
  - Water Services:<http://waterservices.usgs.gov/>
  - Help:<http://help.waterdata.usgs.gov/>
- Water Quality Portal
  - <http://www.waterqualitydata.us/>
