# netcdf使用

nc格式数据是水文模型应用中常见的一种格式，很多软件比如WRF、VIC等都会用到，至于为什么经常用，可以参考官方[用户手册](https://www.unidata.ucar.edu/software/netcdf/docs/index.html)。

## 安装netcdf

因为水文上很多模型使用范围较小，社区人员不多，因此软件持续开发的能力相对较弱，所以使用的依赖库的版本很多都不是最新的，netcdf也不例外，但是水文软件安装时候可以组织自己独立的用户，在独立文件夹下进行，因此单独安装一些库时，比如这里的netcdf，推荐依据官方[用户手册](https://www.unidata.ucar.edu/software/netcdf/docs/getting_and_building_netcdf.html)安装最新的稳定版本，以下是个人实践。

### Ubuntu下的安装

Ubuntu 16.04下进行安装。

首先需要进行netCDF-C的安装，因为其他库都依赖netCDF，比如Fortran、Python、Java、C++等库，C库的安装是必要条件。

#### 获取netCDF-C

可以通过apt-get获取pre-built的库，也可以直接获取最新版本的源码，这里选择从源码安装，因为下载[源码](https://github.com/Unidata/netcdf-c/releases)，这里选择下载tar.gz版本，zip版应该也没区别。

#### 构建netCDF-C

netCDF库需要第三方的库才能实现完整的功能。

依赖有：

- 对netCDF-4的支持需要：
  - HDF5 1.8.9 or later.
  - HDF5 1.10.1 or later.
- zlib 1.2.5 or later (for netCDF-4 compression)
- curl 7.18.0 or later (for DAP remote access client support)
- For parallel I/O support on classic netCDF files
  - PnetCDF 1.6.0 or later

注意：对4.4.1以前的版本，只能使用HDF5 1.8.X版本。

这里的构建采用支持netCDF-4和远程数据客户端以及并行计算的方式。并行需要的mpicc可以是openmpi也可以是mpich，这里选择了后者。总之需要：HDF5,zlib,curl,mpich。还可以选择szip，也可以不装，这里先用szip了。以上各依赖库需要的最低版本：HDF5 1.8.9, zlib 1.2.5, curl 7.18.0，mpich文档内没有说明。这里都选择安装最新版，依次展示如下，zlib 1.2.11，hdf5-1.10.5，curl-7.65.0。

[下载](https://www.zlib.net/)并构建zlib：

下载源码后，进入文件夹。可以按一般做法，把源码解压到usr/local/src中。然后进行构建。如果不选择/usr/local作为安装路径而是自己新建文件夹，后期如果在C语言代码中遇到include的情况时，还需要配置，否则会报错，因此这里依从官方文档的安装方式。如果后面有问题，需要卸载的话，直接在src文件夹下用sudo make uninstall卸载即可，如果手动卸载，由于安装的位置都在一起，容易卸不完全。

```code
sudo tar -zxvf zlib-1.2.11.tar.gz -C /usr/local/src
cd /usr/local/src/zlib-1.2.11
sudo ./configure --prefix=/usr/local
sudo make
sudo make check
sudo make install
```

下载并构建hdf5：

进入hdf5的[官网下载页面](https://www.hdfgroup.org/downloads/hdf5/)，可以看到source code和如何用configure构建的说明，下载源码之后结合构建说明（在release_docs文件夹下的install文件里有详细说明）以及netcdf官方文档的说明做即可。具体代码如下：

```code
sudo tar -zxvf hdf5-1.10.5.tar.gz -C /usr/local/src
cd /usr/local/src/hdf5-1.10.5
sudo ./configure --with-zlib=/usr/local --prefix=/usr/local
sudo make
sudo make check
sudo make install
```

根据HDF5安装文档，线程安全的能力配置中有--enable-hl等命令，详细地还需进一步参考说明，我看别的安装文档中也都没有这一项，加上个人不太清楚这个命令是干什么的，所以就不适用--enable-hl了，况且netcdf用户手册里面还敲错了。
sudo make可能需要花费几分钟的时间，需要等待。
sudo make check可能需要花费几分钟的时间，需要等待。没有报错就可以执行安装了。

[下载](https://curl.haxx.se/download.html)并构建curl：

```code
sudo tar -zxvf curl-7.65.0.tar.gz -C /usr/local/src
cd /usr/local/src/curl-7.65.0
sudo ./configure --prefix=/usr/local
sudo make
sudo make check
sudo make install
```

sudo make check可能需要花费几分钟时间。中间我遇到了一些错误，有一些权限问题，暂时未处理，因为不影响我的使用。

安装[mpich](http://www.mpich.org/downloads/)：

根据官方文档，最简单的安装方法是使用apt。因此这里就直接使用这种方式了。

```code
sudo apt-get install mpich
```

最后构建安装netcdf，执行以下代码

```code
sudo tar -zxvf netcdf-c-4.7.0.tar.gz -C /usr/local/src
cd /usr/local/src/netcdf-c-4.7.0
sudo CPPFLAGS='-I/usr/local/include' LDFLAGS='-L/usr/local/lib' ./configure --prefix=/usr/local
sudo make
sudo make check
sudo make install
```

sudo make check可能需要花费几分钟时间。

### windows下的安装

可以下载[exe文件](https://www.unidata.ucar.edu/software/netcdf/docs/winbin.html)直接安装。

### netCDF-python

使用pip安装netCDF4-python即可。

## 资料

补充一些资料如下：
[Python programming guide for Earth Scientists](http://python.hydrology-amsterdam.nl/manuals/hydro_python_manual.pdf)；
[netcdf4-python](https://github.com/Unidata/netcdf4-python)；
[Generating NetCDF files with Python](http://www.ceda.ac.uk/static/media/uploads/ncas-reading-2015/11_create_netcdf_python.pdf)；
[Python-NetCDF reading and writing example with plotting](http://schubert.atmos.colostate.edu/~cslocum/netcdf_example.html)。
