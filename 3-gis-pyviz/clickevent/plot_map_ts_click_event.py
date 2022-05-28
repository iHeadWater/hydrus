import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cartopy.crs as ccrs
from cartopy.feature import NaturalEarthFeature
from matplotlib import gridspec
from matplotlib.cm import ScalarMappable
from mpl_toolkits.axes_grid1 import make_axes_locatable


def test_plot_map_ts(self):
    data_map = np.arange(5).tolist()
    lat = [24, 30, 40, 50, 50.5]
    lon = [-120, -110, -100, -90, -70]
    data_ts_obs_np = np.arange(30).reshape(5, 6)
    data_ts_pred_np = np.arange(30, 60).reshape(5, 6)
    data_ts = [
        [data_ts_obs_np[i], data_ts_pred_np[i]] for i in range(data_ts_obs_np.shape[0])
    ]
    print(data_ts)
    t = np.arange(6).tolist()
    sites_id = ["01", "02", "03", "04", "05"]
    plot_ts_map(data_map, data_ts, lat, lon, t, sites_id)


def plot_map_carto(
    data, lat, lon, ax=None, pertile_range=None, fig_size=(8, 8), cmap_str="viridis"
):
    temp = data
    if pertile_range is None:
        vmin = np.amin(temp)
        vmax = np.amax(temp)
    else:
        assert 0 <= pertile_range[0] < pertile_range[1] <= 100
        vmin = np.percentile(temp, pertile_range[0])
        vmax = np.percentile(temp, pertile_range[1])
    llcrnrlat = (np.min(lat),)
    urcrnrlat = (np.max(lat),)
    llcrnrlon = (np.min(lon),)
    urcrnrlon = (np.max(lon),)
    extent = [llcrnrlon[0], urcrnrlon[0], llcrnrlat[0], urcrnrlat[0]]
    # Figure
    only_map = False
    if ax is None:
        fig, ax = plt.subplots(
            1, 1, figsize=fig_size, subplot_kw={"projection": ccrs.PlateCarree()}
        )
        only_map = True
    ax.set_extent(extent)
    states = NaturalEarthFeature(
        category="cultural",
        scale="50m",
        facecolor="none",
        name="admin_1_states_provinces_shp",
    )
    ax.add_feature(states, linewidth=0.5, edgecolor="black")
    ax.coastlines("50m", linewidth=0.8)
    # auto projection
    scat = plt.scatter(lon, lat, c=temp, s=10, cmap=cmap_str, vmin=vmin, vmax=vmax)

    if only_map:
        # get size and extent of axes:
        axpos = ax.get_position()
        pos_x = axpos.x0 + axpos.width + 0.01  # + 0.25*axpos.width
        pos_y = axpos.y0
        cax_width = 0.02
        cax_height = axpos.height
        # create new axes where the colorbar should go.
        # it should be next to the original axes and have the same height!
        pos_cax = fig.add_axes([pos_x, pos_y, cax_width, cax_height])
        plt.colorbar(ax=ax, cax=pos_cax)
        return fig
    else:
        plt.colorbar()
    return scat, ax


def plot_ts_matplot(t, y, color="r", ax=None, title=None):
    assert type(t) == list
    assert type(y) == list
    if ax is None:
        fig = plt.figure()
        ax = fig.subplots()
    ax.plot(t, y[0], color=color, label="pred")
    ax.plot(t, y[1], label="obs")
    ax.legend()
    if title is not None:
        ax.set_title(title, loc="center")
    if ax is None:
        return fig, ax
    else:
        return ax


def plot_ts_map(dataMap, dataTs, lat, lon, t, sites_id, pertile_range=None):
    # show the map in a pop-up window
    matplotlib.use("TkAgg")
    assert type(dataMap) == list
    assert type(dataTs) == list
    # setup axes
    fig = plt.figure(figsize=(8, 8), dpi=100)
    gs = gridspec.GridSpec(2, 1)
    # plt.subplots_adjust(left=0.13, right=0.89, bottom=0.05)
    # plot maps
    ax1 = plt.subplot(gs[0], projection=ccrs.PlateCarree())
    scat, ax1 = plot_map_carto(
        dataMap, lat=lat, lon=lon, ax=ax1, pertile_range=pertile_range
    )
    # line plot
    ax2 = plt.subplot(gs[1])

    # plot ts
    def onclick(event):
        print("click event")
        # refresh the ax2, then new ts data can be showed without previous one
        ax2.cla()
        xClick = event.xdata
        yClick = event.ydata
        d = np.sqrt((xClick - lon) ** 2 + (yClick - lat) ** 2)
        ind = np.argmin(d)
        titleStr = "site_id %s, lat %.3f, lon %.3f" % (
            sites_id[ind],
            lat[ind],
            lon[ind],
        )
        tsLst = dataTs[ind]
        plot_ts_matplot(t, tsLst, ax=ax2, title=titleStr)
        # following funcs both work
        fig.canvas.draw()
        # plt.draw()

    fig.canvas.mpl_connect("button_press_event", onclick)
    plt.show()
