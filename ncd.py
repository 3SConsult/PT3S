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

    def __init__(self, gdf, preset, attr_colors=None, colors=None, line_width=None, patch_fmt=None, patch_values=None, norm_min=None, norm_max=None, query=None, marker_style=None, marker_size=None, manual_col=None):
        
        """
        Initializes the NcdD object with the given parameters and preset configurations.

        :param gdf: GeoDataFrame containing the data to be plotted.
        :type gdf: geopandas.GeoDataFrame
        :param preset: Preset configuration for the plot. Options include 'Manual', 'DI', 'W0', 'QMAVAbs', 'QM'.
        :type preset: str
        :param attr_colors: Attribute used for coloring the plot. Overrides preset if provided.
        :type attr_colors: str, optional, default=None
        :param colors: List of colors for the colormap. Overrides preset if provided.
        :type colors: list, optional, default=None
        :param attr_lws: Line width scaling factor. Overrides preset if provided.
        :type attr_lws: int, optional, default=None
        :param patch_fmt: Format string for legend patches. Overrides preset if provided.
        :type patch_fmt: str, optional, default=None
        :param patch_values: Values for legend patches. Overrides preset if provided.
        :type patch_values: list, optional, default=None
        :param query: Query string to filter the GeoDataFrame.
        :type query: str, optional, default=None
        :param marker_style: Marker style for the plot. Overrides preset if provided.
        :type marker_style: str, optional, default=None
        :param marker_size: Marker size scaling factor. Overrides preset if provided.
        :type marker_size: int, optional, default=None
        :param manual_col: Column used for manual plotting. Only used if preset is 'Manual'.
        :type manual_col: str, optional, default=None
        """
        self.gdf = gdf
        self.preset = preset
        
        # Initialize all attributes
        self.attr_colors = None
        self.colors = None
        self.line_width = None
        self.patch_fmt = None
        self.patch_values = None
        self.norm_min = None
        self.norm_max = None
        self.query = None
        self.marker_style = None
        self.marker_size = None
        self.manual_col = None

        # Set default values based on preset
        if self.preset == 'Manual':
            self.manual_col = self.manual_col
        elif self.preset == 'DI':
            self.attr_colors = 'DI'
            self.colors = ['lightgray', 'dimgray']
            self.line_width = 25
            self.patch_fmt = "DN (Innen) {:4.0f}"
        elif self.preset == 'W0':
            self.attr_colors = 'W0'
            self.colors = ['oldlace', 'orange'] 
            self.patch_fmt = "W {:4.0f} kW"  
            self.marker_style = 'o'
            self.marker_size = 250
        elif self.preset == 'QMAVAbs':
            self.attr_colors = 'QMAVAbs'
            self.colors = ['darkgreen','magenta']
            self.line_width = 20
            self.patch_fmt = "Q (abs.) {:4.0f} t/h"
        elif self.preset == 'QM':
            self.attr_colors = 'QM'
            self.colors = ['aquamarine','teal'] 
            self.patch_fmt = "dp {:4.1f} bar"  
            self.patch_values = "dp -{:4.1f} bar"  
            self.marker_style = 'o'
            self.marker_size = 250

        # Overwrite preset values with entered arguments if provided
        self.attr_colors = attr_colors if attr_colors is not None else self.attr_colors
        self.colors = colors if colors is not None else self.colors
        self.line_width = line_width if line_width is not None else self.line_width
        self.patch_fmt = patch_fmt if patch_fmt is not None else self.patch_fmt
        self.patch_values = patch_values if patch_values is not None else self.patch_values
        self.norm_min = norm_min if norm_min is not None else self.norm_min
        self.norm_max = norm_max if norm_max is not None else self.norm_max
        self.query = query if query is not None else self.query
        self.marker_style = marker_style if marker_style is not None else self.marker_style
        self.marker_size = marker_size if marker_size is not None else self.marker_size


