Para trabajar con el archivo datos.xlsx en un Jupyter Notebook necesitarás tener instaladas las siguientes librerías: pandas y numpy. Para instalarlas, puedes usar el siguiente comando:

!pip install pandas 

!pip install numpy

Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pandas in /home/statick/.local/lib/python3.11/site-packages (1.5.3)
Requirement already satisfied: numpy in /home/statick/.local/lib/python3.11/site-packages (1.24.2)
Requirement already satisfied: python-dateutil>=2.8.1 in /usr/lib/python3.11/site-packages (from pandas) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /home/statick/.local/lib/python3.11/site-packages (from pandas) (2023.2)
Requirement already satisfied: six>=1.5 in /usr/lib/python3.11/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)

Una vez instaladas, puedes empezar a trabajar con el archivo datos.xlsx siguiendo los siguientes pasos:

Importar las librerías pandas y numpy:

import pandas as pd

import numpy as np

Cargar el archivo datos.xlsx en un objeto DataFrame de pandas:

df = pd.read_excel('datos.xlsx')

Verificar que los datos se hayan cargado correctamente:

df.head()

	FECHA 	ANIO 	MES 	CODIGO CLIENTE 	CANAL 	COD_ITEM 	NOMBRE_PRODUCTO 	NOMBRE_CATEGORIA 	NOMBRE_TIPO_NEGOCIO 	COD_LOCAL 	NOMBRE_LOCAL 	NOMBRE_PROVINCIA 	NOMBRE_CIUDAD 	NÚMERO DE TRANSACCIÓN 	VENTA_NETA 	MARGEN 	CANTIDAD 	COD FORMA DE PAGO
0 	2021-10-08 	2021 	10 	7767359 	PDV 	50785 	CEPILLOS B&C 	IMPLEMENTOS DE CABELLO B&C 	B&C 	791 	FYBECA MALL DE LOS ANDES 	TUNGURAHUA 	AMBATO 	3810852 	7 	2 	1 	1
1 	2022-01-21 	2022 	1 	8522244 	PDV 	30253 	DELINEADOR OJOS ESSENCE 	COSMETICO UÑAS 	B&CP 	95 	FYBECA LOS MANGOS 	MANABÍ 	PORTOVIEJO 	5962659 	9 	2 	1 	1
2 	2021-12-30 	2021 	12 	7482712 	PDV 	103961 	HANUTA B&C 	COLACIONES Y SNACKS 	B&C 	1271 	FYBECA SAN LUIS SHOPPING 	PICHINCHA 	QUITO 	3485885 	11 	2 	2 	3
3 	2022-09-15 	2022 	9 	6005545 	PDV 	92243 	PAPAS PRINGLES B&C. 	CONFITES 	B&C 	71840 	FYBECA LOS FRESNOS 	PICHINCHA 	QUITO 	4209849 	18 	2 	1 	5
4 	2022-07-20 	2022 	7 	6627039 	PDV 	5757 	VITAMIN CHOICE ANTIOXIDANTE 	SUPLEMENTOS 	B&C 	1901 	FYBECA SCALA 	PICHINCHA 	QUITO 	6412586 	7 	2 	1 	5

Realizar operaciones de data wrangling y munging con las funciones y métodos de pandas y numpy. Por ejemplo:

Seleccionar sólo las columnas de interés:

df = df[['FECHA', 'ANIO', 'MES', 'CODIGO CLIENTE', 'CANAL', 'COD_ITEM', 'NOMBRE_PRODUCTO', 'NOMBRE_CATEGORIA', 'NOMBRE_TIPO_NEGOCIO', 'COD_LOCAL', 'NOMBRE_LOCAL', 'NOMBRE_PROVINCIA', 'NOMBRE_CIUDAD', 'NÚMERO DE TRANSACCIÓN', 'VENTA_NETA', 'MARGEN', 'CANTIDAD', 'COD FORMA DE PAGO']]

Eliminar filas con valores faltantes:

df = df.dropna()

