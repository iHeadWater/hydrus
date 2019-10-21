# A model-derived dataset of land surface states and fluxes

本文主要对文献[A Long-Term Hydrologically Based Dataset of Land Surface Fluxes and States for the Conterminous United States](https://journals.ametsoc.org/doi/full/10.1175/1520-0442%282002%29015%3C3237%3AALTHBD%3E2.0.CO%3B2)做一些翻译理解，以帮助理解CAMELS数据集。

## 数据集制作动机

和其他数据集很相似的是该数据集也是从climate modeling的角度出发的。land surface modeling在整个climate modeling里可以作为一个boundary condition，帮助陆气耦合模型吸收地表的物理量表达。在陆气耦合模型中，评估参数性能需要在建模的时空分辨率上比较观测值和模拟值，而缺少丰富的地表观测数据使得这称为了一个难点。有一些相关研究，但观测值通常都是点的，或者面积远小于模型的空间分辨率，缺乏长期的、全国范围的许多地表moisture fluxes和storages等的观测。

另外全球reanalyses，比如使用NCEP的全球预报模型，提供了一种能诊断大气和地表moisture和energy fluxes的模型预测。但是有较大误差，尽管后来有不少改进。一个主要原因是为了校准模型，soil moisture用的是nudging，这使得其他water budget的变量不准确，surface water budget不闭合nonclosure。因此，reanalyses的数据对于land surface moisture和energy的flux和状态变量模拟是不合适的。

## 数据集的制作基本思路

更好的地表water budget模拟的diagnosis能通过基于物理机制的，由高质量的可控的地表变量驱动的地表模型来获得。并且其汇流模拟结果可以和观测值进行匹配。在地表scheme中，有效的自由度可以通过在地表设置模型forcing变量来大大降低，而不是预先确定。为了结果的一致性，地表scheme应该通过构建，闭合地表水和能源budget。考虑到这些budget在设计上的封闭性，其他内部变量的可变性和相互作用可能reanalyses(或就此而言，任何耦合模型)产生的结果(包括模型状态的某种类型的更新)要现实得多。

## 数据集

一个50年的地表forcing观测和计算的地表fluxes和states变量。时间步长是3h，空间分辨率是1/8度，和LDAS的一致。

使用的陆地水文模型是VIC model。详细过程不再表述。

最后存储的各变量有：

| 变量类型                                | 变量名称  | 单位               | 3-h和天/derived monthly |
| --------------------------------------- | --------- | ------------------ | ----------------------- |
| Precipitation                           | Prate     | $kg m^{-2} s^{-1}$ | 3-h和天                 |
| Evapotranspiration                      | Evap      | $kg m^{-2} s^{-1}$ | 3-h和天                 |
| Runoff (surface)                        | Qs        | $kg m^{-2} s^{-1}$ | 3-h和天                 |
| Baseflow                                | Qsb       | $kg m^{-2} s^{-1}$ | 3-h和天                 |
| Soil moisture, layer 1                  | Soilm1    | $kg m^{-2}$        | 3-h和天                 |
| Soil moisture, layer 2                  | Soilm2    | $kg m^{-2}$        | 3-h和天                 |
| Soil moisture, layer 3                  | Soilm3    | $kg m^{-2}$        | 3-h和天                 |
| Snow water equivalent                   | SWE       | $kg m^{-2}$        | 3-h和天                 |
| Net shortwave radiation at the surface  | SWnet     | $W m^{-2}$         | 3-h和天                 |
| Incoming (downward) longwave radiation  | LWdown    | $W m^{-2}$         | 3-h和天                 |
| Net radiation at the surface            | NetRad    | $W m^{-2}$         | 3-h和天                 |
| Latent heat flux                        | Qle       | $W m^{-2}$         | 3-h和天                 |
| Sensible heat flux                      | Qh        | $W m^{-2}$         | 3-h和天                 |
| Ground heat flux                        | Qg        | $W m^{-2}$         | 3-h和天                 |
| Albedo                                  | Albedo    | -                  | 3-h和天                 |
| Surface (skin) temperature              | RadT      | K                  | 3-h和天                 |
| Relative humidity                       | RH        | %                  | 3-h和天                 |
| Air temperature                         | Tair2     | K                  | 3-h和天                 |
| Wind speed                              | Wind      | $m s^{-1}$         | 3-h和天                 |
| Average soil moisture tendency, layer 1 | DelSoilm1 | $kg m^{-2} s^{-1}$ | derived monthly         |
| Average soil moisture tendency, layer 2 | DelSoilm2 | $kg m^{-2} s^{-1}$ | derived monthly         |
| Average soil moisture tendency, layer 3 | DelSoilm3 | $kg m^{-2} s^{-1}$ | derived monthly         |
| Average snow water tendency             | DelSWE    | $kg m^{-2} s^{-1}$ | derived monthly         |