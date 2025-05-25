# -*- coding: utf-8 -*-
"""
Created on Fri May 23 10:25:04 2025

@author: jablonski

This is a collection of Functions that utilize the SIR 3S Toolkit to perform certain tasks regarding the import of data into SIR 3S and the editing of models in SIR 3S.
"""

import logging
logger = logging.getLogger('PT3S') 
import pandas as pd

def SIR3S_model_insert_dfPipes(s3s, dfPipes):
    '''
    Takes a dataframe with each row representing one pipe and creates a new SIR 3S District Heating Model with it. The dataframe needs minimum of cols: geometry(LINESTRING), MATERIAL(String), DN(int), KVR(int)
    param: s3s: instance of SIR3S_Model() with opened model
    type: PythonWrapperToolkit.SIR3S_Model()
    param: dfPipes
    type: pd.dataframe
    '''
    #Prep dfPipes
    #dfPipes.loc[:, 'nodeKI_id'] = ''
    #dfPipes.loc[:, 'nodeKK_id'] = ''

    # Initialize climbing indices
    climbing_index = 0
    
    # Iterate over each row in the DataFrame
    for idx in range(len(dfPipes)):
        dfPipes.at[idx, 'nodeKI_id'] = climbing_index
        dfPipes.at[idx, 'nodeKK_id'] = climbing_index + 1
        climbing_index += 2

    #Toolkit Code
    s3s.StartEditSession(SessionName="AddNodesAndPipes")

    def AddNodesAndPipes(dfXL, node_counter):
        '''
        '''
        #fix: ensure no duplicate node names
        supplementary_nodes = pd.DataFrame(columns=['id', 'tk'])
        for i in range(len(dfXL)):
            # --- nodeKI logic ---
            nodeKI_id = dfXL.loc[i, 'nodeKI_id']
            if nodeKI_id not in supplementary_nodes['id'].values:
                x_ki, y_ki = dfXL.loc[i, 'geometry'].coords[0]
                tk_ki = s3s.AddNewNode("-1", f"Node{i}KI {VL_or_RL(int(dfXL.loc[i, 'KVR']))}", f"Node{i}", x_ki, y_ki, 1.0, 0.1, 2.0, f"Node{i}KI", f'ID{node_counter}', int(dfXL.loc[i, 'KVR']))
                supplementary_nodes.loc[len(supplementary_nodes)] = [nodeKI_id, tk_ki]
                dfXL.loc[i, 'nodeKI'] = tk_ki
                node_counter += 1
            else:
                tk_ki = supplementary_nodes.loc[supplementary_nodes['id'] == nodeKI_id, 'tk'].values[0]
                dfXL.loc[i, 'nodeKI'] = tk_ki

            # --- nodeKK logic ---
            nodeKK_id = dfXL.loc[i, 'nodeKK_id']
            if nodeKK_id not in supplementary_nodes['id'].values:
                x_kk, y_kk = dfXL.loc[i, 'geometry'].coords[-1]
                tk_kk = s3s.AddNewNode("-1", f"Node{i}KK {VL_or_RL(int(dfXL.loc[i, 'KVR']))}", f"Node{i}", x_kk, y_kk, 1.0, 0.1, 2.0, f"Node{i}KK", f'ID{node_counter}', int(dfXL.loc[i, 'KVR']))
                supplementary_nodes.loc[len(supplementary_nodes)] = [nodeKK_id, tk_kk]
                dfXL.loc[i, 'nodeKK'] = tk_kk
                node_counter += 1
            else:
                tk_kk = supplementary_nodes.loc[supplementary_nodes['id'] == nodeKK_id, 'tk'].values[0]
                dfXL.loc[i, 'nodeKK'] = tk_kk

            # Add the pipe
            tk_pipe=s3s.AddNewPipe("-1", tk_ki, tk_kk, dfXL.loc[i, 'geometry'].length, 'LINESTRING (120 76, 500 300, 620 480)', str(dfXL.loc[i, 'MATERIAL']), str(dfXL.loc[i, 'DN']), 1.5, f'ID{i}', f'Pipe {i}', int(dfXL.loc[i, 'KVR'])) # Change to proper linstring with crs
            dfXL.loc[i, 'tk']=tk_pipe

        return dfXL, supplementary_nodes, node_counter

    dfPipes['KVR'] = dfPipes['KVR'].astype(str).str.strip()

    dfVL = dfPipes[dfPipes['KVR'] == '1'].reset_index(drop=True)
    dfRL = dfPipes[dfPipes['KVR'] == '2'].reset_index(drop=True)

    dfVL, dfVL_nodes, node_counter_VL = AddNodesAndPipes(dfVL, 0)
    dfRL, dfRL_nodes, node_counter_RL = AddNodesAndPipes(dfRL, node_counter_VL)
    
    dfPipes = pd.concat([dfVL, dfRL], ignore_index=True)
    dfNodes = pd.concat([dfVL_nodes, dfRL_nodes], ignore_index=True)
    node_counter = node_counter_VL + node_counter_RL

    if '2LROHR' not in dfPipes.columns:
        dfPipes['2LROHR'] = None

    '''# Use Fk instead of Tk
    for idx, row in dfPipes.iterrows():
        # Find the matching row where tk_id equals current row's 2LROHR_id
        match = dfPipes[dfPipes['tk_id'] == row['2LROHR_id']]
        if not match.empty:
            match_idx = match.index[0]
            match_tk = match.at[match_idx, 'tk']
            
            # Update the current row's 2LROHR with the matching row's tk
            dfPipes.at[idx, '2LROHR'] = match_tk
        
            if pd.notna(match_tk):
                s3s.SetValue(match_tk, 'Fk2lrohr', str(match_tk))
    '''

    #Pipe Properties
    
    if 'BAUJAHR' in dfPipes.columns:
        try:
            s3s.SetValue('Baujahr', str(dfPipes.loc[i, 'BAUJAHR']))  # for loop
        except:
            logger.debug("Baujahr not added as property")

    if 'HAL' in dfPipes.columns:
        try:
            s3s.SetValue('Hal', str(dfPipes.loc[i, 'HAL']))  
        except:
            logger.debug("Hal not added as property")

    s3s.EndEditSession()
    s3s.SaveChanges()
    s3s.RefreshViews()

    return dfPipes, dfNodes, node_counter


