'''
NAME
    NetCDF with Python
PURPOSE
    To demonstrate how to read and write data with NetCDF files using
    a NetCDF file from the NCEP/NCAR Reanalysis.
    Plotting using Matplotlib and Basemap is also shown.
PROGRAMMER(S)
    Chris Slocum
    Owenyy修改
REVISION HISTORY
    20140320 -- Initial version created and posted online
    20140722 -- Added basic error handling to ncdump
                Thanks to K.-Michael Aye for highlighting the issue
    20190505 -- basemap2020年断更，新的绘图包使用cartopy
REFERENCES
    netcdf4-python -- http://code.google.com/p/netcdf4-python/
    NCEP/NCAR Reanalysis -- Kalnay et al. 1996
        http://dx.doi.org/10.1175/1520-0477(1996)077<0437:TNYRP>2.0.CO;2
'''
import datetime as dt  # Python standard library datetime  module
import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def ncdump(nc_fid, verb=True):
    '''
    ncdump outputs dimensions, variables and their attribute information.
    The information is similar to that of NCAR's ncdump utility.
    ncdump requires a valid instance of Dataset.

    Parameters
    ----------
    nc_fid : netCDF4.Dataset
        A netCDF4 dateset object
    verb : Boolean
        whether or not nc_attrs, nc_dims, and nc_vars are printed

    Returns
    -------
    nc_attrs : list
        A Python list of the NetCDF file global attributes
    nc_dims : list
        A Python list of the NetCDF file dimensions
    nc_vars : list
        A Python list of the NetCDF file variables
    '''

    def print_ncattr(key):
        """
        Prints the NetCDF file attributes for a given key

        Parameters
        ----------
        key : unicode
            a valid netCDF4.Dataset.variables key
        """
        try:
            print("\t\ttype:", repr(nc_fid.variables[key].dtype))
            for ncattr in nc_fid.variables[key].ncattrs():
                print('\t\t%s:' % ncattr, \
                      repr(nc_fid.variables[key].getncattr(ncattr)))
        except KeyError:
            print("\t\tWARNING: %s does not contain variable attributes" % key)

    # NetCDF global attributes
    nc_attrs = nc_fid.ncattrs()
    if verb:
        print("NetCDF Global Attributes:")
        for nc_attr in nc_attrs:
            print('\t%s:' % nc_attr, repr(nc_fid.getncattr(nc_attr)))
    nc_dims = [dim for dim in nc_fid.dimensions]  # list of nc dimensions
    # Dimension shape information.
    if verb:
        print("NetCDF dimension information:")
        for dim in nc_dims:
            print("\tName:", dim)
            print("\t\tsize:", len(nc_fid.dimensions[dim]))
            print_ncattr(dim)
    # Variable information.
    nc_vars = [var for var in nc_fid.variables]  # list of nc variables
    if verb:
        print("NetCDF variable information:")
        for var in nc_vars:
            if var not in nc_dims:
                print('\tName:', var)
                print("\t\tdimensions:", nc_fid.variables[var].dimensions)
                print("\t\tsize:", nc_fid.variables[var].size)
                print_ncattr(var)
    return nc_attrs, nc_dims, nc_vars


# 读取nc文件的步骤一般是先创建一个Datase对象
nc_fid = Dataset('./air.sig995.2012.nc')  # Dataset is the class behavior to open the file
print(nc_fid)
# and create an instance of the ncCDF4 class，显示数据的全局属性、维度和变量信息
nc_attrs, nc_dims, nc_vars = ncdump(nc_fid)
# Extract data from NetCDF file
lats = nc_fid.variables['lat'][:]  # extract/copy the data
lons = nc_fid.variables['lon'][:]
time = nc_fid.variables['time'][:]
air = nc_fid.variables['air'][:]  # shape is time, lat, lon as shown above

# Python and NCEP reanalysis Daily Averages的数据集 are slightly off in time， so this fixes that problem
offset = dt.timedelta(hours=48)
# List of all times in the file as datetime objects，这里time的时间表示是与1-1-1 00:00:0.0的小时差
dt_time = [dt.date(1, 1, 1) + dt.timedelta(hours=t) - offset for t in time]
time_idx = 237  # some random day in 2012，随意选一天。
cur_time = dt_time[time_idx]

