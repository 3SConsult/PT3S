Releases
================================

90.14.19.0.dev1
---------------
    db3 and mx files necessary for documentation use are now include in the package

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