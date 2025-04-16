Functions
================================

Welcome to the Functions page! Here, we will delve into the details of each function, its purpose, parameters and returns. Links to the description of returned objects on the :doc:`objects` page will be provided.

.. note::
    Currently, not all functions that are included in PT3S are documented. These will be added in the future.

.. testsetup::

    import os
    import geopandas
    import logging
    import pandas as pd
    import io
    import subprocess
    from PIL import Image

    import folium
    from folium.plugins import HeatMap

    try:
        from PT3S import dxAndMxHelperFcts
    except:
        import dxAndMxHelperFcts

.. _readDxAndMx-label:
Read SIR 3S Model and Results
-----------------------------
.. autofunction:: PythonWrapperToolkit.StartTransaction
Returns :ref:`m object`.

Usage Tutorial
~~~~~~~~~~~~~~

Enter the name of the .db3 file you want to read    

.. doctest::
    
    >>> dbFilename="Example1"

Enter the path to the dir, where this .db3 file is located. In this case the Example data included in PT3S is used.
    
.. doctest::
    
    >>> rootdir=os.path.join(os.path.dirname(os.path.abspath(dxAndMxHelperFcts.__file__)), 'Examples')

Concatenate the rootdir with the dbFilename
    
.. doctest::
    
    >>> dbFile=os.path.join(rootdir, dbFilename + '.db3')
 
dbFile can now be used as a parameter for readDxAndMx()
    
.. doctest::
    
    >>> dbFile
    'C:\\Users\\jablonski\\3S\\PT3S\\Examples\\Example1.db3'

Create a dxWithMx object using readDxAndMx(). 

.. doctest::
    
    >>> m=dxAndMxHelperFcts.readDxAndMx(dbFile=dbFile)

Refer to the :doc:`examples` page. The Examples 1-X use this function.

Read SIR 3S Results only
------------------------
.. autofunction:: dxAndMxHelperFcts.readMx
Returns :ref:`Mx object`.

Refer to :ref:`ex2`. It uses this function. 

Methods
-------

Methods regarding :ref:`m object`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

switchV3DfColsToMultiindex
""""""""""""""""""""""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx.switchV3DfColsToMultiindex

Methods regarding :ref:`Dx object` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

update
""""""
.. autofunction:: Dx.Dx.update

insert
""""""
.. autofunction:: Dx.Dx.insert

importFromSIR3S
"""""""""""""""
.. autofunction:: Dx.Dx.importFromSIR3S
.. autofunction:: Dx.fimportFromSIR3S #Not really dx object

setLayerContentTo
"""""""""""""""""
.. autofunction:: Dx.Dx.setLayerContentTo

SdfCsv
------

.. autofunction:: sdfCsv.SdfCsv.__init__

Plot Network Color Diagram
--------------------------

.. autofunction:: ncd.pNcd_pipes

.. autofunction:: ncd.pNcd_nodes

Usage Tutorial
~~~~~~~~~~~~~~


.. testsetup::

    import os
    import geopandas as gpd
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import matplotlib.colors as mcolors
    import matplotlib.patheffects as path_effects
    import numpy as np
    import ncd
    import Rm

    # Sample data for demonstration
    gdf_ROHR = gpd.GeoDataFrame({'geometry': [], 'DI': []})
    gdf_FWVB = gpd.GeoDataFrame({'geometry': [], 'QM': []})
    gdf_ROHR['geometry'] = gpd.points_from_xy([0, 1], [0, 1])
    gdf_FWVB['geometry'] = gpd.points_from_xy([0, 1], [0, 1])
    gdf_ROHR['DI'] = [100, 200]
    gdf_FWVB['QM'] = [10, 20]

Plot on an axes. Use pNcd_pipes for pipes and pNcd_nodes for nodes. 

If you plot multiple times on the same axes, use zorder to determine plotting order.

Refer to :ref:`ex1`. It uses this function. 

.. doctest::

    >>> fig, ax = plt.subplots()
    >>> pipes_patches = ncd.pNcd_pipes(ax=ax, gdf=gdf_ROHR, attribute='DI', zorder=1)
    >>> nodes_patches = ncd.pNcd_nodes(ax=ax, gdf=gdf_FWVB, attribute='QM', zorder=2)
    >>> all_patches = pipes_patches + nodes_patches
    >>> ax.legend(handles=all_patches, loc='best') # doctest: +SKIP
    >>> plt.show()
    Figure(640x480)
 
Plot Source Spectrum
--------------------

.. autofunction:: ncd.plot_src_spectrum

Refer to :ref:`ex7`. It uses this function.      