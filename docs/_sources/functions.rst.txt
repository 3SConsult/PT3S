Functions
================================

Welcome to the Functions page! Here, we will delve into the details of each function, its purpose, parameters and returns.

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

Read SIR 3S Model and Results
-----------------------------
.. autofunction:: dxAndMxHelperFcts.readDxAndMx

Usage Tutorial
~~~~~~~~~~~~~~
    
Getting dbFile(str)
"""""""""""""""""""

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

Reading data
""""""""""""

Create a dxWithMx object using readDxAndMx(). 

.. doctest::
    
    >>> m=dxAndMxHelperFcts.readDxAndMx(dbFile=dbFile)

From this object m, you can now access a variety of dataframes created by PT3S based on the model and results

.. doctest::
    
    >>> print([attr for attr in dir(m) if isinstance(getattr(m, attr), pd.DataFrame)])    
    ['V3_AGSN', 'V3_AGSNVEC', 'V3_FWVB', 'V3_KNOT', 'V3_ROHR', 'V3_ROHRVEC', 'V3_VBEL', 'V3_WBLZ', 'dfAGSN', 'dfWBLZ', 'gdf_FWVB', 'gdf_KNOT', 'gdf_ROHR']

.. doctest::
    
    >>> m.V3_AGSN.head() # doctest: +SKIP

Also accesible are NetworkX-Graphs, SirCalcExecution- and -Xml-File and the dir to mx files

.. doctest::
    
    >>> print([attr for attr in dir(m) if not attr.startswith('_') and not isinstance(getattr(m, attr), pd.DataFrame)])
    ['G', 'GSig', 'SirCalcExeFile', 'SirCalcXmlFile', 'dx', 'mx', 'nodeposDctNx', 'switchV3DfColsToMultiindex', 'wDirMx']

You can find additional data regarding the model at the m.dx object

.. doctest::
    
    >>> dx=m.dx    

From this object, you can access the model’s database and its tables.

.. doctest::
    
    >>> dx.dataFrames.keys() # doctest: +SKIP
    >>> dfALLG=dx.dataFrames['ALLG']

You can find additional data regarding the results at the m.mx object

.. doctest::
    
    >>> mx=m.mx
 
From this object you can acces the time curve data and the vector data

.. doctest::
    
    >>> mx.df.head() # doctest: +SKIP
    >>> mx.dfVecAggs.head() # doctest: +SKIP
     
Read SIR 3S Results only
------------------------
.. autofunction:: dxAndMxHelperFcts.readMx

SIR 3S Model- and Result-Data
-----------------------------

Initialization
~~~~~~~~~~~~~~

.. autofunction:: dxAndMxHelperFcts.dxWithMx.__init__

Dataframes
~~~~~~~~~~

V3_ROHR
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_ROHR

V3_KNOT
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_KNOT

V3_VBEL
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_VBEL

V3_AGSN
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_AGSN

V3_ROHRVEC
""""""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_ROHRVEC

V3_AGSNVEC
""""""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_AGSNVEC

gdfs
""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._gdfs

Graphs
~~~~~~~~~~

G
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._G


SIR 3S Model-Data
-----------------

Dataframes
~~~~~~~~~~

.. note::
    Currently, by far not all dfs that are attributes of a Dx object are documented. Maybe this will be added in the future.
    V3-VBEL, _KNOT, _ROHR and _FWVB are dx attributes.
    The corresponding m attributes (V3-VBEL, _KNOT, _ROHR and _FWVB) extend the dx dfs with result columns.

dfLAYR
""""""
.. autofunction:: Dx.Dx._dfLAYR

Methods
~~~~~~~

update
""""""
.. autofunction:: Dx.Dx.update

insert
""""""
.. autofunction:: Dx.Dx.insert

importFromSIR3S
"""""""""""""""
.. autofunction:: Dx.Dx.importFromSIR3S
.. autofunction:: Dx.fimportFromSIR3S

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

:ref:`ex1` explains its application.

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
    
:ref:`ex7` explains its application.    