Cambiar el tipo de datos de una columna:

df['FECHA'] = pd.to_datetime(df['FECHA'])

Agrupar los datos por una o varias columnas y realizar operaciones estadísticas:

df.groupby('NOMBRE_CATEGORIA')['VENTA_NETA'].sum()

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

df[df['NOMBRE_PROVINCIA'] == 'TUNGURAHUA']

	FECHA 	ANIO 	MES 	CODIGO CLIENTE 	CANAL 	COD_ITEM 	NOMBRE_PRODUCTO 	NOMBRE_CATEGORIA 	NOMBRE_TIPO_NEGOCIO 	COD_LOCAL 	NOMBRE_LOCAL 	NOMBRE_PROVINCIA 	NOMBRE_CIUDAD 	NÚMERO DE TRANSACCIÓN 	VENTA_NETA 	MARGEN 	CANTIDAD 	COD FORMA DE PAGO
0 	2021-10-08 	2021 	10 	7767359 	PDV 	50785 	CEPILLOS B&C 	IMPLEMENTOS DE CABELLO B&C 	B&C 	791 	FYBECA MALL DE LOS ANDES 	TUNGURAHUA 	AMBATO 	3810852 	7 	2 	1 	1
66 	2022-03-31 	2022 	3 	5137672 	PDV 	1881 	ANALGAN 	ANTICONVULSIVANTES 	FARMA 	72080 	FYBECA GUAYTAMBOS 	TUNGURAHUA 	AMBATO 	2744497 	10 	3 	12 	1
128 	2022-11-07 	2022 	11 	6581213 	PDV 	81281 	HIDRATANTES GATORADE B&C. 	BEBIDAS ISOTONICAS 	B&C 	72047 	FYBECA GALES 	TUNGURAHUA 	AMBATO 	6304691 	19 	2 	2 	5
131 	2021-09-13 	2021 	9 	6043717 	PDV 	8894 	CUPON VIRTUAL CLIENTE. 	CLIENTES - OBSEQUIOS NO MED 	B&CP 	731 	FYBECA FICOA 	TUNGURAHUA 	AMBATO 	3936918 	7 	4 	1 	4
192 	2021-07-14 	2021 	7 	2454177 	PDV 	18280 	CANDISNEY B&C 	CONFITES 	B&C 	791 	FYBECA MALL DE LOS ANDES 	TUNGURAHUA 	AMBATO 	3250810 	10 	2 	1 	4
... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	...
49790 	2021-09-16 	2021 	9 	7900526 	PDV 	92851 	OMEPRAZOL (/LA SANTE) 	ANTIULCEROSOS 	FARMA 	791 	FYBECA MALL DE LOS ANDES 	TUNGURAHUA 	AMBATO 	352010 	10 	4 	32 	5
49845 	2023-03-19 	2023 	3 	5976410 	PDV 	49389 	DICLOFENACO ( MEDIGENER)) 	ANTIINFLAMATORIOS 	FARMA 	791 	FYBECA MALL DE LOS ANDES 	TUNGURAHUA 	AMBATO 	4505822 	15 	2 	10 	5
49863 	2022-09-03 	2022 	9 	3118689 	PDV 	19229 	PROFINAL 	ANTIINFLAMATORIOS 	FARMA 	791 	FYBECA MALL DE LOS ANDES 	TUNGURAHUA 	AMBATO 	4511214 	12 	4 	4 	1
49979 	2022-01-07 	2022 	1 	1996633 	PDV 	29867 	ESOZ 	ANTIULCEROSOS 	FARMA 	72154 	FYBECA PATATE 	TUNGURAHUA 	PATATE 	4076983 	12 	3 	1 	4
49994 	2022-02-25 	2022 	2 	2275487 	PDV 	96359 	ENDOCARE 	DERMOCOSMETICA 	B&CP 	72080 	FYBECA GUAYTAMBOS 	TUNGURAHUA 	AMBATO 	3215801 	14 	2 	1 	1

1132 rows × 18 columns