# Plot of global temperature on our random day
fig = plt.figure()
fig.subplots_adjust(left=0., right=1., bottom=0., top=0.9)
# 首先构建一个map对象，给定它投影以及一些特征，在cartopy中使用axes
ax = plt.axes(projection=ccrs.Mollweide(180))
# 绘制coastlines（各大洲的边界线）和borders（国家的边界）
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)
air_cyclic = air[time_idx, :, :]
# transform 和 projection易混。核心概念是坐标轴的projection独立于数据定义的坐标系。
# 当画图并决定最终的图像的投影时，使用projection参数；而transform参数是告诉Cartopy数据是用什么坐标系定义的。
# data defined on a regular latitude/longitude grid 的坐标系是PlateCarree（普通的线性投影）
# 当没有提供transform参数时，默认的是假设坐标系与投影相匹配。
# 最安全的做法是不管最后的projection是什么，都指定transform参数，这样可选任意的projection以显示数据
# cmap参数指定colormap的颜色
cs = plt.contourf(lons, lats, air_cyclic, 11, cmap=plt.cm.Spectral_r, transform=ccrs.PlateCarree())
# 增加彩色条状图显示颜色对应的数值范围
cbar = plt.colorbar(cs, orientation='horizontal', shrink=0.5)
cbar.set_label("%s (%s)" % (nc_fid.variables['air'].var_desc, nc_fid.variables['air'].units))
# 添加标题，包括数据信息和日期
plt.title("%s on %s" % (nc_fid.variables['air'].var_desc, cur_time))

# Writing NetCDF files
# For this example, we will create two NetCDF4 files. One with the global air
# temperature departure from its value at Darwin, Australia. The other with
# the temperature profile for the entire year at Darwin.
darwin = {'name': 'Darwin, Australia', 'lat': -12.45, 'lon': 130.83}

# Find the nearest latitude and longitude for Darwin
lat_idx = np.abs(lats - darwin['lat']).argmin()
lon_idx = np.abs(lons - darwin['lon']).argmin()

# Simple example: temperature profile for the entire year at Darwin.
# Open a new NetCDF file to write the data to. For format, you can choose from
# 'NETCDF3_CLASSIC', 'NETCDF3_64BIT', 'NETCDF4_CLASSIC', and 'NETCDF4'
# 参数mode='w'表示是“写”netcdf文件的模式
w_nc_fid = Dataset('darwin_2012.nc', 'w', format='NETCDF4')
# 创建的w_nc_fid是空的，没有信息，先给其增加描述信息，这里使用的是之前读取的netcdf数据的信息
w_nc_fid.description = "NCEP/NCAR Reanalysis %s from its value at %s. %s" % (nc_fid.variables['air'].var_desc.lower(), \
                                                                             darwin['name'], nc_fid.description)
# Using our previous dimension info, we can create the new time dimension。创建维度信息
# Even though we know the size, we are going to set the size to unknown
w_nc_fid.createDimension('time', None)
# 创建变量信息，包括变量名称、变量数据类型，坐标变量。返回的是Variable变量
w_nc_dim = w_nc_fid.createVariable('time', nc_fid.variables['time'].dtype, ('time',))
# 设置全局属性，包括units、long_name等。You can do this step yourself but 前面的数据里已经有相关信息了.
for ncattr in nc_fid.variables['time'].ncattrs():
    w_nc_dim.setncattr(ncattr, nc_fid.variables['time'].getncattr(ncattr))
# Assign the dimension data to the new NetCDF file.
w_nc_fid.variables['time'][:] = time
# 添加一个air变量，其数据类型是float64，坐标变量也是time
w_nc_var = w_nc_fid.createVariable('air', 'f8', ('time'))
# 手动设置全局属性如下，u应该表示的是编码格式
w_nc_var.setncatts({'long_name': u"mean Daily Air temperature", 'units': u"degK", 'level_desc': u'Surface', \
                    'var_desc': u"Air temperature", 'statistic': u'Mean\nM'})
# 数据使用之前读取的数据放入到当前的netcdf对象中
w_nc_fid.variables['air'][:] = air[time_idx, lat_idx, lon_idx]
w_nc_fid.close()  # close the new file

