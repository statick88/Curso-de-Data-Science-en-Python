Dash es un framework de Python utilizado para crear aplicaciones web interactivas y visualizaciones de datos. Es fácil de usar y permite crear visualizaciones de datos y aplicaciones de forma rápida y sencilla. En este ejemplo, crearemos un tablero sencillo que muestra una gráfica y un filtro de rango para el eje x.

Para empezar, debemos instalar el paquete dash y las bibliotecas adicionales que vamos a necesitar. Para ello, abrimos una terminal y ejecutamos los siguientes comandos:

python

pip install dash
pip install pandas
pip install plotly

Una vez instalados los paquetes necesarios, podemos comenzar a crear nuestro tablero. Empezamos importando las bibliotecas necesarias y leyendo los datos que queremos visualizar. En este caso, utilizaremos un conjunto de datos de ejemplo incluido en la biblioteca plotly.

python

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = px.data.gapminder()

A continuación, creamos la aplicación de Dash. Para ello, creamos una instancia de la clase Dash y le pasamos el argumento __name__ que indica el nombre del módulo actual. Luego, creamos la disposición de la aplicación utilizando los componentes de Dash. En este ejemplo, utilizaremos un componente dcc.Graph para mostrar la gráfica y un componente dcc.RangeSlider para filtrar los datos en el eje x.

python

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Ejemplo de Tablero Dash'),
    dcc.Graph(
        id='grafica',
        figure=px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", log_x=True)
    ),
    dcc.RangeSlider(
        id='rango-x',
        min=df['gdpPercap'].min(),
        max=df['gdpPercap'].max(),
        value=[df['gdpPercap'].min(), df['gdpPercap'].max()],
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

En el código anterior, hemos definido la disposición de la aplicación utilizando un componente html.Div para agrupar los diferentes componentes de la aplicación. Dentro de este componente, hemos creado un componente html.H1 para mostrar un encabezado en la aplicación, un componente dcc.Graph para mostrar la gráfica y un componente dcc.RangeSlider para filtrar los datos en el eje x. El componente dcc.Graph utiliza la biblioteca plotly para crear la gráfica, y el componente dcc.RangeSlider define los límites del filtro y los valores predeterminados.

Finalmente, definimos una función de devolución de llamada para actualizar la gráfica cuando se cambia el valor del filtro. En esta función, utilizamos la biblioteca pandas para filtrar los datos en función del valor del filtro y luego actualizamos la gráfica con los nuevos datos.

python

@app.callback(
    dash.dependencies.Output('grafica', 'figure'),
    [dash.dependencies.Input('rango-x', 'value')])
def actualizar_grafica(rango_x):
    df_filtrado = df[(df['gdpPercap'] >= rango_x[0]) & (df['gdpPercap']