def Node_on_Node(s3s):
    '''
    '''

def Merge_Nodes(s3s, tk1, tk2):
    '''
    
    '''
        

def Get_Node_Tks_From_Pipe(s3s, pipe_tk):
    '''
    Returns the tk to the From- and To-Node based on the pipe with the given tk.
    '''
    from_node_name = s3s.GetValue(pipe_tk, 'FromNode.Name')[0]
    to_node_name = s3s.GetValue(pipe_tk, 'ToNode.Name')[0]

    from_node_tk = None
    to_node_tk = None

    for node_tk in s3s.GetTksofElementType(ElementType=Interfaces.Sir3SObjectTypes.Node):
        node_name = s3s.GetValue(node_tk, 'Name')[0]
        if node_name == from_node_name:
            from_node_tk = node_tk
        if node_name == to_node_name:
            to_node_tk = node_tk

    return from_node_tk, to_node_tk


def Get_Pipe_Tk_From_Nodes(s3s, fkKI, fkKK, Order):
    '''
    Returns pipe tk correspond to tks of From-Node fkKI and To-Node fkKK. If Order=False, fkKI and fkKK can be interchanged and the pipe is still found.
    '''
    #fix: order param: seems to find pipe both ways even with Order=True
    from_node_name = s3s.GetValue(fkKI, 'Name')[0]
    to_node_name = s3s.GetValue(fkKK, 'Name')[0]
    Order = True

    if Order:
        for pipe_tk in s3s.GetTksofElementType(ElementType=Interfaces.Sir3SObjectTypes.Pipe):
            if (s3s.GetValue(pipe_tk, 'FromNode.Name')[0] == from_node_name and 
                s3s.GetValue(pipe_tk, 'ToNode.Name')[0] == to_node_name):
                pipe_tk_ret = pipe_tk
    else:
        for pipe_tk in s3s.GetTksofElementType(ElementType=Interfaces.Sir3SObjectTypes.Pipe):
            from_name = s3s.GetValue(pipe_tk, 'FromNode.Name')[0]
            to_name = s3s.GetValue(pipe_tk, 'ToNode.Name')[0]
            if ((from_name == from_node_name and to_name == to_node_name) or 
                (from_name == to_node_name and to_name == from_node_name)):
                pipe_tk_ret = pipe_tk

def VL_or_RL(KVR):
    if KVR == 1:
        return 'VL'
    elif KVR == 2:
        return 'RL'
    else:
        return 'Unknown'
