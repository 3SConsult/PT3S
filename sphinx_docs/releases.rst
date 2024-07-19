Releases
========

Welcome to the Releases page! Here, you can keep up with the additions and fixes that come with new releases.

90.14.25.0.dev1
---------------

**Changed:**

- Dx:
    - Logging
    - processing of PGRP_PUMP, PGRP_PUMP_BZ, RMES_DPTS, RMES_DPTS_BZ
    

90.14.24.0.dev1
---------------

**New:**

- DistrictHeating db3+Mx included in package for Example3

90.14.23.0.dev1
---------------
**Fix:**

- readMx:
    Logging: _Done added

- Selenium as install req

- Examples: XML and Mx1 File included with content, all other result files blank


90.14.22.0.dev1
---------------

90.14.21.0.dev1
---------------
**New:**

- readMx:
    Reads SIR 3S results and returns a Mx object.
    
    Args:
        - rootdire (str): Path to root directory of the Model. The results are read into a Mx object via the mx files.
        - logPathOutputFct (fct, optional, default=os.path.relpath): logPathOutputFct(fileName) is used for logoutput of filenames unless explicitly stated otherwise in the logoutput
    Returns:
        - Results: Mx object:
            - mx.df: pandas-Df ('time curve data') from from SIR 3S' MXS file(s)
            - mx.dfVecAggs: pandas-Df ('vector data') from SIR 3S' MXS file(s)

90.14.20.0.dev1
---------------
- readDxAndMx:
    **Fix:**
        - m is constructed (instead of reading m-pickle) if SIR 3S' dbFile is newer than m-pickle; in previous releases m-pickle was read even if dbFile is newer
    **New:**
        - INFO: if SIR 3S' dbFile is newer than SIR 3S' mxFile; in this case the results are maybe dated or (worse) incompatible to the model 

90.14.19.0.dev1
---------------
**New:**

- SIR 3S db3 and mx files used in Examples are now included in the package.

90.14.18.0.dev1
---------------
- readDxAndMx:
    **New:**
        - mxsVecsResults2MxDfVecAggs: (list, optional, default=None): List of timesteps for SIR 3S' Vector-Results to be included in mx.dfVecAggs.
        - crs: (str, optional, default=None): (=coordinate reference system) Determines crs used in geopandas-Dfs (Possible value:'EPSG:25832'). If None, crs will be read from the dbFile.
- dxWithMx:
    **New:**
        - geopandas-Dfs: gdf_KNOT, gdf_ROHR, gdf_FWVB
        - setLayerContentTo

90.14.17.0.dev1
---------------
- readDxAndMx:
    **New:**
        - preventPklDump: True now forces SIR 3S sources to be read because pickles are deleted if existing before timecheck pickles vs. SIR 3S sources is performed.
        - dxWithMx (readDxAndMx): V3_FWVB: new columns: QM, TI, TK
- Dx:
    **Update:**
        - returns now rowsAffectedTotal
