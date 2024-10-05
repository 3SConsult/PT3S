# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:18:24 2024

@author: jablonski
"""

import logging
import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as path_effects
import matplotlib.patches as mpatches
import Rm

logger = logging.getLogger('PT3S') 

class NcdD:
    """
    NcdD: Base class for handling geospatial data and plotting attributes.

    :param gdf: Geospatial DataFrame containing the data to plot.
    :type gdf: geopandas.GeoDataFrame, optional
    :param attr_colors: Column name in gdf to use for coloring the plot.
    :type attr_colors: str, optional
    :param colors: List of colors to use for the colormap.
    :type colors: list, optional
    :param patch_fmt: Format string for legend patches.
    :type patch_fmt: str, optional
    :param patch_values: Specific values to use for legend patches.
    :type patch_values: list, optional
    :param norm_min: Minimum value for normalization.
    :type norm_min: float, optional
    :param norm_max: Maximum value for normalization.
    :type norm_max: float, optional
    :param query: Query string to filter the data.
    :type query: str, optional
    :param ignore_values: List of values to ignore in the attr_colors column.
    :type ignore_values: list, optional
    """
    
    def __init__(self, gdf=None, attr_colors=None, colors=None, patch_fmt=None, patch_values=None, norm_min=None, norm_max=None, query=None, ignore_values=None):
        self.gdf = gdf
        self.attr_colors = attr_colors
        self.colors = colors
        self.patch_fmt = patch_fmt
        self.patch_values = patch_values
        self.norm_min = norm_min
        self.norm_max = norm_max
        self.query = query
        self.ignore_values = ignore_values if ignore_values is not None else []
        self.legend_handles_labels = []

class NcdD_pipes(NcdD):
    """
    NcdD_pipes: Subclass of NcdD for handling and plotting pipe data.

    :param gdf: Geospatial DataFrame containing the data to plot.
    :type gdf: geopandas.GeoDataFrame
    :param attr_colors: Column name in gdf to use for coloring the plot.
    :type attr_colors: str
    :param colors: List of colors to use for the colormap.
    :type colors: list, optional
    :param patch_fmt: Format string for legend patches.
    :type patch_fmt: str, optional
    :param patch_values: Specific values to use for legend patches.
    :type patch_values: list, optional
    :param norm_min: Minimum value for normalization.
    :type norm_min: float, optional
    :param norm_max: Maximum value for normalization.
    :type norm_max: float, optional
    :param query: Query string to filter the data.
    :type query: str, optional
    :param line_width: Width of the lines in the plot.
    :type line_width: float, optional
    :param ignore_values: List of values to ignore in the attr_colors column.
    :type ignore_values: list, optional
    """
    
    def __init__(self, gdf, attr_colors, colors=None, patch_fmt=None, patch_values=None, norm_min=None, norm_max=None, query=None, line_width=None, ignore_values=None):
        super().__init__(gdf, attr_colors, colors, patch_fmt, patch_values, norm_min, norm_max, query, ignore_values)
        self.line_width = line_width if line_width is not None else 10


class NcdD_nodes(NcdD):
    """
    NcdD_nodes: Subclass of NcdD for handling and plotting node data.

    :param gdf: Geospatial DataFrame containing the data to plot.
    :type gdf: geopandas.GeoDataFrame
    :param attr_colors: Column name in gdf to use for coloring the plot.
    :type attr_colors: str
    :param colors: List of colors to use for the colormap.
    :type colors: list, optional
    :param patch_fmt: Format string for legend patches.
    :type patch_fmt: str, optional
    :param patch_values: Specific values to use for legend patches.
    :type patch_values: list, optional
    :param norm_min: Minimum value for normalization.
    :type norm_min: float, optional
    :param norm_max: Maximum value for normalization.
    :type norm_max: float, optional
    :param query: Query string to filter the data.
    :type query: str, optional
    :param marker_style: Style of the markers in the plot.
    :type marker_style: str, optional
    :param marker_size: Size of the markers in the plot.
    :type marker_size: float, optional
    :param ignore_values: List of values to ignore in the attr_colors column.
    :type ignore_values: list, optional
    """
    
    def __init__(self, gdf, attr_colors, colors=None, patch_fmt=None, patch_values=None, norm_min=None, norm_max=None, query=None, marker_style=None, marker_size=None, ignore_values=None):
        super().__init__(gdf, attr_colors, colors, patch_fmt, patch_values, norm_min, norm_max, query, ignore_values)
        self.marker_style = marker_style if marker_style is not None else 'o'
        self.marker_size = marker_size if marker_size is not None else 10


def pNcd_nodes(ax=None, NcdD_list=None):
    """
    pNcd_nodes: Plots nodes with specified attributes and colors.

    :param ax: Matplotlib axis object. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional
    :param NcdD_list: List of objects containing plotting data and attributes.
    :type NcdD_list: list of NcdD objects, optional

    :return: List of legend patches.
    :rtype: list of matplotlib.patches.Patch
    """
    logStr = "{0:s}.{1:s}: ".format(__name__, sys._getframe().f_code.co_name)
    logger.debug("{0:s}{1:s}".format(logStr, 'Start.'))

    try:
        if ax is None:
            fig, ax = plt.subplots(figsize=Rm.DINA3q)
            logger.debug("{0:s}{1:s}".format(logStr, 'Created new axis.'))

        if NcdD_list is None or not NcdD_list:
            logger.debug("{0:s}{1:s}".format(logStr, 'No plot data provided.'))
            return

        all_patches = []
        for NcdD in NcdD_list:
            gdf = NcdD.gdf
            if not gdf.empty:
                logger.debug("{0:s}{1:s}".format(logStr, f'Plotting {NcdD.attr_colors} data.'))

                # Apply ignore values
                if NcdD.ignore_values:
                    gdf = apply_ignore_values(gdf, NcdD.attr_colors, NcdD.ignore_values)

                # Create Colormap
                cmap = mcolors.LinearSegmentedColormap.from_list('cmap', NcdD.colors, N=256)
                norm_min = NcdD.norm_min if NcdD.norm_min is not None else gdf[NcdD.attr_colors].min()
                norm_max = NcdD.norm_max if NcdD.norm_max is not None else gdf[NcdD.attr_colors].max()
                norm = plt.Normalize(vmin=norm_min, vmax=norm_max)
                logger.debug("{0:s}norm_min: {1:10.2f} norm_max: {2:10.2f}".format(logStr, norm_min, norm_max))

                # Filter and Sort Data if Query is Provided
                df = gdf.query(NcdD.query) if NcdD.query else gdf
                df = df.sort_values(by=[NcdD.attr_colors], ascending=True)
                
                # Plotting Data with Markers
                size_norm_min = df[NcdD.attr_colors].min()
                size_norm_max = df[NcdD.attr_colors].max()
                size_norm = plt.Normalize(vmin=size_norm_min, vmax=size_norm_max)
                marker_size = NcdD.marker_size if NcdD.marker_size is not None else 10  # Default marker size
                sizes = size_norm(df[NcdD.attr_colors].astype(float)) * marker_size  # Scale sizes appropriately

                df.plot(ax=ax,
                        marker=NcdD.marker_style,
                        markersize=sizes,
                        linestyle='None',  # No lines, only markers
                        color=cmap(norm(df[NcdD.attr_colors].astype(float))),
                        path_effects=[path_effects.Stroke(capstyle="round")])
                logger.debug("{0:s}{1:s}".format(logStr, f'Plotted {NcdD.attr_colors} data.'))
                
                plt.axis('off')
                
                # Create Legend Patches
                patch_values = NcdD.patch_values if NcdD.patch_values is not None else np.linspace(norm_min, norm_max, num=5)
                logger.debug("{0:s}patch_values: {1}".format(logStr, patch_values))
                patches = [mpatches.Patch(color=cmap(norm(value)), label=NcdD.patch_fmt.format(value)) for value in patch_values]
                all_patches.extend(patches)

        return all_patches

    except Exception as e:
        logger.error("{0:s}{1:s} - {2}".format(logStr, 'Error.', str(e)))

    logger.debug("{0:s}{1:s}".format(logStr, 'End.'))


def apply_ignore_values(df, attr_colors, ignore_values):
    """
    apply_ignore_values: Filters out rows in the DataFrame where the specified attribute has values in the ignore_values list.

    :param df: DataFrame to filter.
    :type df: pandas.DataFrame
    :param attr_colors: Column name to check for ignore values.
    :type attr_colors: str
    :param ignore_values: List of values to ignore.
    :type ignore_values: list

    :return: Filtered DataFrame.
    :rtype: pandas.DataFrame
    """
    return df[~df[attr_colors].isin(ignore_values)]


def pNcd_pipes(ax=None, NcdD_list=None):
    """
    pNcd_pipes: Plots pipes with specified attributes and colors.

    :param ax: Matplotlib axis object. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional
    :param NcdD_list: List of objects containing plotting data and attributes.
    :type NcdD_list: list of NcdD objects, optional

    :return: List of legend patches.
    :rtype: list of matplotlib.patches.Patch
    """
    logStr = "{0:s}.{1:s}: ".format(__name__, sys._getframe().f_code.co_name)
    logger.debug("{0:s}{1:s}".format(logStr, 'Start.'))

    try:
        if ax is None:
            fig, ax = plt.subplots(figsize=Rm.DINA3q)
            logger.debug("{0:s}{1:s}".format(logStr, 'Created new axis.'))

        if NcdD_list is None or not NcdD_list:
            logger.debug("{0:s}{1:s}".format(logStr, 'No plot data provided.'))
            return

        all_patches = []
        for NcdD in NcdD_list:
            gdf = NcdD.gdf
            if not gdf.empty:
                logger.debug("{0:s}{1:s}".format(logStr, f'Plotting {NcdD.attr_colors} data.'))

                # Apply ignore values
                if NcdD.ignore_values:
                    gdf = apply_ignore_values(gdf, NcdD.attr_colors, NcdD.ignore_values)

                # Create Colormap
                cmap = mcolors.LinearSegmentedColormap.from_list('cmap', NcdD.colors, N=256)
                norm_min = NcdD.norm_min if NcdD.norm_min is not None else gdf[NcdD.attr_colors].min()
                norm_max = NcdD.norm_max if NcdD.norm_max is not None else gdf[NcdD.attr_colors].max()
                norm = plt.Normalize(vmin=norm_min, vmax=norm_max)
                logger.debug("{0:s}norm_min: {1:10.2f} norm_max: {2:10.2f}".format(logStr, norm_min, norm_max))

                # Filter and Sort Data if Query is Provided
                df = gdf.query(NcdD.query) if NcdD.query else gdf
                df = df.sort_values(by=[NcdD.attr_colors], ascending=True)
                
                # Plotting Data with Lines
                df.plot(ax=ax,
                        linewidth=norm(df[NcdD.attr_colors]) * NcdD.line_width,
                        color=cmap(norm(df[NcdD.attr_colors].astype(float))),
                        path_effects=[path_effects.Stroke(capstyle="round")],
                        label=NcdD.attr_colors)  # Add label for legend
                logger.debug("{0:s}{1:s}".format(logStr, f'Plotted {NcdD.attr_colors} data.'))
                
                plt.axis('off')
                
                # Create Legend Patches
                patch_values = NcdD.patch_values if NcdD.patch_values is not None else np.linspace(norm_min, norm_max, num=5)
                logger.debug("{0:s}patch_values: {1}".format(logStr, patch_values))
                patches = [mpatches.Patch(color=cmap(norm(value)), label=NcdD.patch_fmt.format(value)) for value in patch_values]
                all_patches.extend(patches)

        return all_patches

    except Exception as e:
        logger.error("{0:s}{1:s} - {2}".format(logStr, 'Error.', str(e)))

    logger.debug("{0:s}{1:s}".format(logStr, 'End.'))
