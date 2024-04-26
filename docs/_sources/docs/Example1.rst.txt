Example:
--------

.. code:: ipython3

    try:
        from PT3S import dxAndMxHelperFcts
    except:
        import dxAndMxHelperFcts

.. code:: ipython3

    m=dxAndMxHelperFcts.readDxAndMx('../Examples/Wärmenetz-Planungsbeispiel.db3')

.. code:: ipython3

    dfROHR=m.V3_ROHR

.. code:: ipython3

    dfROHR.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>pk</th>
          <th>fkDE</th>
          <th>rk</th>
          <th>tk</th>
          <th>fkKI</th>
          <th>fkKK</th>
          <th>fkDTRO_ROWD</th>
          <th>fkLTGR</th>
          <th>fkSTRASSE</th>
          <th>L</th>
          <th>...</th>
          <th>('TMIN', 'KNOT~*~*~*~PH', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-13 23:00:00'))_i</th>
          <th>('TMAX', 'KNOT~*~*~*~PH', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-13 23:00:00'))_i</th>
          <th>('STAT', 'KNOT~*~*~*~PH', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00'))_k</th>
          <th>('TIME', 'KNOT~*~*~*~PH', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-12 23:00:00'))_k</th>
          <th>('TMIN', 'KNOT~*~*~*~PH', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-13 23:00:00'))_k</th>
          <th>('TMAX', 'KNOT~*~*~*~PH', Timestamp('2023-02-12 23:00:00'), Timestamp('2023-02-13 23:00:00'))_k</th>
          <th>QMAVAbs</th>
          <th>VAVAbs</th>
          <th>PHRAbs</th>
          <th>JVAbs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>5442010239090746007</td>
          <td>5306805303452857793</td>
          <td>5442010239090746007</td>
          <td>5442010239090746007</td>
          <td>5669301360686511351</td>
          <td>5397948523091900401</td>
          <td>4684070986837856878</td>
          <td>4779752876656844188</td>
          <td>5644881417512616095</td>
          <td>36.429348</td>
          <td>...</td>
          <td>3.501101</td>
          <td>4.030397</td>
          <td>3.2898</td>
          <td>3.290663</td>
          <td>3.2898</td>
          <td>3.791431</td>
          <td>5.284859e+01</td>
          <td>7.528126e-01</td>
          <td>1.041356e-02</td>
          <td>2.858564e-01</td>
        </tr>
        <tr>
          <th>1</th>
          <td>5417154223408487165</td>
          <td>5306805303452857793</td>
          <td>5417154223408487165</td>
          <td>5417154223408487165</td>
          <td>4876992779283362126</td>
          <td>5397948523091900401</td>
          <td>4684070986837856878</td>
          <td>4779752876656844188</td>
          <td>5644881417512616095</td>
          <td>130.216858</td>
          <td>...</td>
          <td>3.31079</td>
          <td>3.802972</td>
          <td>3.2898</td>
          <td>3.290663</td>
          <td>3.2898</td>
          <td>3.791431</td>
          <td>1.539487e+01</td>
          <td>2.192777e-01</td>
          <td>3.643116e-03</td>
          <td>2.797730e-02</td>
        </tr>
        <tr>
          <th>2</th>
          <td>5726827761099671871</td>
          <td>5306805303452857793</td>
          <td>5726827761099671871</td>
          <td>5726827761099671871</td>
          <td>5669301360686511351</td>
          <td>5465373302536437394</td>
          <td>5227809287145441987</td>
          <td>4779752876656844188</td>
          <td>4691593553739008509</td>
          <td>52.374901</td>
          <td>...</td>
          <td>3.501101</td>
          <td>4.030397</td>
          <td>3.516661</td>
          <td>3.517417</td>
          <td>3.516661</td>
          <td>4.045881</td>
          <td>1.197174e-09</td>
          <td>6.124849e-12</td>
          <td>2.341257e-21</td>
          <td>4.470189e-20</td>
        </tr>
        <tr>
          <th>3</th>
          <td>4811306899232458618</td>
          <td>5306805303452857793</td>
          <td>4811306899232458618</td>
          <td>4811306899232458618</td>
          <td>4837439299025862974</td>
          <td>4875518068053211860</td>
          <td>4684070986837856878</td>
          <td>4779752876656844188</td>
          <td>4691593553739008509</td>
          <td>6.559972</td>
          <td>...</td>
          <td>3.179915</td>
          <td>3.875697</td>
          <td>3.204382</td>
          <td>3.205366</td>
          <td>3.204382</td>
          <td>3.891908</td>
          <td>6.796223e+01</td>
          <td>9.672580e-01</td>
          <td>3.036335e-03</td>
          <td>4.628580e-01</td>
        </tr>
        <tr>
          <th>4</th>
          <td>4843836890906700052</td>
          <td>5306805303452857793</td>
          <td>4843836890906700052</td>
          <td>4843836890906700052</td>
          <td>4837439299025862974</td>
          <td>4832729931974744286</td>
          <td>4684070986837856878</td>
          <td>4779752876656844188</td>
          <td>4691593553739008509</td>
          <td>7.759803</td>
          <td>...</td>
          <td>3.179915</td>
          <td>3.875697</td>
          <td>3.206016</td>
          <td>3.206999</td>
          <td>3.206016</td>
          <td>3.910682</td>
          <td>6.522658e+01</td>
          <td>9.274810e-01</td>
          <td>3.312205e-03</td>
          <td>4.268414e-01</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 189 columns</p>
    </div>


