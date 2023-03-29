# Código de lectura de archivo csv y mostrar los datos en la pantalla:

import pandas as pd

datos = pd.read_csv('/home/statick/workspaces/Curso de Data Science en Python/Code/ventas.csv')
print(datos)

# Código para calcular el total de ventas del mes y mostrarlo en la pantalla:

import pandas as pd

datos = pd.read_csv('ventas.csv')
total_ventas = datos['Venta'].sum()
print("El total de ventas del mes es:", total_ventas)

#Código para calcular la venta promedio por día y mostrarlo en la pantalla:

import pandas as pd

datos = pd.read_csv('ventas.csv')
venta_promedio = datos['Venta'].mean()
print("La venta promedio por día es:", venta_promedio)

# Código para calcular el día con mayor venta y mostrarlo en la pantalla:

import pandas as pd

datos = pd.read_csv('ventas.csv')
dia_max_venta = datos.loc[datos['Venta'].idxmax()]['Día']
print("El día con mayor venta fue el día", dia_max_venta)

# Código para calcular el día con menor venta y mostrarlo en la pantalla:

import pandas as pd

datos = pd.read_csv('ventas.csv')
dia_min_venta = datos.loc[datos['Venta'].idxmin()]['Día']
print("El día con menor venta fue el día", dia_min_venta)

# Código para crear un gráfico de barras que muestre las ventas por día:

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('ventas.csv')
ventas_por_dia = datos.groupby('Día').sum()['Venta']
ventas_por_dia.plot(kind='bar')
plt.title('Ventas por día')
plt.xlabel('Día')
plt.ylabel('Ventas')
plt.show()
