Classes and Objects
================================

Welcome to the Classes and Objects page! Here, we will delve into the differnt classes and objects and their relationship. Refer to the :doc:`functions` page to learn more about the functions that create these objects.

.. note::
    Currently, not all Objects that exist in PT3S are documented. These will be added in the future.

.. testsetup::

    import os
    import geopandas
    import logging
    import networkx as nx
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
    dbFilename="Example1"
    dbFile=os.path.join(os.path.dirname(os.path.abspath(dxAndMxHelperFcts.__file__))
                    +'/Examples/'
                    +dbFilename
                    +'.db3')
    m=dxAndMxHelperFcts.readDxAndMx(dbFile=dbFile                                 
                                ,preventPklDump=True
    )

.. _m object:
m Object
--------
The m object or dxWithMx object is a wrapper for Dx with attached Mx and the center piece in working with PT3S. It is created by :ref:`readDxAndMx-label`

.. autofunction:: dxAndMxHelperFcts.dxWithMx.__init__

.. image:: uml/combined_image.png
   :alt: classes_dxAndMxHelperFcts
   :width: 100%
   :align: center
|

Dataframes
~~~~~~~~~~

From this object m, you can now access a variety of dataframes created by PT3S based on the model and results

.. doctest::
    
    >>> print([attr for attr in dir(m) if isinstance(getattr(m, attr), pd.DataFrame)])    
    ['V3_AGSN', 'V3_AGSNVEC', 'V3_FWVB', 'V3_KNOT', 'V3_ROHR', 'V3_ROHRVEC', 'V3_VBEL', 'V3_WBLZ', 'dfAGSN', 'dfWBLZ', 'gdf_FWVB', 'gdf_KNOT', 'gdf_ROHR']

The following section presents these dataframes by documenting the functions that create them.

V3_ROHR
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_ROHR
.. doctest::
    
    >>> print(m.V3_ROHR)
                          pk                 fkDE  ...        PHRAbs         JVAbs
    0    5442010239090746007  5306805303452857793  ...  1.041356e-02  2.858564e-01
    1    4917786378639043296  5306805303452857793  ...  1.464281e-02  2.559136e-01
    2    4762482310382009633  5306805303452857793  ...  1.084467e-02  2.645375e-01
    3    4987229536643024523  5306805303452857793  ...  1.804474e-03  2.640792e-01
    4    5722206630503885118  5306805303452857793  ...  1.978778e-03  2.640800e-01
    ..                   ...                  ...  ...           ...           ...
    519  4919408196640282331  5306805303452857793  ...  7.555330e-25  2.897193e-23
    520  4957957828740199285  5306805303452857793  ...  0.000000e+00  0.000000e+00
    521  5499776682108862751  5306805303452857793  ...  0.000000e+00  0.000000e+00
    522  5285235772707481262  5306805303452857793  ...  7.560484e-03  7.560484e-01
    523  5373158549695106826  5306805303452857793  ...  7.642428e-03  7.642428e-01
    <BLANKLINE>
    [524 rows x 216 columns]

V3_KNOT
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_KNOT
.. doctest::
    
    >>> print(m.V3_KNOT)
                          pk                 fkDE  ...   QM       dPH
    3    5669301360686511351  5306805303452857793  ...  0.0  1.488921
    4    5397948523091900401  5306805303452857793  ...  0.0  1.467910
    5    5239335112004772156  5306805303452857793  ...  0.0  1.444288
    6    5298886695042021307  5306805303452857793  ...  0.0  1.434558
    7    4993257270457791438  5306805303452857793  ...  0.0  1.432193
    ..                   ...                  ...  ...  ...       ...
    515  5705481928638455076  5306805303452857793  ...  0.0       NaN
    516  4910948593863484232  5306805303452857793  ...  0.0       NaN
    517  5032870132214455820  5306805303452857793  ...  0.0 -0.038701
    518  4808122385198820357  5306805303452857793  ...  0.0 -0.038701
    519  4810663080415972317  5306805303452857793  ...  0.0       NaN
    <BLANKLINE>
    [517 rows x 214 columns]

V3_VBEL
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_VBEL
.. doctest::
    
    >>> print(m.V3_VBEL)
                                                  pk  ...       mlc_k
    OBJTYPE OBJID                                     ...            
    FWES    5194722485643852853  5194722485643852853  ...  577.049723
            5393031835236689087  5393031835236689087  ...  593.013845
    FWVB    4611752310942477664  4611752310942477664  ...  574.339884
            4612528660388965271  4612528660388965271  ...  551.357794
            4612562908060328263  4612562908060328263  ...  574.527331
    ...                                          ...  ...         ...
    VENT    5397401198360947165  5397401198360947165  ...   577.04972
            5514879539114546017  5514879539114546017  ...  586.490818
            5586353371153335311  5586353371153335311  ...   577.15915
            5652541284139882253  5652541284139882253  ...  592.208663
            5684594766069449552  5684594766069449552  ...  577.085888
    <BLANKLINE>
    [883 rows x 619 columns]

