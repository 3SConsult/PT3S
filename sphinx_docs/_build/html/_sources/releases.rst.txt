Releases
================================

90.14.21.0.dev1
---------------
    
    new:
    
    readMx:

        Reads SIR 3S results and returns a Mx object.
        
        Args:
            rootdire (str): 
                Path to root directory of the Model. The results are read into a Mx object via the mx files.
                    
            logPathOutputFct (fct, optional, default=os.path.relpath):
                logPathOutputFct(fileName) is used for logoutput of filenames unless explicitly stated otherwise in the logoutput
        
        Returns:
            Results: Mx object:
                mx.df: pandas-Df ('time curve data') from from SIR 3S' MXS file(s)
                mx.dfVecAggs: pandas-Df ('vector data') from SIR 3S' MXS file(s)

90.14.20.0.dev1
---------------
    readDxAndMx:

        fix:
            m is constructed (instead of reading m-pickle) if SIR 3S' dbFile is newer than m-pickle; in previous releases m-pickle was read even if dbFile is newer
        new:
            INFO: if SIR 3S' dbFile is newer than SIR 3S' mxFile; in this case the results are maybe dated or (worse) incompatible to the model 
            
90.14.19.0.dev1
---------------
    SIR 3S db3 and mx files used in Examples are now included in the package.

90.14.18.0.dev1
---------------
    readDxAndMx:

        mxsVecsResults2MxDfVecAggs: new
            (list, optional, default=None): 
                List of timesteps for SIR 3S' Vector-Results to be included in mx.dfVecAggs.
            
        crs: new   
            (str, optional, default=None):
                (=coordinate reference system) Determines crs used in geopandas-Dfs (Possible value:'EPSG:25832'). If None, crs will be read from the dbFile.                          
        
    dxWithMx:
        new: geopandas-Dfs: gdf_KNOT, gdf_ROHR, gdf_FWVB
        new: setLayerContentTo

90.14.17.0.dev1
---------------
    readDxAndMx:
    
        preventPklDump:
            True now forces SIR 3S sources to be read because pickles are deleted if existing before timecheck pickles vs. SIR 3S sources is performed.
        dxWithMx (readDxAndMx):
            V3_FWVB: new columns: QM, TI, TK
            
    Dx:
        update:
            returns now rowsAffectedTotal