def pNcd_DH(ax=None, axTitle=None, NcdD_list=None):
    """
    Plots the data from a list of NcdD objects on the given axis.

    :param ax: Matplotlib axis to plot on. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional, default=None
    :param axTitle: Title for the axis.
    :type axTitle: str, optional, default=None
    :param NcdD_list: List of NcdD objects containing the data to be plotted.
    :type NcdD_list: list of NcdD
    """
    logStr = "{0:s}.{1:s}: ".format(__name__, sys._getframe().f_code.co_name)
    logger.debug("{0:s}{1:s}".format(logStr, 'Start.'))

    try:
        if ax is None:
            fig, ax = plt.subplots()
            logger.debug("{0:s}{1:s}".format(logStr, 'Created new axis.'))

        if NcdD_list is None:
            logger.debug("{0:s}{1:s}".format(logStr, 'No plot data provided.'))
            return

        all_patches = []

        for NcdD in NcdD_list:
            gdf = NcdD.gdf
            if not gdf.empty:
                logger.debug("{0:s}{1:s}".format(logStr, f'Plotting {NcdD.attr_colors} data.'))

                # Create Colormap
                cmap = mcolors.LinearSegmentedColormap.from_list('cmap', NcdD.colors, N=256)
                norm_min = NcdD.norm_min if NcdD.norm_min is not None else gdf[NcdD.attr_colors].min()
                norm_max = NcdD.norm_max if NcdD.norm_max is not None else gdf[NcdD.attr_colors].max()
                norm = plt.Normalize(vmin=norm_min, vmax=norm_max)
                logger.debug("{0:s}norm_min: {1:10.2f} norm_max: {2:10.2f}".format(logStr, norm_min, norm_max))

                # Filter and Sort Data if Query is Provided
                df = gdf.query(NcdD.query) if NcdD.query else gdf
                df = df.sort_values(by=[NcdD.attr_colors], ascending=True)
                
                # Plotting Data
                if NcdD.preset == 'DI' or NcdD.preset == 'QMAVAbs':
                    # Plotting with lines
                    df.plot(ax=ax,
                            linewidth=norm(df[NcdD.attr_colors]) * NcdD.line_width,
                            color=cmap(norm(df[NcdD.attr_colors].astype(float))),
                            path_effects=[path_effects.Stroke(capstyle="round")])
                elif NcdD.preset == 'W0' or NcdD.preset == 'QM':
                    # Plotting with Markers
                    size_norm_min = df[NcdD.attr_colors].min()
                    size_norm_max = df[NcdD.attr_colors].max()
                    size_norm = plt.Normalize(vmin=size_norm_min, vmax=size_norm_max)
                    sizes = size_norm(df[NcdD.attr_colors].astype(float)) * NcdD.marker_size # Scale sizes appropriately
                   
                    # Plotting with Markers
                    df.plot(ax=ax,
                            marker=NcdD.marker_style,
                            markersize=sizes,
                            color=cmap(norm(df[NcdD.attr_colors].astype(float))),
                            path_effects=[path_effects.Stroke(capstyle="round")])
                elif NcdD.preset == 'KNOT':
                    # Placeholder for KNOT Plotting
                    pass
                elif NcdD.preset == 'Manual':
                    # Placeholder for Manual Plotting
                    pass               
                logger.debug("{0:s}{1:s}".format(logStr, f'Plotted {NcdD.attr_colors} data.'))

                # Create Legend Patches
                patch_values = NcdD.patch_values if NcdD.patch_values is not None else np.linspace(norm_min, norm_max, num=5)
                logger.debug("{0:s}patch_values: {1}".format(logStr, patch_values))
                patches = [mpatches.Patch(color=cmap(norm(value)), label=NcdD.patch_fmt.format(value)) for value in patch_values]
                all_patches.extend(patches)

        # Set Aspect Ratio
        ax.set_aspect('equal', adjustable='datalim')
        logger.debug("{0:s}{1:s}".format(logStr, 'Set aspect ratio to equal.'))

        # Add Legend
        ax.legend(handles=all_patches, loc='best')
        logger.debug("{0:s}{1:s}".format(logStr, 'Added legend.'))

    except Exception as e:
        logger.error("{0:s}{1:s} - {2}".format(logStr, 'Error.', str(e)))

    logger.debug("{0:s}{1:s}".format(logStr, 'End.'))