# A plot of the temperature profile for Darwin in 2012
fig = plt.figure()
# c表示color颜色，r是红色，b是蓝色，先绘出固定坐标所有dt_time时间的数据
plt.plot(dt_time, air[:, lat_idx, lon_idx], c='r')
# marker是点的标记形式，绘出这一点
plt.plot(dt_time[time_idx], air[time_idx, lat_idx, lon_idx], c='b', marker='o')
# ha是让点的横坐标数据cur_time显示在点的右侧，默认是左侧
plt.text(dt_time[time_idx], air[time_idx, lat_idx, lon_idx], cur_time, ha='right')
# 害怕横坐标刻度的数据显示重叠，因此让横坐标的刻度倾斜
fig.autofmt_xdate()
plt.ylabel("%s (%s)" % (nc_fid.variables['air'].var_desc, nc_fid.variables['air'].units))
plt.xlabel("Time")
plt.title("%s from\n%s for %s" % (nc_fid.variables['air'].var_desc, darwin['name'], cur_time.year))

# Complex example: global temperature departure from its value at Darwin
departure = air[:, :, :] - air[:, lat_idx, lon_idx].reshape((time.shape[0], 1, 1))

# Open a new NetCDF file to write the data to. For format, you can choose from
# 'NETCDF3_CLASSIC', 'NETCDF3_64BIT', 'NETCDF4_CLASSIC', and 'NETCDF4'
w_nc_fid = Dataset('air.departure.sig995.2012.nc', 'w', format='NETCDF4')
w_nc_fid.description = "The departure of the NCEP/NCAR Reanalysis %s from its value at %s. %s" % \
                       (nc_fid.variables['air'].var_desc.lower(), darwin['name'], nc_fid.description)
# 创建多维度。Using our previous dimension information, we can create the new dimensions
data = {}
for dim in nc_dims:
    w_nc_fid.createDimension(dim, nc_fid.variables[dim].size)
    data[dim] = w_nc_fid.createVariable(dim, nc_fid.variables[dim].dtype, \
                                        (dim,))
    # You can do this step yourself but someone else did the work for us.
    for ncattr in nc_fid.variables[dim].ncattrs():
        data[dim].setncattr(ncattr, nc_fid.variables[dim].getncattr(ncattr))
# Assign the dimension data to the new NetCDF file.
w_nc_fid.variables['time'][:] = time
w_nc_fid.variables['lat'][:] = lats
w_nc_fid.variables['lon'][:] = lons

# Ok, time to create our departure variable
w_nc_var = w_nc_fid.createVariable('air_dep', 'f8', ('time', 'lat', 'lon'))
w_nc_var.setncatts({'long_name': u"mean Daily Air temperature departure", \
                    'units': u"degK", 'level_desc': u'Surface', \
                    'var_desc': u"Air temperature departure", \
                    'statistic': u'Mean\nM'})
w_nc_fid.variables['air_dep'][:] = departure
w_nc_fid.close()  # close the new file

# Rounded maximum absolute value of the departure used for contouring
max_dep = np.round(np.abs(departure[time_idx, :, :]).max() + 5., decimals=-1)

# Generate a figure of the departure for a single day
fig = plt.figure()
fig.subplots_adjust(left=0., right=1., bottom=0., top=0.9)
ax = plt.axes(projection=ccrs.Mollweide(180))
# 绘制coastlines（各大洲的边界线）和borders
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)

dep_cyclic = departure[time_idx, :, :]
levels = np.linspace(-max_dep, max_dep, 11)
cs = plt.contourf(lons, lats, dep_cyclic, levels=levels, cmap=plt.cm.bwr, transform=ccrs.PlateCarree())
x, y = darwin['lon'], darwin['lat']
# 点如果直接用plt画，没法设置transform，会导致显示的坐标不正确，因此用ax。
ax.plot(x, y, c='c', marker='o', transform=ccrs.PlateCarree())
ax.text(x, y, 'Darwin,\nAustralia', color='r', weight='semibold', transform=ccrs.PlateCarree())
cbar = plt.colorbar(cs, orientation='horizontal', shrink=0.5)
cbar.set_label("%s departure (%s)" % (nc_fid.variables['air'].var_desc, nc_fid.variables['air'].units))
plt.title("Departure of Global %s from\n%s for %s" % (nc_fid.variables['air'].var_desc, darwin['name'], cur_time))
plt.show()

# Close original NetCDF file.
nc_fid.close()
