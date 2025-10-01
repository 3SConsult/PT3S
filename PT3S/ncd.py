# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:18:24 2024

@author: jablonski
"""

import logging
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as path_effects
import matplotlib.patches as mpatches
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.colors import Normalize
from matplotlib.collections import LineCollection
from difflib import get_close_matches

try:
    from PT3S import Rm
except:
    import Rm

logger = logging.getLogger('PT3S')

def pNcd_pipes(ax=None, gdf=None, attribute=None, colors=['darkgreen', 'magenta'], legend_fmt=None, legend_values=None, norm_min=None, norm_max=None, query=None, line_width_factor=10, zorder=None):
    """
    pNcd_pipes: Plots pipes on axis with customization options.

    :param ax: Matplotlib axis object. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional
    :param gdf: Geospatial DataFrame containing the data to plot.
    :type gdf: geopandas.GeoDataFrame
    :param attribute: Column name in gdf of the data that should be plotted.
    :type attribute: str
    :param colors: List of colors to use for the colormap. Default is ['darkgreen', 'magenta'].
    :type colors: list, optional
    :param legend_fmt: Legend text for attribute. Default is attribute + '{:.4f}'.
    :type legend_fmt: str, optional
    :param legend_values: Specific values to use for value steps in legend. Default is None.
    :type legend_values: list, optional
    :param norm_min: Minimum value for normalization. Default is None.
    :type norm_min: float, optional
    :param norm_max: Maximum value for normalization. Default is None.
    :type norm_max: float, optional
    :param query: Query string to filter the data. Default is None.
    :type query: str, optional
    :param line_width_factor: Factor to influence width of the lines in the plot. Default is 10.
    :type line_width_factor: float, optional
    :param zorder: Determines order of plotting when calling the function multilpe times. Default is None.
    :type zorder: float, optional
    
    :return: patches.
    :rtype: matplotlib.patches.Patch
    """
    logStr = "{0:s}.{1:s}: ".format(__name__, sys._getframe().f_code.co_name)
    logger.debug("{0:s}{1:s}".format(logStr, 'Start.'))

    try:
        if ax is None:
            fig, ax = plt.subplots(figsize=(11.7, 8.3))  # A3 size
            logger.debug("{0:s}{1:s}".format(logStr, 'Created new axis.'))

        if gdf is None or gdf.empty:
            logger.debug("{0:s}{1:s}".format(logStr, 'No plot data provided.'))
            return
        if isinstance(attribute, list):
            pass
        else:
            # Set default legend_fmt if not provided
            if legend_fmt is None:
                legend_fmt = attribute + ' {:4.0f}'
            logger.debug("Fine 1")
            # Create Colormap
            cmap = mcolors.LinearSegmentedColormap.from_list('cmap', colors, N=256)
            norm_min = norm_min if norm_min is not None else gdf[attribute].min()
            norm_max = norm_max if norm_max is not None else gdf[attribute].max()
            norm = plt.Normalize(vmin=norm_min, vmax=norm_max)
            logger.debug("{0:s}norm_min: {1:10.2f} norm_max: {2:10.2f}".format(logStr, norm_min, norm_max))
            # Filter and Sort Data if Query is Provided
            df = gdf.query(query) if query else gdf
            df = df.sort_values(by=[attribute], ascending=True)

            # Plotting Data with Lines
            sizes = norm(df[attribute].astype(float)) * line_width_factor  # Scale sizes appropriately
            
            df.plot(ax=ax,
                    linewidth=sizes,
                    color=cmap(norm(df[attribute].astype(float))),
                    path_effects=[path_effects.Stroke(capstyle="round")],
                    label=attribute,
                    #alpha=0.5,
                    zorder=zorder)  # Add label for legend
            logger.debug("{0:s}{1:s}".format(logStr, f'Plotted {attribute} data.'))

            plt.axis('off')
            # Create Legend Patches
            legend_values = legend_values if legend_values is not None else np.linspace(norm_min, norm_max, num=5)
            logger.debug("{0:s}legend_values: {1}".format(logStr, legend_values))
            patches = [mpatches.Patch(color=cmap(norm(value)), label=legend_fmt.format(value)) for value in legend_values]

            return patches
        
    except Exception as e:
        logger.error("{0:s}{1:s} - {2}".format(logStr, 'Error.', str(e)))

    logger.debug("{0:s}{1:s}".format(logStr, 'End.'))

def pNcd_nodes(ax=None, gdf=None, attribute=None, colors=['darkgreen', 'magenta'], legend_fmt=None, legend_values=None, norm_min=None, norm_max=None, query=None, marker_style='o', marker_size_factor=1000.0, zorder=None):
    """
    pNcd_nodes: Plots nodes on axis with customization options.

    :param ax: Matplotlib axis object. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional
    :param gdf: Geospatial DataFrame containing the data to plot.
    :type gdf: geopandas.GeoDataFrame
    :param attribute: Column name in gdf of the data that should be plotted.
    :type attribute: str
    :param colors: List of colors to use for the colormap. Default is ['darkgreen', 'magenta'].
    :type colors: list, optional
    :param legend_fmt: Legend text for attribute. Default is attribute + '{:.4f}'.
    :type legend_fmt: str, optional
    :param legend_values: Specific values to use for value steps in legend. Default is None.
    :type legend_values: list, optional
    :param norm_min: Minimum value for normalization. Default is None.
    :type norm_min: float, optional
    :param norm_max: Maximum value for normalization. Default is None.
    :type norm_max: float, optional
    :param query: Query string to filter the data. Default is None.
    :type query: str, optional
    :param marker_style: Style of the markers in the plot. Default is 'o'.
    :type marker_style: str, optional
    :param marker_size_factor: Factor to influence size of the markers in the plot. Default is 1000.0.
    :type marker_size_factor: float, optional
    :param zorder: Determines order of plotting when calling the function multilpe times. Default is None.
    :type zorder: float, optional
    
    :return: patches.
    :rtype: matplotlib.patches.Patch
    """
    logStr = "{0:s}.{1:s}: ".format(__name__, sys._getframe().f_code.co_name)
    logger.debug("{0:s}{1:s}".format(logStr, 'Start.'))

    try:
        if ax is None:
            fig, ax = plt.subplots(figsize=(11.7, 8.3))  # A3 size
            logger.debug("{0:s}{1:s}".format(logStr, 'Created new axis.'))

        if gdf is None or gdf.empty:
            logger.debug("{0:s}{1:s}".format(logStr, 'No plot data provided.'))
            return

        # Set default legend_fmt if not provided
        if legend_fmt is None:
            legend_fmt = attribute + ' {:4.0f}'

        # Create Colormap
        cmap = mcolors.LinearSegmentedColormap.from_list('cmap', colors, N=256)
        norm_min = norm_min if norm_min is not None else gdf[attribute].min()
        norm_max = norm_max if norm_max is not None else gdf[attribute].max()
        norm = plt.Normalize(vmin=norm_min, vmax=norm_max)
        logger.debug("{0:s}norm_min: {1:10.2f} norm_max: {2:10.2f}".format(logStr, norm_min, norm_max))

        # Filter and Sort Data if Query is Provided
        df = gdf.query(query) if query else gdf
        df = df.sort_values(by=[attribute], ascending=True)
        
        # Plotting Data with Markers
        sizes = norm(df[attribute].astype(float)) * marker_size_factor  # Scale sizes appropriately
        df.plot(ax=ax,
                marker=marker_style,
                markersize=sizes,
                linestyle='None',  # No lines, only markers
                color=cmap(norm(df[attribute].astype(float))),
                path_effects=[path_effects.Stroke(capstyle="round")],
                zorder=zorder)
        logger.debug("{0:s}{1:s}".format(logStr, f'Plotted {attribute} data.'))

        plt.axis('off')
        # Create Legend Patches
        legend_values = legend_values if legend_values is not None else np.linspace(norm_min, norm_max, num=5)
        logger.debug("{0:s}legend_values: {1}".format(logStr, legend_values))
        patches = [mpatches.Patch(color=cmap(norm(value)), label=legend_fmt.format(value)) for value in legend_values]

        return patches

    except Exception as e:
        logger.error("{0:s}{1:s} - {2}".format(logStr, 'Error.', str(e)))

    logger.debug("{0:s}{1:s}".format(logStr, 'End.'))

# Quellspektren
def mix_colors(vector, colors):
    """
    Mixes colors based on the provided vector.

    :param vector: A vector of weights for the colors.
    :type vector: np.ndarray
    :param colors: An array of colors to be mixed.
    :type colors: np.ndarray
    :return: The mixed color as an integer array.
    :rtype: np.ndarray
    """
    vector = np.array(vector, dtype=float)  # Ensure the vector is of type float
    vector /= vector.sum()  # Normalize the vector so that its elements sum to 1
    colors_array = np.array(colors, dtype=float)  # Ensure the colors are of type float
    mixed_color = np.dot(vector, colors_array)
    return mixed_color.astype(int)

def convert_to_hex(color_array):
    """
    Converts an RGB color array to a hexadecimal color string.

    :param color_array: An array with RGB values.
    :type color_array: np.ndarray
    :return: The hexadecimal color string.
    :rtype: str
    """
    hex_color = "#{:02x}{:02x}{:02x}".format(int(color_array[0]), int(color_array[1]), int(color_array[2]))
    logger.debug(f"Converted color: {hex_color}")
    return hex_color

def _add_mixture_scale(ax, colors, source_labels=None, language='en'):
    """
    Adds an inset scale that visualizes source mixtures.
    - 2 sources: horizontal gradient with % ticks.
    - 3 sources: ternary triangle with sampled points.
    - >3 sources: compact sample strip of mixtures.
    """

    n = len(colors)
    if source_labels is None:
        source_labels = [f"Source {i+1}" for i in range(n)]

    # Normalize colors to 0..1 for imshow/scatter usage
    cols_np = np.array(colors, dtype=float).clip(0, 255)

    def _mix(w):
        # w is a weight vector summing to 1
        c = np.dot(w, cols_np) / 255.0
        return np.clip(c, 0, 1)

    if n == 2:
            axins = inset_axes(ax, width="50%", height="4%", loc="lower left", borderpad=1.0)
            t = np.linspace(0, 1, 256)
            grad = np.array([_mix([1 - x, x]) for x in t], dtype=float)
            img = np.expand_dims(grad, axis=0)
            axins.imshow(img, aspect="auto")
            axins.set_yticks([])

            # bottom ticks (Source 2)
            xticks = np.linspace(0, 255, 5)
            perc = np.linspace(0, 100, 5).astype(int)
            axins.set_xticks(xticks)
            axins.set_xticklabels([f"{p}%" for p in perc], fontsize=8)
            axins.set_xlabel(f"Share of Source 2", fontsize=8)

            # style: no frame, no tick marks, transparent bg
            axins.set_facecolor((0, 0, 0, 0))
            axins.tick_params(axis='both', which='both', length=0)
            for s in axins.spines.values():
                s.set_visible(False)

            # top ticks (Source 1)
            axins_top = axins.twiny()
            axins_top.set_xlim(axins.get_xlim())
            axins_top.set_xticks(xticks)
            axins_top.set_xticklabels([f"{100 - p}%" for p in perc], fontsize=8)
            axins_top.set_xlabel(f"Share of Source 1", fontsize=8)
            axins_top.tick_params(axis='both', which='both', length=0)
            axins_top.set_frame_on(False)
            for s in axins_top.spines.values():
                s.set_visible(False)

    elif n == 3:
        # --- 3-source ternary inset --------------------------------------------------
        axins = inset_axes(ax, width="35%", height="35%", loc="lower left", borderpad=1.0)
        axins.set_aspect('equal')
        axins.axis('off')

        # Triangle vertices
        A = np.array([0.0, 0.0])                     # S1
        B = np.array([1.0, 0.0])                     # S2
        C = np.array([0.5, np.sqrt(3)/2])            # S3

        # Outline
        axins.plot([A[0], B[0], C[0], A[0]],
                   [A[1], B[1], C[1], A[1]],
                   color="#555", lw=0.8)

        # Sample grid on simplex
        steps = 10  # increase for smoother filling
        pts_xy = []
        pts_c = []
        for i in range(steps + 1):
            for j in range(steps + 1 - i):
                k = steps - i - j
                w = np.array([i, j, k], dtype=float) / steps  # (S1,S2,S3)
                # Barycentric → Cartesian: x = b*B.x + c*C.x ; y = c*C.y
                x = w[1] * B[0] + w[2] * C[0]
                y = w[2] * C[1]
                pts_xy.append([x, y])
                pts_c.append(_mix(w))
        pts_xy = np.array(pts_xy)
        axins.scatter(pts_xy[:, 0], pts_xy[:, 1], c=pts_c, s=18, edgecolors='none')

        # Labels at vertices
        axins.text(A[0] - 0.05, A[1] - 0.05, source_labels[0], fontsize=8, ha='right', va='top')
        axins.text(B[0] + 0.05, B[1] - 0.05, source_labels[1], fontsize=8, ha='left', va='top')
        axins.text(C[0], C[1] + 0.05, source_labels[2], fontsize=8, ha='center', va='bottom')
        axins.set_title("Mixture (ternary)", fontsize=9, pad=2)

    else:
        # --- >3 sources: compact sample strip ---------------------------------------
        axins = inset_axes(ax, width="35%", height="7%", loc="lower left", borderpad=1.0)
        rng = np.random.default_rng(0)  # deterministic
        m = 18  # number of swatches
        W = rng.dirichlet(np.ones(n), size=m)       # random simplex samples
        swatch = np.array([_mix(w) for w in W])     # (m, 3)
        img = np.expand_dims(swatch, axis=0)        # (1, m, 3)
        axins.imshow(img, aspect="auto")
        axins.set_yticks([])
        axins.set_xticks([])
        axins.set_title("Sample mixtures", fontsize=9, pad=2)

def plot_src_spectrum(
    ax=None,
    gdf=None,
    attribute=None,            # str (column with vectors) OR list[str] (columns to combine)
    colors=None,
    line_width=2,
    dn_col='DN',
    lw_min=0.5,
    lw_max=6.0,
    # --- Pie-chart controls ---
    plot_pies=False,
    n_pies=0,
    ratio_decimals=2,
    pie_radius_rel=0.02,         # radius as fraction of max(network width/height)
    connector_kwargs=None,        # e.g., dict(color='grey', lw=1.5, ls='--', alpha=0.8)
    pie_zorder=30,
    # --- Visibility & layout ---
    expand_limits_for_pies=True,
    force_equal_aspect=True,
    debug_pie_centers=False,
    # --- New: placement & labeling enhancements ---
    n_angle_samples=24,           # number of candidate angles for connector (e.g., 16–36)
    pie_gap_rel=0.01,             # min gap between pies (relative to bbox max dimension)
    avoid_legend=True,            # avoid placing pies where they overlap legend
    show_pie_labels=True,         # show ratio labels next to pies
    label_decimals=0,             # decimals in percentage labels
    label_color='k',
    label_fontsize=9,
    draw_mixture_scale=True,
    pie_label_inside=True,
    pie_label_r_rel=0.6,        # radial position of labels inside wedge (0..1 of radius)
    auto_contrast_labels=True,  # choose white/black text based on wedge color luminance
    min_label_pct=0.0,          # hide labels below this % if desired (0 = show all)

):
    """
    Plots the source spectrum for a district heating network with optional pie annotations.

    :param ax: Matplotlib axis object. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional

    :param gdf: Geospatial DataFrame containing the network geometries to plot. Must include a 'geometry'
                column with LineString or MultiLineString objects.
    :type gdf: geopandas.GeoDataFrame

    :param attribute: Mixture information per row. If a string, it is the name of a column whose entries are
                    vector-like mixtures (e.g., [96, 4] or [0.96, 0.04]). If a list of strings, these columns
                    are combined row-wise (in the given order) into a mixture vector. Values may be absolute
                    contributions or percentages; they are normalized internally to sum to 1. If the sum is
                    ~100, values are treated as percentages.
    :type attribute: str or list[str]

    :param colors: Base RGB colors used for color mixing and pie wedges. Each color is a 3-component RGB
                sequence in the 0–255 range (alpha optional, ignored for mixing).
    :type colors: list[numpy.ndarray] or list[Sequence[float]], length == number of sources

    :param line_width: Fallback line width applied when DN-based scaling is unavailable or invalid.
    :type line_width: float, optional

    :param dn_col: Name of the diameter (or similar) column used to scale line widths and to select
                representative pipes for pie placement.
    :type dn_col: str, optional

    :param lw_min: Minimum line width used when scaling by ``dn_col``.
    :type lw_min: float, optional

    :param lw_max: Maximum line width used when scaling by ``dn_col``.
    :type lw_max: float, optional

    :param plot_pies: If True, annotate selected unique mixture ratios with pie charts positioned outside the
                    network bounding box and connected via a line from a representative pipe.
    :type plot_pies: bool, optional

    :param n_pies: Number of pie annotations to place. For two sources: choose extremes (max per source),
                then the most balanced (closest to 50/50), then additional values spread across the spectrum.
                For more than two sources: one extreme per source, then most balanced (closest to uniform),
                then farthest-point sampling for diversity.
    :type n_pies: int, optional

    :param ratio_decimals: Rounding applied to normalized ratios for de-duplication of unique mixtures.
    :type ratio_decimals: int, optional

    :param pie_radius_rel: Pie radius as a fraction of the larger side of the network bounding box. Adjust to
                        tune visual size across differently scaled coordinate systems.
    :type pie_radius_rel: float, optional

    :param connector_kwargs: Keyword arguments passed to ``matplotlib.pyplot.plot`` for connector styling
                            (e.g., ``dict(color='grey', lw=1.2, ls='--', alpha=0.9)``).
    :type connector_kwargs: dict, optional

    :param pie_zorder: Z-order for pie wedges and their connectors.
    :type pie_zorder: int, optional

    :param expand_limits_for_pies: If True, expands the axis limits to fully include all pies (and a small
                                margin), ensuring they remain visible even when placed outside the original
                                data extent.
    :type expand_limits_for_pies: bool, optional

    :param force_equal_aspect: If True, forces equal aspect ratio so circular pies are rendered as circles.
    :type force_equal_aspect: bool, optional

    :param debug_pie_centers: If True, draws small markers at pie centers to aid debugging of placement.
    :type debug_pie_centers: bool, optional

    :param n_angle_samples: Number of candidate connector angles to test per pie. The chosen angle minimizes
                            the interior crossing distance and penalizes overlap with other pies and with the
                            legend/mix-scale area (when avoidance is enabled).
    :type n_angle_samples: int, optional

    :param pie_gap_rel: Minimum gap between pie outer circles, expressed as a fraction of the larger side of
                        the network bounding box. Helps avoid pie‑pie overlap.
    :type pie_gap_rel: float, optional

    :param avoid_legend: If True, pie placement avoids overlapping the existing legend and/or mixture scale
                        axes when possible (requires a canvas draw to measure extents).
    :type avoid_legend: bool, optional

    :param show_pie_labels: If True, draw ratio labels next to each pie. For two sources, two labels are
                            shown on opposite sides; for three or more sources, a single combined label
                            (e.g., "30/50/20%") is placed.
    :type show_pie_labels: bool, optional

    :param label_decimals: Number of decimal places to show in percentage labels.
    :type label_decimals: int, optional

    :param label_color: Text color for pie labels.
    :type label_color: str, optional

    :param label_fontsize: Font size for pie labels.
    :type label_fontsize: float, optional

    :param draw_mixture_scale: If True, draw the mixture scale (e.g., gradient/ternary inset) for the color
                            scheme. If False, suppresses this inset.
    :type draw_mixture_scale: bool, optional

    :returns: The axis used for plotting (useful for further chaining/customization).
    :rtype: matplotlib.axes.Axes

    :raises ValueError: If required parameters are missing, if the number of attribute columns does not match
                        the number of colors/sources, or if color specifications are malformed.
    :raises KeyError: If the specified ``attribute`` column(s) or ``dn_col`` are not present in ``gdf``.
    :raises TypeError: If ``attribute`` is neither a string nor a list of strings.

    .. note::
    - Mixtures are normalized to sum to 1. If the raw sum is approximately 100, values are interpreted
        as percentages. Rows with invalid/empty mixtures fallback to a neutral light-gray color.
    - DN-based width scaling maps the observed ``dn_col`` range linearly into ``[lw_min, lw_max]``. If
        ``dn_col`` has no numeric variation, a midpoint width is used.
    - Pie placement samples multiple angles and chooses the one minimizing interior travel distance while
        avoiding overlap with other pies and the legend/mixture scale (when enabled). Axes limits are expanded
        to include pies when requested.

    """
    import sys
    import logging
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from difflib import get_close_matches
    from math import cos, sin, pi, isfinite

    # --------- Logging & fallbacks ----------
    try:
        _logger = logger  # use module/global logger if present
    except NameError:
        _logger = logging.getLogger(__name__)

    def _get_figsize():
        try:
            return getattr(Rm, 'DINA3q', (12, 8))
        except NameError:
            return (12, 8)

    logStr = "{0:s}.{1:s}: ".format(__name__, sys._getframe().f_code.co_name)
    _logger.debug(f"{logStr}Start.")

    # --------- Color utilities (with fallbacks) ----------
    def _to_rgb01(c):
        c = np.array(c, dtype=float).clip(0, 255) / 255.0
        if c.size == 3:
            return (c[0], c[1], c[2], 1.0)
        if c.size == 4:
            return tuple(c)
        raise ValueError("Color must have 3 or 4 components.")

    def _convert_to_hex_local(rgb):
        r, g, b = np.array(rgb, dtype=float).clip(0, 255).astype(int).tolist()
        return f"#{r:02X}{g:02X}{b:02X}"

    def _convert_to_hex(rgb):
        func = globals().get('convert_to_hex')
        if callable(func):
            try:
                return func(np.array(rgb))
            except Exception:
                pass
        return _convert_to_hex_local(rgb)

    def _mix_colors_local(weights, base_colors):
        w = np.array(weights, dtype=float).ravel()
        C = np.array(base_colors, dtype=float)
        if w.ndim != 1 or C.ndim != 2 or C.shape[1] < 3 or len(w) != C.shape[0]:
            raise ValueError("Invalid weights/colors shapes.")
        sw = w.sum()
        if sw == 0 or not np.isfinite(sw):
            sw = 1.0
        w = w / sw
        rgb = (w[:, None] * C[:, :3]).sum(axis=0)
        return np.clip(rgb, 0, 255)

    def _mix_colors(weights, base_colors):
        func = globals().get('mix_colors')
        if callable(func):
            try:
                return func(weights, base_colors)
            except Exception:
                pass
        return _mix_colors_local(weights, base_colors)

    # --------- Ratio utilities ----------
    def _normalize_ratio(r):
        try:
            v = np.array(r, dtype=float).ravel()
        except Exception:
            return None
        s = np.nansum(v)
        if not np.isfinite(s) or s <= 0:
            return None
        if abs(s - 100.0) < 1e-3:
            v = v / 100.0
        else:
            v = v / s
        return v

    def _round_tuple(v, dec):
        return tuple(np.round(np.asarray(v, dtype=float), dec).tolist())

    def _extract_mix_series(gdf, attribute, n_sources):
        if isinstance(attribute, str):
            if attribute not in gdf.columns:
                suggestions = get_close_matches(attribute, list(map(str, gdf.columns)), n=5, cutoff=0.5)
                hint = f" Did you mean one of: {suggestions}" if suggestions else ""
                raise KeyError(f"Column '{attribute}' not found in gdf.{hint}")
            ser_raw = gdf[attribute]
            out = []
            for idx, val in ser_raw.items():
                try:
                    arr = np.asarray(val, dtype=float).ravel()
                    if arr.size != n_sources:
                        raise ValueError(
                            f"Row {idx}: vector length {arr.size} != number of sources {n_sources}."
                        )
                    arrn = _normalize_ratio(arr)
                except Exception:
                    arrn = None
                out.append(arrn)
            return pd.Series(out, index=gdf.index)
        elif isinstance(attribute, (list, tuple)) and all(isinstance(c, str) for c in attribute):
            missing = [c for c in attribute if c not in gdf.columns]
            if missing:
                raise KeyError(f"Columns not found for 'attribute': {missing}")
            if len(attribute) != n_sources:
                raise ValueError(
                    f"Number of attribute columns ({len(attribute)}) must equal number of sources ({n_sources})."
                )
            vals = gdf.loc[:, attribute].astype(float).values  # (N, M)
            sums = np.nansum(vals, axis=1)
            sums[~np.isfinite(sums) | (sums == 0)] = np.nan
            normed = vals / sums[:, None]
            out = [None if not np.isfinite(s) else normed[i, :] for i, s in enumerate(sums)]
            return pd.Series(out, index=gdf.index)
        else:
            raise TypeError("`attribute` must be a column name (str) holding vectors, or a list of column names.")

    def _get_unique_ratios(series, dec):
        uniq = {}
        for idx, v in series.items():
            if v is None:
                continue
            key = _round_tuple(v, dec)
            if key not in uniq:
                uniq[key] = []
            uniq[key].append(idx)
        return uniq  # dict: ratio_tuple -> [row indices]
    def _relative_luminance(rgb255):
        """WCAG relative luminance for contrast decisions (sRGB)."""
        r, g, b = (np.array(rgb255[:3], dtype=float) / 255.0).tolist()
        def f(u): return u/12.92 if u <= 0.03928 else ((u + 0.055)/1.055) ** 2.4
        R, G, B = f(r), f(g), f(b)
        return 0.2126*R + 0.7152*G + 0.0722*B

    def _auto_text_color(rgb255):
        """
        Choose black or white text for best contrast with a background color.
        Uses WCAG contrast ratio heuristic.
        """
        L = _relative_luminance(rgb255)
        contrast_black = (L + 0.05) / 0.05           # vs black (L=0)
        contrast_white = (1.0 + 0.05) / (L + 0.05)   # vs white (L=1)
        return 'black' if contrast_black >= contrast_white else 'white'

    def _label_inside_pie(ax, center_xy, proportions, base_colors, radius,
                        pie_label_r_rel=0.6, label_decimals=0, label_fontsize=9,
                        label_color='k', auto_contrast=True, min_label_pct=0.0,
                        start_angle_deg=90.0, zorder=10):
        """
        Place one label per wedge INSIDE the pie area at the wedge's mid-angle.
        - proportions: iterable summing to 1 (shares)
        - base_colors: same length as proportions, RGB 0-255
        - radius: pie radius in data units
        - start_angle_deg: first wedge starts at 12 o'clock by default
        """
        cx, cy = center_xy
        angle = start_angle_deg
        for p, col in zip(proportions, base_colors):
            if p <= 0:
                continue
            pct = float(p) * 100.0
            if pct < float(min_label_pct):
                angle += 360.0 * float(p)
                continue

            theta_deg = 360.0 * float(p)
            theta_mid = np.deg2rad(angle + theta_deg * 0.5)

            # label position inside the wedge
            rlab = float(pie_label_r_rel) * float(radius)
            x = cx + rlab * np.cos(theta_mid)
            y = cy + rlab * np.sin(theta_mid)

            # choose text color
            txt_color = _auto_text_color(col) if auto_contrast else label_color

            ax.text(
                x, y,
                f"{pct:.{label_decimals}f}%",
                ha='center', va='center',
                color=txt_color,
                fontsize=label_fontsize,
                zorder=zorder,
                clip_on=False,
            )

            angle += theta_deg
    # --------- Ratio selection ----------
    def _select_ratios_two_sources(unique_keys, n):
        if n <= 0 or len(unique_keys) == 0:
            return []
        arr = np.array(unique_keys)  # (U, 2)
        p0, p1 = arr[:, 0], arr[:, 1]

        if len(unique_keys) == 1:
            return [unique_keys[0]]

        chosen = []
        chosen_idxs = set()

        i_max0 = int(np.argmax(p0))  # extreme towards source 1
        i_max1 = int(np.argmax(p1))  # extreme towards source 2
        for i in [i_max0, i_max1]:
            if i not in chosen_idxs and len(chosen) < n:
                chosen.append(unique_keys[i])
                chosen_idxs.add(i)
        if len(chosen) >= n:
            return chosen[:n]

        # Most balanced (closest to 0.5/0.5)
        bal_idx = int(np.argmin(np.abs(p0 - 0.5)))
        if bal_idx not in chosen_idxs and len(chosen) < n:
            chosen.append(unique_keys[bal_idx])
            chosen_idxs.add(bal_idx)
        if len(chosen) >= n:
            return chosen[:n]

        # Fill remaining by spreading across spectrum (quantiles)
        remaining = [i for i in range(len(unique_keys)) if i not in chosen_idxs]
        if remaining:
            k_need = n - len(chosen)
            qs = np.linspace(0, 1, k_need + 2)[1:-1]  # internal quantiles
            order_all = np.argsort(p0[remaining])
            cand = [remaining[i] for i in order_all]
            for q in qs:
                target = np.quantile(p0, q)
                best, best_d = None, np.inf
                for i in cand:
                    d = abs(p0[i] - target)
                    if d < best_d:
                        best_d, best = d, i
                if best is not None:
                    chosen.append(unique_keys[best])
                    cand.remove(best)
                if len(chosen) >= n:
                    break
        return chosen[:n]

    def _select_ratios_generic(unique_keys, n):
        if n <= 0 or len(unique_keys) == 0:
            return []
        U = np.array(unique_keys)  # (U, M)
        M = U.shape[1]
        chosen_idxs = set()

        # Extremes: for each source, argmax of that component
        for m in range(M):
            idx = int(np.argmax(U[:, m]))
            chosen_idxs.add(idx)
            if len(chosen_idxs) >= n:
                return [unique_keys[i] for i in list(chosen_idxs)[:n]]

        # Most balanced: closest to uniform
        uniform = np.ones(M) / M
        bal_idx = int(np.argmin(np.linalg.norm(U - uniform, axis=1)))
        chosen_idxs.add(bal_idx)
        if len(chosen_idxs) >= n:
            return [unique_keys[i] for i in list(chosen_idxs)[:n]]

        # Farthest-point sampling for remaining
        chosen = list(chosen_idxs)
        while len(chosen) < min(n, len(unique_keys)):
            dists = np.full(U.shape[0], np.inf)
            for i in range(U.shape[0]):
                d = np.min([np.linalg.norm(U[i] - U[j]) for j in chosen])
                dists[i] = d
            next_idx = int(np.argmax(dists))
            if next_idx in chosen:
                break
            chosen.append(next_idx)
        return [unique_keys[i] for i in chosen[:n]]

    def _find_idx_for_ratio(lookup, ratio_key, dn_series):
        idxs = lookup.get(ratio_key, [])
        if not idxs:
            return None
        if dn_series is not None:
            dns = pd.to_numeric(dn_series.loc[idxs], errors='coerce')
            if dns.notna().any():
                return dns.idxmax()
        return idxs[0]

    # --------- Geometry helpers for placement ----------
    def _ray_rect_intersection(cx, cy, dx, dy, rect):
        """
        Intersect a ray from (cx,cy) in direction (dx,dy) with axis-aligned rectangle.
        Returns (x, y, t) where t>0 and (cx+ t*dx, cy+ t*dy) lies on the rectangle boundary.
        Returns (None, None, None) if no valid intersection (shouldn't happen for finite dx,dy).
        """
        minx, miny, maxx, maxy = rect
        ts = []
        # vertical sides
        if dx > 0:
            t = (maxx - cx) / dx
            y = cy + t * dy
            if t > 0 and miny - 1e-9 <= y <= maxy + 1e-9:
                ts.append((t, maxx, y))
        elif dx < 0:
            t = (minx - cx) / dx
            y = cy + t * dy
            if t > 0 and miny - 1e-9 <= y <= maxy + 1e-9:
                ts.append((t, minx, y))
        # horizontal sides
        if dy > 0:
            t = (maxy - cy) / dy
            x = cx + t * dx
            if t > 0 and minx - 1e-9 <= x <= maxx + 1e-9:
                ts.append((t, x, maxy))
        elif dy < 0:
            t = (miny - cy) / dy
            x = cx + t * dx
            if t > 0 and minx - 1e-9 <= x <= maxx + 1e-9:
                ts.append((t, x, miny))
        if not ts:
            return None, None, None
        tmin, xhit, yhit = min(ts, key=lambda z: z[0])
        return xhit, yhit, tmin

    def _expand_rect(rect, pad):
        minx, miny, maxx, maxy = rect
        return (minx - pad, miny - pad, maxx + pad, maxy + pad)

    def _rect_overlap(a, b):
        ax0, ay0, ax1, ay1 = a
        bx0, by0, bx1, by1 = b
        return not (ax1 < bx0 or bx1 < ax0 or ay1 < by0 or by1 < ay0)

    def _draw_pie(ax, center_xy, proportions, base_colors, radius,
                  zorder=10, edgecolor='white', linewidth=0.5,
                  clip_on=False):
        """Draw a pie at data coordinates using Wedge patches."""
        x0, y0 = center_xy
        start_angle = 90.0  # 12 o'clock
        for p, col in zip(proportions, base_colors):
            if p <= 0:
                continue
            theta = 360.0 * float(p)
            wedge = mpatches.Wedge(center=(x0, y0),
                                   r=radius,
                                   theta1=start_angle,
                                   theta2=start_angle + theta,
                                   facecolor=_to_rgb01(col),
                                   edgecolor=edgecolor,
                                   linewidth=linewidth,
                                   zorder=zorder,
                                   clip_on=clip_on)
            ax.add_patch(wedge)
            start_angle += theta

    def _label_two_sources(ax, ex, ey, theta, r, pcts, **kw):
        """
        Place two labels on opposite sides of the pie, perpendicular to connector direction.
        pcts: (p0, p1) in percent.
        """
        nx, ny = -sin(theta), cos(theta)  # normal vector (unit)
        offset = 0.6 * r
        posA = (ex - (r + offset) * nx, ey - (r + offset) * ny)
        posB = (ex + (r + offset) * nx, ey + (r + offset) * ny)

        def _ha_va(dx, dy):
            # choose alignment based on vector direction for better anchoring
            ha = 'left' if dx > 0 else 'right' if dx < 0 else 'center'
            va = 'bottom' if dy > 0 else 'top' if dy < 0 else 'center'
            # if mostly horizontal, center vertically
            if abs(dx) > abs(dy):
                va = 'center'
            else:
                ha = 'center'
            return ha, va

        haA, vaA = _ha_va(-nx, -ny)
        haB, vaB = _ha_va(nx, ny)

        ax.text(*posA, f"{pcts[0]:.{label_decimals}f}%", ha=haA, va=vaA, **kw)
        ax.text(*posB, f"{pcts[1]:.{label_decimals}f}%", ha=haB, va=vaB, **kw)

    def _label_multi_sources(ax, ex, ey, theta, r, pcts, **kw):
        """
        Place one combined label offset perpendicular to the connector.
        pcts: sequence of percents.
        """
        nx, ny = -sin(theta), cos(theta)
        offset = 0.7 * r
        pos = (ex + (r + offset) * nx, ey + (r + offset) * ny)
        s = "/".join([f"{p:.{label_decimals}f}%" for p in pcts])
        ha = 'center'
        va = 'center'
        ax.text(*pos, s, ha=ha, va=va, **kw)

    try:
        # --- Axis ---
        if ax is None:
            fig, ax = plt.subplots(figsize=_get_figsize())
            _logger.debug(f"{logStr}Created new axis.")

        if gdf is None or gdf.empty:
            _logger.debug(f"{logStr}No plot data provided.")
            return ax

        if attribute is None or colors is None:
            raise ValueError("Both 'attribute' and 'colors' must be provided.")
        n_sources = len(colors)

        # --- Build normalized mixture series (vector per row) ---
        mix_ser = _extract_mix_series(gdf, attribute, n_sources)  # Series of arrays or None

        # For color mixing, use a safe fallback color if a row has no valid vector
        def _safe_mix(v):
            vn = _normalize_ratio(v) if v is not None else None
            if vn is None or len(vn) != n_sources:
                return np.array([200, 200, 200])  # light gray fallback
            return _mix_colors(vn, colors)

        gdf = gdf.copy()  # avoid mutating original
        gdf['mixed_color'] = mix_ser.apply(_safe_mix)
        gdf['mixed_color_hex'] = gdf['mixed_color'].apply(
            lambda x: _convert_to_hex(np.array(x).clip(0, 255))
        )

        # --- Validate linewidth bounds ---
        try:
            lw_min_val = float(lw_min)
            lw_max_val = float(lw_max)
        except Exception:
            _logger.warning(f"{logStr}Invalid lw_min/lw_max; falling back to defaults.")
            lw_min_val, lw_max_val = 0.5, 6.0

        if lw_min_val <= 0:
            _logger.warning(f"{logStr}lw_min <= 0; clamping to 0.1.")
            lw_min_val = 0.1
        if lw_max_val <= 0:
            _logger.warning(f"{logStr}lw_max <= 0; clamping to 0.2.")
            lw_max_val = 0.2
        if lw_min_val > lw_max_val:
            _logger.warning(f"{logStr}lw_min > lw_max; swapping values.")
            lw_min_val, lw_max_val = lw_max_val, lw_min_val

        # --- DN-based linewidths (fallback to constant) ---
        widths = None
        if dn_col in gdf.columns:
            dn_series = pd.to_numeric(gdf[dn_col], errors='coerce')
            valid = dn_series.dropna()
            if not valid.empty:
                dn_min, dn_max = valid.min(), valid.max()
                if dn_max > dn_min:
                    widths = np.interp(dn_series.fillna(dn_min),
                                       (dn_min, dn_max), (lw_min_val, lw_max_val))
                    _logger.debug(f"{logStr}Line widths scaled by '{dn_col}' in range "
                                  f"[{lw_min_val}, {lw_max_val}]. DN range: [{dn_min}, {dn_max}]")
                else:
                    mid = 0.5 * (lw_min_val + lw_max_val)
                    widths = np.full(len(gdf), mid)
                    _logger.debug(f"{logStr}'{dn_col}' has no variation; using mid width {mid}.")
            else:
                _logger.warning(f"{logStr}'{dn_col}' exists but contains no numeric values; using fixed line_width.")
        else:
            _logger.debug(f"{logStr}'{dn_col}' not found; using fixed line_width.")

        if widths is None:
            widths = np.full(len(gdf), float(line_width))

        # --- Plot the network (lines) ---
        for (idx, row), lw in zip(gdf.iterrows(), widths):
            geom = row['geometry']
            color = row['mixed_color_hex']
            try:
                if geom.geom_type == 'LineString':
                    x, y = geom.xy
                    ax.plot(x, y, color=color, linewidth=lw)
                elif geom.geom_type == 'MultiLineString':
                    for part in geom.geoms:
                        x, y = part.xy
                        ax.plot(x, y, color=color, linewidth=lw)
                else:
                    _logger.debug(f"{logStr}Unsupported geometry '{geom.geom_type}' at index {idx}; skipped.")
            except Exception as e:
                _logger.debug(f"{logStr}Failed plotting index {idx}: {e}")

        # --- Legend for source colors ---
        legend_handles = []
        for i, color in enumerate(colors):
            color_hex = _convert_to_hex(np.array(color).clip(0, 255))
            legend_handles.append(
                plt.Line2D([0], [0], color=color_hex, lw=max(1.0, lw_min_val), label=f"Source {i+1}")
            )
        ax.legend(handles=legend_handles, loc='best')

        # --- Mixture scale inset (if available) ---
        if draw_mixture_scale:
            try:
                _add_mixture_scale  # noqa
                try:
                    _add_mixture_scale(ax, colors)
                except Exception as e:
                    _logger.debug(f"{logStr}_add_mixture_scale failed: {e}")
            except NameError:
                pass  # silently skip if not available
        else:
            pass

        ax.set_axis_off()

        # --- Pie chart annotations (optional) ---
        if plot_pies and n_pies > 0:
            _logger.debug(f"{logStr}Pie annotations requested: n_pies={n_pies}")

            # Unique normalized ratios (rounded) with index lists
            ratio_map = _get_unique_ratios(mix_ser, ratio_decimals)
            unique_ratio_keys = list(ratio_map.keys())
            if len(unique_ratio_keys) == 0:
                _logger.warning(f"{logStr}No valid ratios found for pie selection.")
                return ax

            # Select which ratios to annotate
            if n_sources == 2:
                chosen_ratios = _select_ratios_two_sources(unique_ratio_keys, n_pies)
            else:
                chosen_ratios = _select_ratios_generic(unique_ratio_keys, n_pies)

            if not chosen_ratios:
                _logger.warning(f"{logStr}No ratios selected for pies.")
                return ax

            # Layout: pies outside bbox
            minx, miny, maxx, maxy = gdf.total_bounds
            max_dim = max(maxx - minx, maxy - miny)
            margin = 0.04 * max_dim
            pie_radius = float(pie_radius_rel) * max_dim
            pie_gap = float(pie_gap_rel) * max_dim

            dn_series_for_rep = gdf[dn_col] if dn_col in gdf.columns else None
            if connector_kwargs is None:
                _ckw = dict(color='grey', lw=1.2, ls='--', alpha=0.9)
            else:
                _ckw = dict(color='grey', lw=1.2, ls='--', alpha=0.9)
                _ckw.update(dict(connector_kwargs))

            base_colors = [np.array(c, dtype=float) for c in colors]
            placed_pies = []   # list of dicts: {'center':(ex,ey), 'bbox':(x0,y0,x1,y1), 'theta':theta}
            pie_boxes = []     # for axis expansion

            # Legend bbox in data coords (optional avoidance)
            legend_rect_data = None
            if avoid_legend:
                # force a draw so legend has a window extent
                try:
                    ax.figure.canvas.draw()
                    leg = ax.get_legend()
                    if leg is not None:
                        renderer = ax.figure.canvas.get_renderer()
                        wb = leg.get_window_extent(renderer=renderer)
                        # transform display -> data coords
                        inv = ax.transData.inverted()
                        (x0, y0) = inv.transform((wb.x0, wb.y0))
                        (x1, y1) = inv.transform((wb.x1, wb.y1))
                        legend_rect_data = (min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))
                except Exception:
                    legend_rect_data = None

            inner_rect = (minx, miny, maxx, maxy)
            outer_rect = _expand_rect(inner_rect, margin + pie_radius + pie_gap)

            # Precompute candidate angles
            angles = np.linspace(0, 2 * pi, max(4, int(n_angle_samples)), endpoint=False)

            for rkey in chosen_ratios:
                rep_idx = _find_idx_for_ratio(ratio_map, rkey, dn_series_for_rep)
                if rep_idx is None:
                    continue

                geom = gdf.at[rep_idx, 'geometry']
                try:
                    cpt = geom.centroid
                    cx, cy = float(cpt.x), float(cpt.y)
                except Exception:
                    continue

                # Choose best angle by minimizing a cost function:
                # cost = inside_exit_distance + penalties (pie overlap, legend overlap)
                best = None  # (cost, ex, ey, theta)
                for theta in angles:
                    dx, dy = cos(theta), sin(theta)

                    # where ray exits inner rect (distance inside network)
                    _, _, t_exit_inner = _ray_rect_intersection(cx, cy, dx, dy, inner_rect)
                    if t_exit_inner is None:
                        continue
                    # where ray hits outer rect (pie center location)
                    ex, ey, t_outer = _ray_rect_intersection(cx, cy, dx, dy, outer_rect)
                    if t_outer is None:
                        continue

                    # candidate pie bbox
                    pb = (ex - pie_radius, ey - pie_radius, ex + pie_radius, ey + pie_radius)

                    # overlap penalty with already placed pies
                    penalty = 0.0
                    for pp in placed_pies:
                        (px, py) = pp['center']
                        d2 = (ex - px) ** 2 + (ey - py) ** 2
                        min_sep = (pie_radius + pie_radius + pie_gap)
                        if d2 < (min_sep ** 2):
                            # quadratic penalty as overlap severity grows
                            penalty += 1e6 * (min_sep ** 2 - d2)

                    # penalty for overlapping legend
                    if legend_rect_data is not None and _rect_overlap(pb, legend_rect_data):
                        penalty += 1e8

                    cost = t_exit_inner + penalty  # prefer short exit; avoid overlaps

                    if (best is None) or (cost < best[0]):
                        best = (cost, ex, ey, theta)

                if best is None:
                    # fallback to nearest side (original)
                    # choose nearest side endpoint axis-aligned
                    d_left, d_right = cx - minx, maxx - cx
                    d_bottom, d_top = cy - miny, maxy - cy
                    side = np.argmin([d_left, d_right, d_bottom, d_top])
                    if side == 0:
                        theta = pi  # left
                    elif side == 1:
                        theta = 0.0  # right
                    elif side == 2:
                        theta = -pi/2  # down
                    else:
                        theta = pi/2   # up
                    dx, dy = cos(theta), sin(theta)
                    ex, ey, _ = _ray_rect_intersection(cx, cy, dx, dy, outer_rect)
                else:
                    _, ex, ey, theta = (best[0], best[1], best[2], best[3])

                # record and draw
                pb = (ex - pie_radius, ey - pie_radius, ex + pie_radius, ey + pie_radius)
                placed_pies.append({'center': (ex, ey), 'bbox': pb, 'theta': theta})
                pie_boxes.append(pb)

                # connector (no clipping)
                ax.plot([cx, ex], [cy, ey], zorder=pie_zorder, clip_on=False, **_ckw)

                if debug_pie_centers:
                    ax.scatter([ex], [ey], s=30, color='k', zorder=pie_zorder+1, clip_on=False)

                # pie (no clipping)
                _draw_pie(ax, (ex, ey), rkey, base_colors, pie_radius,
                          zorder=pie_zorder, edgecolor='white', linewidth=0.6, clip_on=False)

                # labels
                if show_pie_labels and pie_label_inside:
                    _label_inside_pie(
                        ax, (ex, ey), rkey, base_colors, pie_radius,
                        pie_label_r_rel=pie_label_r_rel,
                        label_decimals=label_decimals,
                        label_fontsize=label_fontsize,
                        label_color=label_color,
                        auto_contrast=auto_contrast_labels,
                        min_label_pct=min_label_pct,
                        start_angle_deg=90.0,
                        zorder=pie_zorder + 2,
                    )


            # Expand axis limits so pies are visible
            if expand_limits_for_pies and pie_boxes:
                pxmin = min(b[0] for b in pie_boxes)
                pymin = min(b[1] for b in pie_boxes)
                pxmax = max(b[2] for b in pie_boxes)
                pymax = max(b[3] for b in pie_boxes)
                gap = 0.02 * max_dim  # small extra gap

                new_xmin = min(minx, pxmin) - gap
                new_xmax = max(maxx, pxmax) + gap
                new_ymin = min(miny, pymin) - gap
                new_ymax = max(maxy, pymax) + gap

                ax.set_xlim(new_xmin, new_xmax)
                ax.set_ylim(new_ymin, new_ymax)

            if force_equal_aspect:
                ax.set_aspect('equal', adjustable='datalim')

            _logger.debug(f"{logStr}Pie annotations complete.")

        return ax

    except Exception as e:
        _logger.error(f"{logStr}Error. - {e}")


def plot_ttr_network(
    df: pd.DataFrame,
    dn_col: str = "DN",
    geometry_col: str = "geometry",
    fk_ki_col: str = "fkKI",
    fk_kk_col: str = "fkKK",
    cmap: str = "viridis",
    node_size: float = 25.0,
    linewidth_range: tuple[float, float] = (0.6, 5.0),
    annotate: bool = False,
    annotation_fmt: str = "{:.1f}",
    ttr_label: str = "TTR [h]",
    agg: str = "max",
    ax: plt.Axes | None = None,
    colorbar: bool = True,
    show_values: bool = False,
    dt_col: str | None = None,
    show_edge_dt: bool = False,
    # --- TTR scaling controls ---
    ttr_norm: str = "data",                 # 'data' | 'clip' | 'percentile'
    ttr_vmin: float | None = None,          # used if ttr_norm='clip'
    ttr_vmax: float | None = None,
    ttr_percentiles: tuple[float, float] = (2.0, 98.0),
    # --- Highlight controls ---
    highlight_keys: list | tuple | set | None = None,
    highlight_marker_size: float = 140.0,
    # Matching strategy:
    #   'auto'   -> numeric if fk cols numeric; else string-normalized
    #   'both'   -> union of direct OR string OR numeric (most forgiving)
    #   'numeric'-> numeric-only match
    #   'string' -> string-normalized-only match
    highlight_match: str = "auto",
):
    """
    Plots a district heating network with edges from geometry and nodes colored by TTR values.

    :param df: The DataFrame containing edge and node attributes.
    :type df: pandas.DataFrame
    :param dn_col: Column name for pipe diameter used to scale edge linewidth.
    :type dn_col: str, optional, default="DN"
    :param geometry_col: Column name containing WKT or shapely geometries for edges.
    :type geometry_col: str, optional, default="geometry"
    :param fk_ki_col: Column name for the foreign key of the start node (KI).
    :type fk_ki_col: str, optional, default="fkKI"
    :param fk_kk_col: Column name for the foreign key of the end node (KK).
    :type fk_kk_col: str, optional, default="fkKK"
    :param cmap: Colormap for node coloring based on TTR values.
    :type cmap: str, optional, default="viridis"
    :param node_size: Size of the node markers.
    :type node_size: float, optional, default=25.0
    :param linewidth_range: Minimum and maximum linewidth for edges scaled by DN.
    :type linewidth_range: tuple of float, optional, default=(0.6, 5.0)
    :param annotate: Whether to annotate nodes with their TTR values.
    :type annotate: bool, optional, default=False
    :param annotation_fmt: Format string for TTR annotations.
    :type annotation_fmt: str, optional, default="{:.1f}"
    :param ttr_label: Label for the colorbar representing TTR values.
    :type ttr_label: str, optional, default="TTR"
    :param agg: Aggregation method for TTR when multiple edges share a node coordinate.
    :type agg: str, optional, default="max"
    :param ax: The axis to plot on. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional
    :param colorbar: Whether to display a colorbar for TTR values.
    :type colorbar: bool, optional, default=True
    :param show_values: Whether to display TTR values next to each node
    :type show_values: bool, optional, default=False
    :param dt_col: Column name containing the edge travel time to display (e.g., 'dt' or 'dt_new'). If None or missing, no edge labels are drawn.
    :type dt_col: str, optional
    :param show_edge_dt: If True, draw a black text label with the edge's dt value near the edge midpoint.
    :type show_edge_dt: bool, optional, default=False
    :param ttr_norm: Method for TTR normalization: 'data', 'clip', or 'percentile'.
    :type ttr_norm: str, optional, default="data"
    :param ttr_vmin: Minimum TTR value for color scaling (used if ttr_norm='clip').
    :type ttr_vmin: float, optional
    :param ttr_vmax: Maximum TTR value for color scaling (used if ttr_norm='clip').
    :type ttr_vmax: float, optional
    :param ttr_percentiles: Percentiles for TTR normalization when ttr_norm='percentile'.
    :type ttr_percentiles: tuple of float, optional, default=(2.0, 98.0)
    :param highlight_keys: List of node keys to highlight (matches fkKI or fkKK).
    :type highlight_keys: list, tuple, or set, optional
    :param highlight_marker_size: Size of the highlight star markers.
    :type highlight_marker_size: float, optional, default=140.0
    :param highlight_match: Strategy for matching highlight keys: 'auto', 'both', 'numeric', or 'string'.
    :type highlight_match: str, optional, default="auto"

    :return: A tuple containing:
        - ax: The matplotlib axis with the plot.
        - nodes_df: DataFrame of plotted nodes with columns ['x', 'y', 'TTR'].
    :rtype: tuple(matplotlib.axes.Axes, pandas.DataFrame)
    """

    # ---- Validate columns
    required = [
        "XKOR_KI","YKOR_KI","XKOR_KK","YKOR_KK",
        "TTR_KI","TTR_KK","KVR_KI","KVR_KK",
        fk_ki_col, fk_kk_col
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # ---- Axes
    created_fig = False
    if ax is None:
        fig, ax = plt.subplots(figsize=Rm.DINA3q)
        created_fig = True

    # ---- DN -> linewidth mapping (per-edge)
    lw_min, lw_max = linewidth_range
    if dn_col in df.columns:
        dnf = pd.to_numeric(df[dn_col], errors="coerce").to_numpy()
        finite = np.isfinite(dnf)
        if finite.any():
            dn_min = float(np.nanmin(dnf[finite]))
            dn_max = float(np.nanmax(dnf[finite]))
            spread = dn_max - dn_min
            if spread > 0:
                dn_norm = (dnf - dn_min) / spread
                dn_norm = np.clip(dn_norm, 0, 1)
                row_widths = lw_min + dn_norm * (lw_max - lw_min)
            else:
                row_widths = np.full(len(dnf), 0.5 * (lw_min + lw_max))
        else:
            row_widths = np.full(len(df), lw_min)
    else:
        row_widths = np.full(len(df), lw_min)

    # ---- Geometry parsing helpers
    def _parse_coords_str(coord_str: str):
        # Parse "x y, x y, x y" (ignore optional Z)
        pts = []
        for pair in coord_str.split(","):
            parts = pair.strip().split()
            if len(parts) >= 2:
                try:
                    x = float(parts[0]); y = float(parts[1])
                    pts.append((x, y))
                except ValueError:
                    continue
        return pts

    def _parse_linestring_wkt(wkt: str):
        left = wkt.find("("); right = wkt.rfind(")")
        if left == -1 or right == -1 or right <= left:
            return []
        inner = wkt[left+1:right]
        return _parse_coords_str(inner)

    def _parse_multilinestring_wkt(wkt: str):
        start = wkt.find("(("); end = wkt.rfind("))")
        if start == -1 or end == -1 or end <= start:
            return []
        inner = wkt[start+2:end]
        polylines = []
        for part in inner.split("),"):
            part = part.strip()
            if part.startswith("("): part = part[1:]
            if part.endswith(")"): part = part[:-1]
            pts = _parse_coords_str(part)
            if len(pts) >= 2:
                polylines.append(pts)
        return polylines

    def _geometry_to_polylines(g):
        """
        Returns list of polylines (each: list[(x,y)] len>=2).
        Accepts shapely LineString/MultiLineString or WKT string.
        """
        if g is None or (isinstance(g, float) and np.isnan(g)):
            return []
        # Shapely-like geometry (duck typing)
        if hasattr(g, "geom_type"):
            gt = getattr(g, "geom_type", "")
            try:
                if gt == "LineString":
                    coords = list(g.coords)
                    return [coords] if len(coords) >= 2 else []
                elif gt == "MultiLineString":
                    pls = []
                    for ls in getattr(g, "geoms", []):
                        coords = list(ls.coords)
                        if len(coords) >= 2:
                            pls.append(coords)
                    return pls
            except Exception:
                pass
        # WKT
        if isinstance(g, str):
            s = g.strip().upper()
            if s.startswith("LINESTRING"):
                pts = _parse_linestring_wkt(g)
                return [pts] if len(pts) >= 2 else []
            if s.startswith("MULTILINESTRING"):
                return _parse_multilinestring_wkt(g)
        return []

    # ---- Build edge segments + per-segment widths
    segments = []
    seg_widths = []
    for pos, (_, row) in enumerate(df.iterrows()):
        this_w = float(row_widths[pos])
        polylines = _geometry_to_polylines(row.get(geometry_col))
        if not polylines:
            # Fallback to straight KI→KK
            try:
                x0, y0 = float(row["XKOR_KI"]), float(row["YKOR_KI"])
                x1, y1 = float(row["XKOR_KK"]), float(row["YKOR_KK"])
                segments.append(np.array([(x0, y0), (x1, y1)], dtype=float))
                seg_widths.append(this_w)
            except Exception:
                continue
        else:
            for pts in polylines:
                arr = np.array(pts, dtype=float)
                if arr.shape[0] >= 2:
                    segments.append(arr)
                    seg_widths.append(this_w)

    if segments:
        lc = LineCollection(
            segments,
            colors=(0.8, 0.8, 0.8, 1.0),   # light grey
            linewidths=seg_widths,
            zorder=1,
            capstyle="round",
            joinstyle="round",
        )
        ax.add_collection(lc)
        
        # --- Edge labels (dt) ---
        if show_edge_dt and (dt_col is not None) and (dt_col in df.columns):
            def _polyline_midpoint_xy(pts):
                """
                Compute true geometric midpoint of a polyline (list of (x,y)).
                Returns (xm, ym) or (None, None) if length is zero.
                """
                arr = np.asarray(pts, dtype=float)
                if arr.shape[0] < 2:
                    return (None, None)
                seg_vecs = np.diff(arr, axis=0)
                seg_len = np.hypot(seg_vecs[:, 0], seg_vecs[:, 1])
                total = float(seg_len.sum())
                if total == 0.0:
                    return (None, None)
                half = 0.5 * total
                cum = np.cumsum(seg_len)
                # Find the segment where the half-length falls
                j = int(np.searchsorted(cum, half))
                prev_cum = 0.0 if j == 0 else float(cum[j-1])
                remain = half - prev_cum
                # Interpolate along segment j
                p0 = arr[j]
                p1 = arr[j+1]
                seg_d = float(seg_len[j]) if seg_len[j] > 0 else 1.0
                t = remain / seg_d
                xm = p0[0] + t * (p1[0] - p0[0])
                ym = p0[1] + t * (p1[1] - p0[1])
                return (xm, ym)

            for _, row in df.iterrows():
                # 1) Skip missing / non-finite dt values
                val = abs(row[dt_col])/3600
                try:
                    if pd.isna(val):
                        continue
                except Exception:
                    continue

                # 2) Try geometry-based midpoint
                x_lab = y_lab = None
                try:
                    polylines = _geometry_to_polylines(row.get(geometry_col))
                except Exception:
                    polylines = None

                if polylines:
                    # Choose the longest polyline (stable for MULTILINESTRING)
                    def _pl_len(pl):
                        a = np.asarray(pl, dtype=float)
                        if a.shape[0] < 2:
                            return 0.0
                        v = np.diff(a, axis=0)
                        return float(np.hypot(v[:, 0], v[:, 1]).sum())

                    best_pl = max(polylines, key=_pl_len)
                    x_lab, y_lab = _polyline_midpoint_xy(best_pl)

                # 3) Fallback: midpoint of KI–KK coords if geometry missing/degenerate
                if (x_lab is None) or (y_lab is None):
                    # use standard column names ONLY if present
                    if {"XKOR_KI","YKOR_KI","XKOR_KK","YKOR_KK"}.issubset(df.columns):
                        try:
                            x0, y0 = float(row["XKOR_KI"]), float(row["YKOR_KI"])
                            x1, y1 = float(row["XKOR_KK"]), float(row["YKOR_KK"])
                            x_lab, y_lab = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
                        except Exception:
                            x_lab = y_lab = None

                # 4) Draw the label if we found a position
                if (x_lab is not None) and (y_lab is not None):
                    ax.text(
                        x_lab, y_lab,
                        annotation_fmt.format(val) + " h",
                        color="black",
                        fontsize=8,
                        ha="center", va="center",
                        zorder=4,
                        # Optional white halo for readability (uncomment the next 3 lines):
                        # path_effects=[
                        #     matplotlib.patheffects.withStroke(linewidth=2.5, foreground="white")
                        # ]
                    )
            
    # ---- Build nodes (KVR==1) and aggregate TTR at same (x,y)
    nodes_ki = (df[["XKOR_KI", "YKOR_KI", "TTR_KI", "KVR_KI"]]
                .rename(columns={"XKOR_KI":"x","YKOR_KI":"y","TTR_KI":"TTR","KVR_KI":"KVR"}))
    nodes_kk = (df[["XKOR_KK", "YKOR_KK", "TTR_KK", "KVR_KK"]]
                .rename(columns={"XKOR_KK":"x","YKOR_KK":"y","TTR_KK":"TTR","KVR_KK":"KVR"}))
    nodes = pd.concat([nodes_ki, nodes_kk], ignore_index=True)
    nodes = nodes[nodes["KVR"] == 1]
    nodes = nodes.dropna(subset=["x", "y", "TTR"])

    if nodes.empty:
        nodes_df = pd.DataFrame(columns=["x", "y", "TTR"])
    else:
        if agg not in {"max", "min", "mean", "median", "first", "last"}:
            raise ValueError("agg must be one of: 'max','min','mean','median','first','last'")
        nodes_df = nodes.groupby(["x", "y"], as_index=False).agg(TTR=("TTR", agg))

    # ---- TTR normalization (data / clip / percentile)
    if nodes_df.empty:
        vmin, vmax = 0.0, 1.0
    else:
        ttr_vals = nodes_df["TTR"].to_numpy(dtype=float)
        if ttr_norm == "percentile":
            low, high = ttr_percentiles
            vmin = float(np.nanpercentile(ttr_vals, low))
            vmax = float(np.nanpercentile(ttr_vals, high))
        elif ttr_norm == "clip":
            data_min = float(np.nanmin(ttr_vals))
            data_max = float(np.nanmax(ttr_vals))
            vmin = data_min if ttr_vmin is None else float(ttr_vmin)
            vmax = data_max if ttr_vmax is None else float(ttr_vmax)
        else:  # 'data'
            vmin = float(np.nanmin(ttr_vals))
            vmax = float(np.nanmax(ttr_vals))
        if not np.isfinite(vmin) or not np.isfinite(vmax):
            vmin, vmax = 0.0, 1.0
        if vmin == vmax:
            vmin -= 0.5; vmax += 0.5
    norm = Normalize(vmin=vmin, vmax=vmax)

    # ---- Scatter base nodes colored by TTR
    if not nodes_df.empty:
        sc = ax.scatter(
            nodes_df["x"], nodes_df["y"],
            c=nodes_df["TTR"], cmap=cmap, norm=norm,
            s=node_size,
            edgecolors="k", linewidths=0.25,
            zorder=2
        )
        if colorbar:
            cbar = plt.colorbar(sc, ax=ax, shrink=0.85)
            cbar.set_label(ttr_label)
    
        if show_values:
            for _, r in nodes_df.iterrows():
                ax.annotate(
                    annotation_fmt.format(r["TTR"] if "TTR" in r else r["TT"]) + "h",
                    xy=(r["x"], r["y"]),
                    xytext=(3, 3),
                    textcoords="offset points",
                    fontsize=8,
                    color="black",
                    zorder=3,
                )

    # ---- Highlighted nodes (always visible, no KVR/TTR requirement)
    if highlight_keys:
        # Normalize keys to plain Python scalars
        keys_list = []
        for k in list(highlight_keys):
            try:
                keys_list.append(k.item() if hasattr(k, "item") else k)
            except Exception:
                keys_list.append(k)

        # Build boolean selections under different strategies
        sel_ki_direct = df[fk_ki_col].isin(keys_list)
        sel_kk_direct = df[fk_kk_col].isin(keys_list)

        norm_str = lambda s: s.astype(str).str.strip().str.casefold()
        keys_str = pd.Series(keys_list, dtype="object").astype(str).str.strip().str.casefold()
        sel_ki_str = norm_str(df[fk_ki_col]).isin(keys_str)
        sel_kk_str = norm_str(df[fk_kk_col]).isin(keys_str)

        ki_num = pd.to_numeric(df[fk_ki_col], errors="coerce")
        kk_num = pd.to_numeric(df[fk_kk_col], errors="coerce")
        keys_num = pd.to_numeric(pd.Series(keys_list), errors="coerce")
        sel_ki_num = ki_num.isin(keys_num)
        sel_kk_num = kk_num.isin(keys_num)

        # Choose mode
        if highlight_match == "numeric":
            sel_ki = sel_ki_num
            sel_kk = sel_kk_num
        elif highlight_match == "string":
            sel_ki = sel_ki_str
            sel_kk = sel_kk_str
        elif highlight_match == "both":
            sel_ki = sel_ki_direct | sel_ki_str | sel_ki_num
            sel_kk = sel_kk_direct | sel_kk_str | sel_kk_num
        else:  # 'auto'
            ki_is_num = pd.api.types.is_numeric_dtype(df[fk_ki_col])
            kk_is_num = pd.api.types.is_numeric_dtype(df[fk_kk_col])
            if ki_is_num and kk_is_num:
                sel_ki = sel_ki_num
                sel_kk = sel_kk_num
            else:
                sel_ki = sel_ki_str
                sel_kk = sel_kk_str

        stars_ki = df.loc[sel_ki, ["XKOR_KI", "YKOR_KI"]].rename(columns={"XKOR_KI":"x","YKOR_KI":"y"})
        stars_kk = df.loc[sel_kk, ["XKOR_KK", "YKOR_KK"]].rename(columns={"XKOR_KK":"x","YKOR_KK":"y"})
        stars = pd.concat([stars_ki, stars_kk], ignore_index=True)
        stars = stars.dropna(subset=["x", "y"]).drop_duplicates()

        if not stars.empty:
            ax.scatter(
                stars["x"], stars["y"],
                marker="*",
                s=highlight_marker_size,
                facecolor="white",
                edgecolor="black",
                linewidths=0.9,
                zorder=10,
                label="Sources"
            )
            ax.legend(loc="best", frameon=True)

    # ---- Final touches
    ax.set_aspect("equal", adjustable="datalim")
    ax.autoscale_view()
    ax.set_title("Fluid age TTR[h]")
    ax.axis("off")

    if nodes_df.empty and created_fig:
        ax.set_title("No nodes with KVR == 1 and non-null TTR to plot (edges still shown).")

    return ax, nodes_df

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize


def plot_travel_time_from_source(
    df: pd.DataFrame,
    TMat: np.ndarray,
    map_nodes_tk_ind: dict,
    source,
    # Column names
    geometry_col: str = "geometry",
    tki_col: str = "tki",
    tkk_col: str = "tkk",
    xki_col: str = "XKOR_KI",
    yki_col: str = "YKOR_KI",
    xkk_col: str = "XKOR_KK",
    ykk_col: str = "YKOR_KK",
    kvri_col: str = "KVR_KI",
    kvrk_col: str = "KVR_KK",
    dn_col: str = "DN",
    # Styling (kept consistent with previous function)
    cmap: str = "viridis",
    node_size: float = 25.0,
    linewidth_range: tuple[float, float] = (0.6, 5.0),
    annotate: bool = False,
    annotation_fmt: str = "{:.1f}",
    agg: str = "max",
    show_values: bool = False,
    dt_col: str | None = None,
    show_edge_dt: bool = False,
    # Normalization (same API names as before)
    ttr_norm: str = "data",                 # 'data' | 'clip' | 'percentile'
    ttr_vmin: float | None = None,
    ttr_vmax: float | None = None,
    ttr_percentiles: tuple[float, float] = (2.0, 98.0),
    # Unreachable handling
    treat_zero_as_unreachable: bool = True, # 0 -> NaN (hidden), except source which stays 0.0
    # Highlights
    highlight_keys: list | tuple | set | None = None,
    highlight_match: str = "auto",          # 'auto' | 'both' | 'numeric' | 'string'
    highlight_marker_size: float = 140.0,
    # Matplotlib
    ax: plt.Axes | None = None,
    colorbar: bool = True,
    colorbar_label: str = "Travel time [h]",
    show_axis: bool = True,
):
    """
    Plots travel time from a selected source node using a travel-time matrix and edge geometry.

    :param df: The DataFrame describing edges and endpoints (KI/KK).
    :type df: pandas.DataFrame
    :param TMat: Square matrix with travel times; TMat[to_index, from_index] = time (hours).
    :type TMat: numpy.ndarray
    :param map_nodes_tk_ind: Mapping from node key (tk/tki/tkk values) to matrix index (0..N-1).
    :type map_nodes_tk_ind: dict
    :param source: The selected source node; either a tk key (present in map_nodes_tk_ind) or an integer matrix index.
    :type source: str | int
    :param geometry_col: Column containing WKT or shapely geometries for edges.
    :type geometry_col: str, optional, default="geometry"
    :param tki_col: Column with the KI node key (maps via map_nodes_tk_ind to a matrix index).
    :type tki_col: str, optional, default="tki"
    :param tkk_col: Column with the KK node key (maps via map_nodes_tk_ind to a matrix index).
    :type tkk_col: str, optional, default="tkk"
    :param xki_col: Column with KI X coordinate.
    :type xki_col: str, optional, default="XKOR_KI"
    :param yki_col: Column with KI Y coordinate.
    :type yki_col: str, optional, default="YKOR_KI"
    :param xkk_col: Column with KK X coordinate.
    :type xkk_col: str, optional, default="XKOR_KK"
    :param ykk_col: Column with KK Y coordinate.
    :type ykk_col: str, optional, default="YKOR_KK"
    :param kvri_col: Column indicating KI visibility (plot only if equals 1).
    :type kvri_col: str, optional, default="KVR_KI"
    :param kvrk_col: Column indicating KK visibility (plot only if equals 1).
    :type kvrk_col: str, optional, default="KVR_KK"
    :param dn_col: Column for pipe diameter used to scale edge linewidth.
    :type dn_col: str, optional, default="DN"
    :param cmap: Colormap for node coloring based on travel time.
    :type cmap: str, optional, default="viridis"
    :param node_size: Size of the node markers.
    :type node_size: float, optional, default=25.0
    :param linewidth_range: Min and max linewidth for edges scaled by DN.
    :type linewidth_range: tuple of float, optional, default=(0.6, 5.0)
    :param annotate: Whether to annotate nodes with their travel time values.
    :type annotate: bool, optional, default=False
    :param annotation_fmt: Format string for numeric annotations.
    :type annotation_fmt: str, optional, default="{:.1f}"
    :param agg: Aggregation for travel time when multiple edges reference the same node coordinates.
    :type agg: str, optional, default="max"
    :param show_values: If True, displays the travel-time value next to each plotted node in black.
    :type show_values: bool, optional, default=False
    :param dt_col: Column name containing the edge travel time to display (e.g., 'dt' or 'dt_new'). If None or missing, no edge labels are drawn.
    :type dt_col: str, optional
    :param show_edge_dt: If True, draw a black text label with the edge's dt value near the edge midpoint.
    :type show_edge_dt: bool, optional, default=False
    :param ttr_norm: Normalization method: 'data', 'clip', or 'percentile'.
    :type ttr_norm: str, optional, default="data"
    :param ttr_vmin: Minimum value for color scaling (used if ttr_norm='clip').
    :type ttr_vmin: float, optional
    :param ttr_vmax: Maximum value for color scaling (used if ttr_norm='clip').
    :type ttr_vmax: float, optional
    :param ttr_percentiles: Percentiles for normalization when ttr_norm='percentile'.
    :type ttr_percentiles: tuple of float, optional, default=(2.0, 98.0)
    :param treat_zero_as_unreachable: Treat 0 in TMat as unreachable (hidden), except source which remains 0.0.
    :type treat_zero_as_unreachable: bool, optional, default=True
    :param highlight_keys: Node keys to highlight (matched against tki/tkk), drawn as white stars.
    :type highlight_keys: list | tuple | set, optional
    :param highlight_match: Strategy for matching highlight keys: 'auto', 'both', 'numeric', or 'string'.
    :type highlight_match: str, optional, default="auto"
    :param highlight_marker_size: Size of the highlight star markers.
    :type highlight_marker_size: float, optional, default=140.0
    :param ax: Axis to plot on. If None, a new axis is created.
    :type ax: matplotlib.axes.Axes, optional
    :param colorbar: Whether to display a colorbar for travel time values.
    :type colorbar: bool, optional, default=True
    :param colorbar_label: Label for the colorbar (units).
    :type colorbar_label: str, optional, default="Travel time [h]"
    :param show_axis: If False, hides the entire axis (ticks, labels, frame).
    :type show_axis: bool, optional, default=True

    :return: A tuple containing:
        - ax: The matplotlib axis with the plot.
        - nodes_df: DataFrame of plotted nodes with columns ['x', 'y', 'TT'].
    :rtype: tuple(matplotlib.axes.Axes, pandas.DataFrame)
    """
    # --- Validate TMat
    if not isinstance(TMat, np.ndarray):
        raise TypeError("TMat must be a numpy.ndarray.")
    if TMat.ndim != 2 or TMat.shape[0] != TMat.shape[1]:
        raise ValueError("TMat must be a square 2D array (N x N).")

    n = TMat.shape[0]

    # --- Resolve source index from tk or int
    if isinstance(source, (int, np.integer)):
        src_idx = int(source)
    else:
        try:
            src_idx = int(map_nodes_tk_ind[source])
        except Exception as e:
            raise ValueError(f"Source '{source}' not found in map_nodes_tk_ind.") from e

    if not (0 <= src_idx < n):
        raise IndexError(f"Source index {src_idx} out of bounds for TMat of size {n}.")

    # --- Extract travel-time vector: times TO each node FROM source column
    tt_vec = TMat[:, src_idx].astype(float).copy()

    # Handle unreachable as zeros: convert to NaN (hide), but keep source at 0.0
    if treat_zero_as_unreachable:
        zero_mask = (tt_vec == 0.0)
        tt_vec[zero_mask] = np.nan
        tt_vec[src_idx] = 0.0  # keep source visible at zero

    # --- Prepare axes
    created_fig = False
    if ax is None:
        fig, ax = plt.subplots(figsize=Rm.DINA3q)
        created_fig = True

    # --- DN -> linewidth per-edge
    lw_min, lw_max = linewidth_range
    if dn_col in df.columns:
        dnf = pd.to_numeric(df[dn_col], errors="coerce").to_numpy()
        finite = np.isfinite(dnf)
        if finite.any():
            dn_min = float(np.nanmin(dnf[finite]))
            dn_max = float(np.nanmax(dnf[finite]))
            spread = dn_max - dn_min
            if spread > 0:
                dn_norm = (dnf - dn_min) / spread
                dn_norm = np.clip(dn_norm, 0, 1)
                row_widths = lw_min + dn_norm * (lw_max - lw_min)
            else:
                row_widths = np.full(len(dnf), 0.5 * (lw_min + lw_max))
        else:
            row_widths = np.full(len(df), lw_min)
    else:
        row_widths = np.full(len(df), lw_min)

    # --- Geometry parsing helpers (same as before)
    def _parse_coords_str(coord_str: str):
        pts = []
        for pair in coord_str.split(","):
            parts = pair.strip().split()
            if len(parts) >= 2:
                try:
                    x = float(parts[0]); y = float(parts[1])
                    pts.append((x, y))
                except ValueError:
                    continue
        return pts

    def _parse_linestring_wkt(wkt: str):
        left = wkt.find("("); right = wkt.rfind(")")
        if left == -1 or right == -1 or right <= left:
            return []
        inner = wkt[left+1:right]
        return _parse_coords_str(inner)

    def _parse_multilinestring_wkt(wkt: str):
        start = wkt.find("(("); end = wkt.rfind("))")
        if start == -1 or end == -1 or end <= start:
            return []
        inner = wkt[start+2:end]
        polylines = []
        for part in inner.split("),"):
            part = part.strip()
            if part.startswith("("): part = part[1:]
            if part.endswith(")"): part = part[:-1]
            pts = _parse_coords_str(part)
            if len(pts) >= 2:
                polylines.append(pts)
        return polylines

    def _geometry_to_polylines(g):
        if g is None or (isinstance(g, float) and np.isnan(g)):
            return []
        if hasattr(g, "geom_type"):  # shapely-like
            gt = getattr(g, "geom_type", "")
            try:
                if gt == "LineString":
                    coords = list(g.coords)
                    return [coords] if len(coords) >= 2 else []
                elif gt == "MultiLineString":
                    pls = []
                    for ls in getattr(g, "geoms", []):
                        coords = list(ls.coords)
                        if len(coords) >= 2:
                            pls.append(coords)
                    return pls
            except Exception:
                pass
        if isinstance(g, str):  # WKT
            s = g.strip().upper()
            if s.startswith("LINESTRING"):
                pts = _parse_linestring_wkt(g)
                return [pts] if len(pts) >= 2 else []
            if s.startswith("MULTILINESTRING"):
                return _parse_multilinestring_wkt(g)
        return []

    # --- Build edge segments + per-segment widths
    segments = []
    seg_widths = []
    for pos, (_, row) in enumerate(df.iterrows()):
        this_w = float(row_widths[pos])
        polylines = _geometry_to_polylines(row.get(geometry_col))
        if not polylines:
            # Fallback to straight KI→KK using coordinates
            try:
                x0, y0 = float(row[xki_col]), float(row[yki_col])
                x1, y1 = float(row[xkk_col]), float(row[ykk_col])
                segments.append(np.array([(x0, y0), (x1, y1)], dtype=float))
                seg_widths.append(this_w)
            except Exception:
                continue
        else:
            for pts in polylines:
                arr = np.array(pts, dtype=float)
                if arr.shape[0] >= 2:
                    segments.append(arr)
                    seg_widths.append(this_w)

    if segments:
        lc = LineCollection(
            segments,
            colors=(0.8, 0.8, 0.8, 1.0),   # light grey
            linewidths=seg_widths,
            zorder=1,
            capstyle="round",
            joinstyle="round",
        )
        ax.add_collection(lc)
        # --- Edge labels (dt) ---
        if show_edge_dt and (dt_col is not None) and (dt_col in df.columns):
            def _polyline_midpoint_xy(pts):
                """
                Compute true geometric midpoint of a polyline (list of (x,y)).
                Returns (xm, ym) or (None, None) if length is zero.
                """
                arr = np.asarray(pts, dtype=float)
                if arr.shape[0] < 2:
                    return (None, None)
                seg_vecs = np.diff(arr, axis=0)
                seg_len = np.hypot(seg_vecs[:, 0], seg_vecs[:, 1])
                total = float(seg_len.sum())
                if total == 0.0:
                    return (None, None)
                half = 0.5 * total
                cum = np.cumsum(seg_len)
                # Find the segment where the half-length falls
                j = int(np.searchsorted(cum, half))
                prev_cum = 0.0 if j == 0 else float(cum[j-1])
                remain = half - prev_cum
                # Interpolate along segment j
                p0 = arr[j]
                p1 = arr[j+1]
                seg_d = float(seg_len[j]) if seg_len[j] > 0 else 1.0
                t = remain / seg_d
                xm = p0[0] + t * (p1[0] - p0[0])
                ym = p0[1] + t * (p1[1] - p0[1])
                return (xm, ym)

            for _, row in df.iterrows():
                # 1) Skip missing / non-finite dt values
                val = abs(row[dt_col])/3600
                try:
                    if pd.isna(val):
                        continue
                except Exception:
                    continue

                # 2) Try geometry-based midpoint
                x_lab = y_lab = None
                try:
                    polylines = _geometry_to_polylines(row.get(geometry_col))
                except Exception:
                    polylines = None

                if polylines:
                    # Choose the longest polyline (stable for MULTILINESTRING)
                    def _pl_len(pl):
                        a = np.asarray(pl, dtype=float)
                        if a.shape[0] < 2:
                            return 0.0
                        v = np.diff(a, axis=0)
                        return float(np.hypot(v[:, 0], v[:, 1]).sum())

                    best_pl = max(polylines, key=_pl_len)
                    x_lab, y_lab = _polyline_midpoint_xy(best_pl)

                # 3) Fallback: midpoint of KI–KK coords if geometry missing/degenerate
                if (x_lab is None) or (y_lab is None):
                    # use standard column names ONLY if present
                    if {"XKOR_KI","YKOR_KI","XKOR_KK","YKOR_KK"}.issubset(df.columns):
                        try:
                            x0, y0 = float(row["XKOR_KI"]), float(row["YKOR_KI"])
                            x1, y1 = float(row["XKOR_KK"]), float(row["YKOR_KK"])
                            x_lab, y_lab = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
                        except Exception:
                            x_lab = y_lab = None

                # 4) Draw the label if we found a position
                if (x_lab is not None) and (y_lab is not None):
                    ax.text(
                        x_lab, y_lab,
                        annotation_fmt.format(val) + " h",
                        color="black",
                        fontsize=8,
                        ha="center", va="center",
                        zorder=4,
                        # Optional white halo for readability (uncomment the next 3 lines):
                        # path_effects=[
                        #     matplotlib.patheffects.withStroke(linewidth=2.5, foreground="white")
                        # ]
                    )

    # --- Build nodes from endpoints (use KVR filter and mapping to indices)
    idx_ki = df[tki_col].map(map_nodes_tk_ind)
    idx_kk = df[tkk_col].map(map_nodes_tk_ind)

    nodes_ki = pd.DataFrame({
        "x": df[xki_col],
        "y": df[yki_col],
        "idx": idx_ki,
        "KVR": df[kvri_col]
    })
    nodes_kk = pd.DataFrame({
        "x": df[xkk_col],
        "y": df[ykk_col],
        "idx": idx_kk,
        "KVR": df[kvrk_col]
    })
    nodes = pd.concat([nodes_ki, nodes_kk], ignore_index=True)

    # Filter: KVR == 1, valid coords and known index mapping
    nodes = nodes[(nodes["KVR"] == 1)]
    nodes = nodes.dropna(subset=["x", "y", "idx"])

    if nodes.empty:
        nodes_df = pd.DataFrame(columns=["x", "y", "TT"])
    else:
        # Attach travel time value using matrix indices
        indices = nodes["idx"].to_numpy(dtype=int, copy=True)
        # Guard: only indices within bounds
        in_bounds = (indices >= 0) & (indices < n)
        tt = np.full(len(indices), np.nan, dtype=float)
        tt[in_bounds] = tt_vec[indices[in_bounds]]
        nodes = nodes.assign(TT=tt).dropna(subset=["TT"])

        if nodes.empty:
            nodes_df = pd.DataFrame(columns=["x", "y", "TT"])
        else:
            if agg not in {"max", "min", "mean", "median", "first", "last"}:
                raise ValueError("agg must be one of: 'max','min','mean','median','first','last'")
            nodes_df = nodes.groupby(["x", "y"], as_index=False).agg(TT=("TT", agg))

    # --- Normalization (reuse same knobs)
    if nodes_df.empty:
        vmin, vmax = 0.0, 1.0
    else:
        vals = nodes_df["TT"].to_numpy(dtype=float)
        if ttr_norm == "percentile":
            low, high = ttr_percentiles
            vmin = float(np.nanpercentile(vals, low))
            vmax = float(np.nanpercentile(vals, high))
        elif ttr_norm == "clip":
            data_min = float(np.nanmin(vals))
            data_max = float(np.nanmax(vals))
            vmin = data_min if ttr_vmin is None else float(ttr_vmin)
            vmax = data_max if ttr_vmax is None else float(ttr_vmax)
        else:  # 'data'
            vmin = float(np.nanmin(vals))
            vmax = float(np.nanmax(vals))
        if not np.isfinite(vmin) or not np.isfinite(vmax):
            vmin, vmax = 0.0, 1.0
        if vmin == vmax:
            vmin -= 0.5; vmax += 0.5
    norm = Normalize(vmin=vmin, vmax=vmax)

    # --- Plot nodes
    if not nodes_df.empty:
        sc = ax.scatter(
            nodes_df["x"], nodes_df["y"],
            c=nodes_df["TT"], cmap=cmap, norm=norm,
            s=node_size,
            edgecolors="k", linewidths=0.25,
            zorder=2
        )
        if colorbar:
            cbar = plt.colorbar(sc, ax=ax, shrink=0.85)
            cbar.set_label(colorbar_label)
        if show_values:
            for _, r in nodes_df.iterrows():
                ax.annotate(
                    annotation_fmt.format(r["TTR"] if "TTR" in r else r["TT"]) + "h",
                    xy=(r["x"], r["y"]),
                    xytext=(3, 3),
                    textcoords="offset points",
                    fontsize=8,
                    color="black",
                    zorder=3,
                )

    # Optional annotations
    if annotate and not nodes_df.empty:
        for _, r in nodes_df.iterrows():
            ax.annotate(
                annotation_fmt.format(r["TT"]),
                xy=(r["x"], r["y"]),
                xytext=(3, 3),
                textcoords="offset points",
                fontsize=8,
                color="black",
                zorder=3,
            )

    # --- Highlights: match against tki/tkk (robust)
    if highlight_keys:
        # Normalize keys to Python scalars
        keys_list = []
        for k in list(highlight_keys):
            try:
                keys_list.append(k.item() if hasattr(k, "item") else k)
            except Exception:
                keys_list.append(k)

        sel_ki_direct = df[tki_col].isin(keys_list)
        sel_kk_direct = df[tkk_col].isin(keys_list)

        norm_str = lambda s: s.astype(str).str.strip().str.casefold()
        keys_str = pd.Series(keys_list, dtype="object").astype(str).str.strip().str.casefold()
        sel_ki_str = norm_str(df[tki_col]).isin(keys_str)
        sel_kk_str = norm_str(df[tkk_col]).isin(keys_str)

        ki_num = pd.to_numeric(df[tki_col], errors="coerce")
        kk_num = pd.to_numeric(df[tkk_col], errors="coerce")
        keys_num = pd.to_numeric(pd.Series(keys_list), errors="coerce")
        sel_ki_num = ki_num.isin(keys_num)
        sel_kk_num = kk_num.isin(keys_num)

        if highlight_match == "numeric":
            sel_ki = sel_ki_num
            sel_kk = sel_kk_num
        elif highlight_match == "string":
            sel_ki = sel_ki_str
            sel_kk = sel_kk_str
        elif highlight_match == "both":
            sel_ki = sel_ki_direct | sel_ki_str | sel_ki_num
            sel_kk = sel_kk_direct | sel_kk_str | sel_kk_num
        else:  # 'auto'
            ki_is_num = pd.api.types.is_numeric_dtype(df[tki_col])
            kk_is_num = pd.api.types.is_numeric_dtype(df[tkk_col])
            if ki_is_num and kk_is_num:
                sel_ki = sel_ki_num
                sel_kk = sel_kk_num
            else:
                sel_ki = sel_ki_str
                sel_kk = sel_kk_str

        stars_ki = df.loc[sel_ki, [xki_col, yki_col]].rename(columns={xki_col:"x", yki_col:"y"})
        stars_kk = df.loc[sel_kk, [xkk_col, ykk_col]].rename(columns={xkk_col:"x", ykk_col:"y"})
        stars = pd.concat([stars_ki, stars_kk], ignore_index=True)
        stars = stars.dropna(subset=["x", "y"]).drop_duplicates()

        if not stars.empty:
            ax.scatter(
                stars["x"], stars["y"],
                marker="*",
                s=highlight_marker_size,
                facecolor="white",
                edgecolor="black",
                linewidths=0.9,
                zorder=10,
                label="Source"
            )
            ax.legend(loc="best", frameon=True)

    # --- Final touches
    ax.set_aspect("equal", adjustable="datalim")
    ax.autoscale_view()
    if not show_axis:
        ax.axis("off")
    ax.set_title("Travel Time [h]")

    return ax, nodes_df
