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

Examples
~~~~~~~~
    
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

V3_AGSN
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_AGSN

V3_AGSNVEC
""""""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_AGSNVEC

V3_ROHRVEC
""""""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_ROHRVEC

gdfs
""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._gdfs


SIR 3S Model-Data
-----------------

Dataframes
~~~~~~~~~~

.. note::
    Currently, by far not all dfs that are attributes of a Dx object are documented. These will be added in the future.

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

Plot District Heating Network
-----------------------------

.. autofunction:: pNFD.pNFD_FW