V3_AGSN
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_AGSN
.. doctest::
    
    >>> print(m.V3_AGSN)
        Pos  ... ('TMAX', 'mlc', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-13 23:00:00'))_n
    0    -1  ...                                          602.48758                                   
    0     0  ...                                          602.48758                                   
    1     1  ...                                         602.419501                                   
    2     2  ...                                         602.385399                                   
    3     3  ...                                         602.306951                                   
    ..   ..  ...                                                ...                                   
    523  39  ...                                         582.046941                                   
    524  40  ...                                         582.197052                                   
    525  41  ...                                         582.361158                                   
    526  42  ...                                         582.680754                                   
    527  43  ...                                         583.017569                                   
    <BLANKLINE>
    [537 rows x 52 columns]

V3_ROHRVEC
""""""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_ROHRVEC
.. doctest::
    
    >>> print(m.V3_ROHRVEC)
                           pk  ... (TMAX, tMVEC, 2023-02-12 23:00:00, 2023-02-13 23:00:00)
    0     5442010239090746007  ...                                          98.646645     
    1     5442010239090746007  ...                                          98.646645     
    2     4917786378639043296  ...                                          55.044947     
    3     4917786378639043296  ...                                          55.044947     
    4     4762482310382009633  ...                                          56.352818     
    ...                   ...  ...                                                ...     
    1065  5499776682108862751  ...                                                0.0     
    1066  5285235772707481262  ...                                          56.845562     
    1067  5285235772707481262  ...                                          56.845562     
    1068  5373158549695106826  ...                                         -30.267313     
    1069  5373158549695106826  ...                                         -30.267313     
    <BLANKLINE>
    [1070 rows x 294 columns]

V3_AGSNVEC
""""""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._V3_AGSNVEC
.. doctest::
    
    >>> print(m.V3_AGSNVEC)
        Pos                   pk  ...      QM_min      QM_max
    0     0  5755933101669454049  ...  287.090085  538.206592
    1     0  5755933101669454049  ...  287.090085  538.206592
    2     1  5755933101669454049  ...  287.090085  538.206592
    3     2  5755933101669454049  ... -538.206592 -287.090085
    4     3  5755933101669454049  ... -538.206592 -287.090085
    ..   ..                  ...  ...         ...         ...
    532  39  4868980900521118307  ...  -28.479333  -15.303667
    533  40  4868980900521118307  ...  -28.479333  -15.303667
    534  41  4868980900521118307  ...  -26.661928  -14.329748
    535  42  4868980900521118307  ...  -18.238317   -9.812775
    536  43  4868980900521118307  ...   -5.141132   -2.769349
    <BLANKLINE>
    [537 rows x 352 columns]

GeoDataframes
"""""""""""""

.. autofunction:: dxAndMxHelperFcts.dxWithMx._gdfs
.. doctest::
    
    >>> print(m.gdf_ROHR)
                          pk  ...                        geometry
    3    5669301360686511351  ...  POINT (713620.268 5578828.419)
    4    5397948523091900401  ...  POINT (713602.295 5578860.106)
    5    5239335112004772156  ...  POINT (713574.062 5578909.873)
    6    5298886695042021307  ...  POINT (713553.840 5578945.533)
    7    4993257270457791438  ...  POINT (713553.394 5578952.352)
    ..                   ...  ...                             ...
    515  5705481928638455076  ...         POINT (645.000 285.000)
    516  4910948593863484232  ...         POINT (650.000 170.000)
    517  5032870132214455820  ...         POINT (530.000 285.000)
    518  4808122385198820357  ...         POINT (530.000 170.000)
    519  4810663080415972317  ...         POINT (530.000 103.000)
    <BLANKLINE>
    [517 rows x 215 columns]

    >>> print(m.gdf_KNOT)
                          pk  ...                        geometry
    0    4743997951091160959  ...  POINT (713181.847 5578489.925)
    1    5014209100699808035  ...  POINT (713369.327 5578395.123)
    2    4627580049017248376  ...  POINT (713251.536 5578455.252)
    3    5018070164989726059  ...  POINT (713037.635 5578289.847)
    4    5668240250035163192  ...  POINT (713066.258 5578315.171)
    ..                   ...  ...                             ...
    333  5604960832731508460  ...  POINT (713185.109 5578370.183)
    334  5365421822901958434  ...  POINT (713186.745 5578333.649)
    335  5430995747331401210  ...  POINT (713116.958 5578379.965)
    336  5066450637911116733  ...  POINT (713080.421 5578361.379)
    337  5540117011473392085  ...                            None
    <BLANKLINE>
    [338 rows x 204 columns]

    >>> print(m.gdf_FWVB)
                          pk  ...                        geometry
    0    4743997951091160959  ...  POINT (713181.847 5578489.925)
    1    5014209100699808035  ...  POINT (713369.327 5578395.123)
    2    4627580049017248376  ...  POINT (713251.536 5578455.252)
    3    5018070164989726059  ...  POINT (713037.635 5578289.847)
    4    5668240250035163192  ...  POINT (713066.258 5578315.171)
    ..                   ...  ...                             ...
    333  5604960832731508460  ...  POINT (713185.109 5578370.183)
    334  5365421822901958434  ...  POINT (713186.745 5578333.649)
    335  5430995747331401210  ...  POINT (713116.958 5578379.965)
    336  5066450637911116733  ...  POINT (713080.421 5578361.379)
    337  5540117011473392085  ...                            None
    <BLANKLINE>
    [338 rows x 204 columns]

Graphs
~~~~~~~~~~

Also accesible are NetworkX-Graphs and a corresponding dictionnary with node positions.

.. doctest::
    
    >>> print([attr for attr in dir(m) if not attr.startswith('_') and isinstance(getattr(m, attr), (nx.Graph, nx.DiGraph, dict))])
    ['G', 'GSig', 'nodeposDctNx']

G
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._G

GSig
"""""""
.. autofunction:: dxAndMxHelperFcts.dxWithMx._GSig    

Miscellaneous
~~~~~~~~~~~~~

Also accesible SirCalcExecution- and -Xml-File and the dir to mx files

.. doctest::

    >>> print([attr for attr in dir(m) if not attr.startswith('_') and isinstance(getattr(m, attr), str)])
    ['SirCalcExeFile','SirCalcXmlFile', 'flowMVEC', 'wDirMx']

SirCalcExeFile exists if maxRecords=-1. Additioal forceSir3sRead=True might be necessary.

.. _Dx object:
Dx object
---------

You can find data regarding the model at the m.dx object

.. doctest::
    
    >>> dx=m.dx    

From this object, you can access the model’s database and its tables.

.. doctest::
    
    >>> dx.dataFrames.keys() # doctest: +SKIP
    >>> dfALLG=dx.dataFrames['ALLG']
Dataframes
~~~~~~~~~~

.. note::
    Currently, by far not all dfs that are attributes of a Dx object are documented. Maybe this will be added in the future.
    V3-VBEL, _KNOT, _ROHR and _FWVB are dx attributes.
    The corresponding m attributes (V3-VBEL, _KNOT, _ROHR and _FWVB) extend the dx dfs with result columns.

dfLAYR
""""""
.. autofunction:: Dx.Dx._dfLAYR

.. _Mx object:
Mx object
---------

You can find additional regarding the results at the m.mx object

.. doctest::
    
    >>> mx=m.mx
 
From this object you can acces the raw time curve and the vector data

.. doctest::
    
    >>> mx.df.head() # doctest: +SKIP
    >>> mx.dfVecAggs.head() # doctest: +SKIP   
 
Known Issues
------------

Column tuple names
~~~~~~~~~~~~~~~~~~

Columns containing values that are not generated by PT3S but directly read from SIR 3S are tuples like `('STAT', 'ROHR~*~*~*~A', Timestamp('2023-02-12 23:00:00'))`.

.. doctest::

    >>> print([col for col in m.V3_ROHR.columns if isinstance(col, tuple)][:10])
    [('STAT', 'ROHR~*~*~*~A', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00')), ('TIME', 'ROHR~*~*~*~A', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00')), ('TMIN', 'ROHR~*~*~*~A', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-13 23:00:00')), ('TMAX', 'ROHR~*~*~*~A', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-13 23:00:00')), ('STAT', 'ROHR~*~*~*~DTTR', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00')), ('TIME', 'ROHR~*~*~*~DTTR', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00')), ('TMIN', 'ROHR~*~*~*~DTTR', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-13 23:00:00')), ('TMAX', 'ROHR~*~*~*~DTTR', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-13 23:00:00')), ('STAT', 'ROHR~*~*~*~DWVERL', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00')), ('TIME', 'ROHR~*~*~*~DWVERL', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00'))]

