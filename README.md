```python
import pandas as pd

datos = {
    'Provincia': ['Los Rios', 'Manabi', 'Chimborazo', 'Bolivar', 'Napo'],
    'Ciudad': ['Loja', 'Zamora', 'Santa Elena', 'Santa Elena', 'Loja'],
    'Edad': [39, 19, 57, 65, 60],
    'Ingreso': [4747.327188, 2952.323734, 4604.464213, 3712.333082, 2214.344243],
    'Genero': ['Masculino', 'Masculino', 'Masculino', 'Femenino', 'Otro']
}

df = pd.DataFrame(datos)

df.to_csv('datos2.csv', index=False)
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
      <th>Provincia</th>
      <th>Ciudad</th>
      <th>Edad</th>
      <th>Ingreso</th>
      <th>Genero</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Los Rios</td>
      <td>Loja</td>
      <td>39</td>
      <td>4747.327188</td>
      <td>Masculino</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Manabi</td>
      <td>Zamora</td>
      <td>19</td>
      <td>2952.323734</td>
      <td>Masculino</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Chimborazo</td>
      <td>Santa Elena</td>
      <td>57</td>
      <td>4604.464213</td>
      <td>Masculino</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bolivar</td>
      <td>Santa Elena</td>
      <td>65</td>
      <td>3712.333082</td>
      <td>Femenino</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Napo</td>
      <td>Loja</td>
      <td>60</td>
      <td>2214.344243</td>
      <td>Otro</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd
import numpy as np

# Generar datos aleatorios
np.random.seed(123)
n = 5
provincias = ['Azuay', 'Guayas', 'Pichincha', 'Manabi', 'Esmeraldas']
ciudades = ['Cuenca', 'Guayaquil', 'Quito', 'Portoviejo', 'Esmeraldas']
edades = np.random.randint(18, 80, n)
ingresos = np.random.normal(loc=5000, scale=1000, size=n)
generos = ['Masculino', 'Femenino', 'Masculino', 'Femenino', 'Otro']

# Crear DataFrame y guardar como CSV
datos = {
    'Provincia': provincias,
    'Ciudad': ciudades,
    'Edad': edades,
    'Ingreso': ingresos,
    'Genero': generos
}
df = pd.DataFrame(datos)
df.to_csv('datos3.csv', index=False)
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
      <th>Provincia</th>
      <th>Ciudad</th>
      <th>Edad</th>
      <th>Ingreso</th>
      <th>Genero</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Azuay</td>
      <td>Cuenca</td>
      <td>63</td>
      <td>4926.486320</td>
      <td>Masculino</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Guayas</td>
      <td>Guayaquil</td>
      <td>20</td>
      <td>6814.032774</td>
      <td>Femenino</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Pichincha</td>
      <td>Quito</td>
      <td>46</td>
      <td>4558.002389</td>
      <td>Masculino</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Manabi</td>
      <td>Portoviejo</td>
      <td>52</td>
      <td>6389.511423</td>
      <td>Femenino</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Esmeraldas</td>
      <td>Esmeraldas</td>
      <td>56</td>
      <td>3922.534666</td>
      <td>Otro</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd

# Carga y lectura de datos con Pandas
datos2 = pd.read_csv('datos2.csv')
datos3 = pd.read_csv('datos3.csv')

```


```python
# Conteo de valores únicos en la columna "Genero" para datos2
datos2["Genero"].value_counts()

```




    Masculino    3
    Femenino     1
    Otro         1
    Name: Genero, dtype: int64




```python
# Conteo de valores únicos en la columna "Genero" para datos3
datos3["Genero"].value_counts()

```




    Masculino    2
    Femenino     2
    Otro         1
    Name: Genero, dtype: int64




```python
# Combinación y unión de datos
datos = pd.concat([datos2, datos3])

```


```python
# Verificar si hay valores nulos
datos.isnull().sum()

```




    Provincia    0
    Ciudad       0
    Edad         0
    Ingreso      0
    Genero       0
    dtype: int64




```python
media_por_provincia = datos.groupby('Provincia')['Ingreso'].mean()
print(media_por_provincia)

```

    Provincia
    Azuay         4926.486320
    Bolivar       3712.333082
    Chimborazo    4604.464213
    Esmeraldas    3922.534666
    Guayas        6814.032774
    Los Rios      4747.327188
    Manabi        4670.917579
    Napo          2214.344243
    Pichincha     4558.002389
    Name: Ingreso, dtype: float64



```python
datos = pd.merge(datos2, datos3, how='outer')
```


```python
suma_por_ciudad = datos.groupby('Ciudad')['Ingreso'].sum()
print(suma_por_ciudad)
```

    Ciudad
    Cuenca         4926.486320
    Esmeraldas     3922.534666
    Guayaquil      6814.032774
    Loja           6961.671431
    Portoviejo     6389.511423
    Quito          4558.002389
    Santa Elena    8316.797295
    Zamora         2952.323734
    Name: Ingreso, dtype: float64
