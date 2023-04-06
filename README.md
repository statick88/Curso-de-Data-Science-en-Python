Para trabajar con el archivo datos.xlsx en un Jupyter Notebook necesitarás tener instaladas las siguientes librerías: pandas y numpy. Para instalarlas, puedes usar el siguiente comando:


```python
!pip install pandas 
!pip install numpy
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: pandas in /home/statick/.local/lib/python3.11/site-packages (1.5.3)
    Requirement already satisfied: numpy in /home/statick/.local/lib/python3.11/site-packages (1.24.2)
    Requirement already satisfied: python-dateutil>=2.8.1 in /usr/lib/python3.11/site-packages (from pandas) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /home/statick/.local/lib/python3.11/site-packages (from pandas) (2023.2)
    Requirement already satisfied: six>=1.5 in /usr/lib/python3.11/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)


Una vez instaladas, puedes empezar a trabajar con el archivo datos.xlsx siguiendo los siguientes pasos:

    Importar las librerías pandas y numpy:


```python
import pandas as pd
import numpy as np
```

    Cargar el archivo datos.xlsx en un objeto DataFrame de pandas:


```python
df = pd.read_excel('datos.xlsx')
```

    Verificar que los datos se hayan cargado correctamente:


```python
df.head()
```




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
      <th>FECHA</th>
      <th>ANIO</th>
      <th>MES</th>
      <th>CODIGO CLIENTE</th>
      <th>CANAL</th>
      <th>COD_ITEM</th>
      <th>NOMBRE_PRODUCTO</th>
      <th>NOMBRE_CATEGORIA</th>
      <th>NOMBRE_TIPO_NEGOCIO</th>
      <th>COD_LOCAL</th>
      <th>NOMBRE_LOCAL</th>
      <th>NOMBRE_PROVINCIA</th>
      <th>NOMBRE_CIUDAD</th>
      <th>NÚMERO DE TRANSACCIÓN</th>
      <th>VENTA_NETA</th>
      <th>MARGEN</th>
      <th>CANTIDAD</th>
      <th>COD FORMA DE PAGO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-10-08</td>
      <td>2021</td>
      <td>10</td>
      <td>7767359</td>
      <td>PDV</td>
      <td>50785</td>
      <td>CEPILLOS B&amp;C</td>
      <td>IMPLEMENTOS DE CABELLO B&amp;C</td>
      <td>B&amp;C</td>
      <td>791</td>
      <td>FYBECA MALL DE LOS ANDES</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>3810852</td>
      <td>7</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2022-01-21</td>
      <td>2022</td>
      <td>1</td>
      <td>8522244</td>
      <td>PDV</td>
      <td>30253</td>
      <td>DELINEADOR OJOS ESSENCE</td>
      <td>COSMETICO UÑAS</td>
      <td>B&amp;CP</td>
      <td>95</td>
      <td>FYBECA LOS MANGOS</td>
      <td>MANABÍ</td>
      <td>PORTOVIEJO</td>
      <td>5962659</td>
      <td>9</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-12-30</td>
      <td>2021</td>
      <td>12</td>
      <td>7482712</td>
      <td>PDV</td>
      <td>103961</td>
      <td>HANUTA B&amp;C</td>
      <td>COLACIONES Y SNACKS</td>
      <td>B&amp;C</td>
      <td>1271</td>
      <td>FYBECA SAN LUIS SHOPPING</td>
      <td>PICHINCHA</td>
      <td>QUITO</td>
      <td>3485885</td>
      <td>11</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2022-09-15</td>
      <td>2022</td>
      <td>9</td>
      <td>6005545</td>
      <td>PDV</td>
      <td>92243</td>
      <td>PAPAS PRINGLES B&amp;C.</td>
      <td>CONFITES</td>
      <td>B&amp;C</td>
      <td>71840</td>
      <td>FYBECA LOS FRESNOS</td>
      <td>PICHINCHA</td>
      <td>QUITO</td>
      <td>4209849</td>
      <td>18</td>
      <td>2</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2022-07-20</td>
      <td>2022</td>
      <td>7</td>
      <td>6627039</td>
      <td>PDV</td>
      <td>5757</td>
      <td>VITAMIN CHOICE ANTIOXIDANTE</td>
      <td>SUPLEMENTOS</td>
      <td>B&amp;C</td>
      <td>1901</td>
      <td>FYBECA SCALA</td>
      <td>PICHINCHA</td>
      <td>QUITO</td>
      <td>6412586</td>
      <td>7</td>
      <td>2</td>
      <td>1</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



Realizar operaciones de data wrangling y munging con las funciones y métodos de pandas y numpy. Por ejemplo:

Seleccionar sólo las columnas de interés:


```python
df = df[['FECHA', 'ANIO', 'MES', 'CODIGO CLIENTE', 'CANAL', 'COD_ITEM', 'NOMBRE_PRODUCTO', 'NOMBRE_CATEGORIA', 'NOMBRE_TIPO_NEGOCIO', 'COD_LOCAL', 'NOMBRE_LOCAL', 'NOMBRE_PROVINCIA', 'NOMBRE_CIUDAD', 'NÚMERO DE TRANSACCIÓN', 'VENTA_NETA', 'MARGEN', 'CANTIDAD', 'COD FORMA DE PAGO']]
```

    Eliminar filas con valores faltantes:


```python
df = df.dropna()
```

    Cambiar el tipo de datos de una columna:


```python
df['FECHA'] = pd.to_datetime(df['FECHA'])
```

    Agrupar los datos por una o varias columnas y realizar operaciones estadísticas:


```python
df.groupby('NOMBRE_CATEGORIA')['VENTA_NETA'].sum()
```




    NOMBRE_CATEGORIA
    ABARROTES                        4463
    ACCESORIOS                       1372
    ACCESORIOS CAPILARES             1307
    ACCESORIOS FIESTA                 740
    ACCESORIOS GASTRICAS             1060
                                    ...  
    VENDAS                            250
    VITAMINAS                        2466
    VITAMINAS BIENESTAR               198
    VITAMINAS PREVENCION RESFRIO    11456
    WELLNESS                         3825
    Name: VENTA_NETA, Length: 227, dtype: int64



    Filtrar los datos por una o varias condiciones:


```python
df[df['NOMBRE_PROVINCIA'] == 'TUNGURAHUA']
```




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
      <th>FECHA</th>
      <th>ANIO</th>
      <th>MES</th>
      <th>CODIGO CLIENTE</th>
      <th>CANAL</th>
      <th>COD_ITEM</th>
      <th>NOMBRE_PRODUCTO</th>
      <th>NOMBRE_CATEGORIA</th>
      <th>NOMBRE_TIPO_NEGOCIO</th>
      <th>COD_LOCAL</th>
      <th>NOMBRE_LOCAL</th>
      <th>NOMBRE_PROVINCIA</th>
      <th>NOMBRE_CIUDAD</th>
      <th>NÚMERO DE TRANSACCIÓN</th>
      <th>VENTA_NETA</th>
      <th>MARGEN</th>
      <th>CANTIDAD</th>
      <th>COD FORMA DE PAGO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-10-08</td>
      <td>2021</td>
      <td>10</td>
      <td>7767359</td>
      <td>PDV</td>
      <td>50785</td>
      <td>CEPILLOS B&amp;C</td>
      <td>IMPLEMENTOS DE CABELLO B&amp;C</td>
      <td>B&amp;C</td>
      <td>791</td>
      <td>FYBECA MALL DE LOS ANDES</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>3810852</td>
      <td>7</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2022-03-31</td>
      <td>2022</td>
      <td>3</td>
      <td>5137672</td>
      <td>PDV</td>
      <td>1881</td>
      <td>ANALGAN</td>
      <td>ANTICONVULSIVANTES</td>
      <td>FARMA</td>
      <td>72080</td>
      <td>FYBECA GUAYTAMBOS</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>2744497</td>
      <td>10</td>
      <td>3</td>
      <td>12</td>
      <td>1</td>
    </tr>
    <tr>
      <th>128</th>
      <td>2022-11-07</td>
      <td>2022</td>
      <td>11</td>
      <td>6581213</td>
      <td>PDV</td>
      <td>81281</td>
      <td>HIDRATANTES GATORADE B&amp;C.</td>
      <td>BEBIDAS ISOTONICAS</td>
      <td>B&amp;C</td>
      <td>72047</td>
      <td>FYBECA GALES</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>6304691</td>
      <td>19</td>
      <td>2</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>131</th>
      <td>2021-09-13</td>
      <td>2021</td>
      <td>9</td>
      <td>6043717</td>
      <td>PDV</td>
      <td>8894</td>
      <td>CUPON VIRTUAL CLIENTE.</td>
      <td>CLIENTES - OBSEQUIOS NO MED</td>
      <td>B&amp;CP</td>
      <td>731</td>
      <td>FYBECA FICOA</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>3936918</td>
      <td>7</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>192</th>
      <td>2021-07-14</td>
      <td>2021</td>
      <td>7</td>
      <td>2454177</td>
      <td>PDV</td>
      <td>18280</td>
      <td>CANDISNEY B&amp;C</td>
      <td>CONFITES</td>
      <td>B&amp;C</td>
      <td>791</td>
      <td>FYBECA MALL DE LOS ANDES</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>3250810</td>
      <td>10</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>49790</th>
      <td>2021-09-16</td>
      <td>2021</td>
      <td>9</td>
      <td>7900526</td>
      <td>PDV</td>
      <td>92851</td>
      <td>OMEPRAZOL (/LA SANTE)</td>
      <td>ANTIULCEROSOS</td>
      <td>FARMA</td>
      <td>791</td>
      <td>FYBECA MALL DE LOS ANDES</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>352010</td>
      <td>10</td>
      <td>4</td>
      <td>32</td>
      <td>5</td>
    </tr>
    <tr>
      <th>49845</th>
      <td>2023-03-19</td>
      <td>2023</td>
      <td>3</td>
      <td>5976410</td>
      <td>PDV</td>
      <td>49389</td>
      <td>DICLOFENACO ( MEDIGENER))</td>
      <td>ANTIINFLAMATORIOS</td>
      <td>FARMA</td>
      <td>791</td>
      <td>FYBECA MALL DE LOS ANDES</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>4505822</td>
      <td>15</td>
      <td>2</td>
      <td>10</td>
      <td>5</td>
    </tr>
    <tr>
      <th>49863</th>
      <td>2022-09-03</td>
      <td>2022</td>
      <td>9</td>
      <td>3118689</td>
      <td>PDV</td>
      <td>19229</td>
      <td>PROFINAL</td>
      <td>ANTIINFLAMATORIOS</td>
      <td>FARMA</td>
      <td>791</td>
      <td>FYBECA MALL DE LOS ANDES</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>4511214</td>
      <td>12</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>49979</th>
      <td>2022-01-07</td>
      <td>2022</td>
      <td>1</td>
      <td>1996633</td>
      <td>PDV</td>
      <td>29867</td>
      <td>ESOZ</td>
      <td>ANTIULCEROSOS</td>
      <td>FARMA</td>
      <td>72154</td>
      <td>FYBECA PATATE</td>
      <td>TUNGURAHUA</td>
      <td>PATATE</td>
      <td>4076983</td>
      <td>12</td>
      <td>3</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>49994</th>
      <td>2022-02-25</td>
      <td>2022</td>
      <td>2</td>
      <td>2275487</td>
      <td>PDV</td>
      <td>96359</td>
      <td>ENDOCARE</td>
      <td>DERMOCOSMETICA</td>
      <td>B&amp;CP</td>
      <td>72080</td>
      <td>FYBECA GUAYTAMBOS</td>
      <td>TUNGURAHUA</td>
      <td>AMBATO</td>
      <td>3215801</td>
      <td>14</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>1132 rows × 18 columns</p>
</div>