Often times when using these names with other libraries like pandas, several issues can arise.

You are not able to access a pandas DataFrame column with such a name. You might have tried like this.

.. doctest::

    >>> m.V3_ROHR["('TIME', 'ROHR~*~*~*~DTTR', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00'))"] # doctest: +SKIP
    KeyError: "('TIME', 'ROHR~*~*~*~DTTR', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00'))"

Try this instead:

.. doctest::

    >>> import pandas as pd
    >>> from pandas import Timestamp
    >>> column_name = ('TIME', 'ROHR~*~*~*~DTTR', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00'))
    >>> column_data = m.V3_ROHR[column_name]
    >>> print(column_data)
    0       0.013439
    1       0.025363
    2       0.017844
    3       0.002976
    4       0.003263
            ...    
    519    26.078106
    520    17.345263
    521    20.641092
    522     0.002895
    523      0.00293
    Name: (TIME, ROHR~*~*~*~DTTR, 2023-02-12 23:00:00, 2023-02-12 23:00:00), Length: 524, dtype: object

You could also transform all indices from tuple to string:

.. doctest::

    >>> m.V3_ROHR.columns = [str(col) for col in m.V3_ROHR.columns]
    >>> print(m.V3_ROHR["('TIME', 'ROHR~*~*~*~DTTR', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00'))"])
    1       0.025363
    2       0.017844
    3       0.002976
    4       0.003263
            ...    
    519    26.078106
    520    17.345263
    521    20.641092
    522     0.002895
    523      0.00293