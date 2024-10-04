# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:18:24 2024

@author: jablonski
"""

import logging
import os
import sys

import pandas as pd
import geopandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as path_effects
import matplotlib.patches as mpatches

logger = logging.getLogger('PT3S') 

class NcdD:
    def __init__(self, gdf=None, attr_colors=None, colors=None, patch_fmt=None, patch_values=None, legend_pos=None, norm_min=None, norm_max=None, query=None, ignore_values=None):
        self.gdf = gdf
        self.attr_colors = attr_colors
        self.colors = colors
        self.patch_fmt = patch_fmt
        self.patch_values = patch_values
        self.legend_pos = legend_pos if legend_pos is not None else 'best'
        self.norm_min = norm_min
        self.norm_max = norm_max
        self.query = query
        self.ignore_values = ignore_values if ignore_values is not None else []
        self.legend_handles_labels = []

    def accumulate_legend(self, ax):
        handles, labels = ax.get_legend_handles_labels()
        self.legend_handles_labels.extend(zip(handles, labels))

    def apply_ignore_values(self):
        if self.ignore_values:
            self.gdf = self.gdf[~self.gdf[self.attr_colors].isin(self.ignore_values)]


class NcdD_pipes(NcdD):
    def __init__(self, gdf, attr_colors, colors=None, patch_fmt=None, patch_values=None, legend_pos=None, norm_min=None, norm_max=None, query=None, line_width=None, ignore_values=None):
        super().__init__(gdf, attr_colors, colors, patch_fmt, patch_values, legend_pos, norm_min, norm_max, query, ignore_values)
        self.line_width = line_width if line_width is not None else 10

class NcdD_nodes(NcdD):
    def __init__(self, gdf, attr_colors, colors=None, patch_fmt=None, patch_values=None, legend_pos=None, norm_min=None, norm_max=None, query=None, marker_style=None, marker_size=None, ignore_values=None):
        super().__init__(gdf, attr_colors, colors, patch_fmt, patch_values, legend_pos, norm_min, norm_max, query, ignore_values)
        self.marker_style = marker_style if marker_style is not None else 'o'
        self.marker_size = marker_size if marker_size is not None else 10

def apply_ignore_values(df, attr_colors, ignore_values):
    """
    Filters out rows in the DataFrame where the specified attribute has values in the ignore_values list.

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


def pNcd_nodes(ax=None, axTitle=None, NcdD=None):
    """
    Plots the data from an NcdD object on the given axis using markers.

    :param ax: Matplotlib axis to plot on. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional, default=None
    :param axTitle: Title for the axis.
    :type axTitle: str, optional, default=None
    :param NcdD: NcdD object containing the data to be plotted.
    :type NcdD: NcdD
    """
    logStr = "{0:s}.{1:s}: ".format(__name__, sys._getframe().f_code.co_name)
    logger.debug("{0:s}{1:s}".format(logStr, 'Start.'))

    try:
        if ax is None:
            fig, ax = plt.subplots()
            logger.debug("{0:s}{1:s}".format(logStr, 'Created new axis.'))

        if NcdD is None:
            logger.debug("{0:s}{1:s}".format(logStr, 'No plot data provided.'))
            return

        gdf = NcdD.gdf
        if not gdf.empty:
            logger.debug("{0:s}{1:s}".format(logStr, f'Plotting {NcdD.attr_colors} data.'))

            # Apply ignore values
            NcdD.apply_ignore_values()

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

            # Create Legend Patches
            patch_values = NcdD.patch_values if NcdD.patch_values is not None else np.linspace(norm_min, norm_max, num=5)
            logger.debug("{0:s}patch_values: {1}".format(logStr, patch_values))
            patches = [mpatches.Patch(color=cmap(norm(value)), label=NcdD.patch_fmt.format(value)) for value in patch_values]

            # Accumulate legend handles and labels
            NcdD.accumulate_legend(ax)

    except Exception as e:
        logger.error("{0:s}{1:s} - {2}".format(logStr, 'Error.', str(e)))

    logger.debug("{0:s}{1:s}".format(logStr, 'End.'))

def pNcd_pipes(ax=None, axTitle=None, NcdD=None):
    """
    Plots the data from an NcdD object on the given axis using lines.

    :param ax: Matplotlib axis to plot on. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional, default=None
    :param axTitle: Title for the axis.
    :type axTitle: str, optional, default=None
    :param NcdD: NcdD object containing the data to be plotted.
    :type NcdD: NcdD
    """
    logStr = "{0:s}.{1:s}: ".format(__name__, sys._getframe().f_code.co_name)
    logger.debug("{0:s}{1:s}".format(logStr, 'Start.'))

    try:
        if ax is None:
            fig, ax = plt.subplots()
            logger.debug("{0:s}{1:s}".format(logStr, 'Created new axis.'))

        if NcdD is None:
            logger.debug("{0:s}{1:s}".format(logStr, 'No plot data provided.'))
            return

        gdf = NcdD.gdf
        if not gdf.empty:
            logger.debug("{0:s}{1:s}".format(logStr, f'Plotting {NcdD.attr_colors} data.'))

            # Apply ignore values
            NcdD.apply_ignore_values()

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
                    path_effects=[path_effects.Stroke(capstyle="round")])
            logger.debug("{0:s}{1:s}".format(logStr, f'Plotted {NcdD.attr_colors} data.'))

            # Create Legend Patches
            patch_values = NcdD.patch_values if NcdD.patch_values is not None else np.linspace(norm_min, norm_max, num=5)
            logger.debug("{0:s}patch_values: {1}".format(logStr, patch_values))
            patches = [mpatches.Patch(color=cmap(norm(value)), label=NcdD.patch_fmt.format(value)) for value in patch_values]

            # Accumulate legend handles and labels
            NcdD.accumulate_legend(ax)

    except Exception as e:
        logger.error("{0:s}{1:s} - {2}".format(logStr, 'Error.', str(e)))

    logger.debug("{0:s}{1:s}".format(logStr, 'End.'))
