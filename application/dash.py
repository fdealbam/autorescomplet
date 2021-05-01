


import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os
yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")

pobsindh = 7804407



presentation = dbc.Card(
    dbc.CardBody(
        [
            html.Br(),
            html.Br(),

            html.H5("¿Qué somos?", 
                    style={'textAlign': 'left',
                           "color": "white",
                           "background-color": "#6A1B9A"}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            
            html.H5("¿Quienes somos?", 
                    style={'textAlign': 'left',
                           "color": "white",
                           "background-color": "#6A1B9A"}),
            html.Br(),
            html.Br(),
          
            html.Br(),
            html.Br(),
            html.Br(),

            html.H5("Contacto", 
                    style={'textAlign': 'left',
                           "color": "white",
                           "background-color": "#6A1B9A"}),

            dbc.Button(html.Span(["", html.H1(className="far fa-envelope", 
                                      style={"background-color": "#6A1B9A","color":"white"} 
                                             )]),
                      style={"background-color": "#6A1B9A"},),
                                  
            
   #         dbc.Button(
   #             html.Span(["", html.H1(className="far fa-envelope", style={"color": "white",
   #                        "background-color": "#6A1B9A"}),]),),
        ]),
    style={"width": "13rem", 
          "border": "0",
           #"margin-left": "40px",
          "background-color": "#6A1B9A",
           'color':'#BA68C8',
           "height": "550px",
          })



autores = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Felipe de Alba", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.H6("Doctor en Planeación Urbana por la Universidad de Montreal (2004-2008) con estancias de dos años en el Massachusetts Institute of Technology (MIT) (2009-2011) y de un año en l´École normale supérieure (ENS) de Lyon (Francia) (2012). También fue profesor invitado de tiempo completo “C” en la Universidad Autónoma Metropolitana (Cuajimalpa) (2012- 2014). Es investigador “A” del Centro de Estudios Sociales y de Opinión Publica (CESOP). Ha publicado más de 60 artículos en revistas internacionales y 12 libros", 
                    style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "lowercase",
                          "background-color": "orange"}),
 
            html.H5("Winik Morales", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.H6("Es ingeniero ambiental por el Instituto Tecnológico de Misantla (Veracruz), ha colaborado en varias publicaciones anteriores tanto del CESOP como de la Cámara de Diputados. Actualmente es consultor ambiental", 
                    style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "lowercase",
                          "background-color": "orange"}),

            html.H5("Aeleen Miranda", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.H6("Es especialista en Sistemas de Información Geográfica (SIG) con licenciatura en Estudios Socio territoriales por la Universidad Autónoma Metropolitana (UAM Cuajimalpa). Se ha desarrollado principalmente en consultoría, donde haelaborado estudios de impacto en mercados", 
                    style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "lowercase",
                          "background-color": "orange"}),

            
        ]),
    
    style={"width": "48rem", 
          "border": "0",
          "margin-left": "-4px",
          "background-color": "orange",
           "justify": "justify"
          })


laboratorio = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Laboratorio para la Innovación Estadística", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.H6("Somos una iniciativa para la integrar procesos de Machine Learning (aprendizaje automatizado) e Inteligencia Artificial e Inteligencia Artificial a las decisiones ejecutivas y de política pública. Colaboramos con cualquier entidad o institucion por el placer de innovar", 
                    style={'textAlign': 'left',
                           "color": "black",
                           'text-transform': "lowercase",
                          "background-color": "orange"}),
 


            
        ]),
    
    style={"width": "48rem", 
          "border": "0",
          "margin-left": "-4px",
          "background-color": "orange",
           "justify": "justify"
          })





########################################################################
# A P P 
########################################################################



# identificadores
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                LUX, FONT_AWESOME], server=server)

body = html.Div([
    
    dbc.Row([
        #dbc.Col(dbc.Card(card_economia), sm={  "offset": 1, }),#Variables Vivienda
        dbc.Col(dbc.Card(presentation),                      #población total
               style={'margin-top': '40px',       #arriba
                      'margin-left': '50px',
                   
                   "color":"#BA68C8"
               #       'width': '479px',
               #       'height': '100%',
               }, sm={  "offset": 1, })
     ],  no_gutters= True, justify= "start",
     className="blockquote"),

 
    

    dbc.Row([
        dbc.Col(dbc.Card(laboratorio), #sm={  "offset": 1, }),#Variables Vivienda
               style={'margin-top': '-530px',
                      'margin-left': '240px', 
               #       'width': '479px',
               #       'height': '100%',
#               }, sm={  "offset": 1, 
                     }),
     #], className="blockquote"),
    
        dbc.Col(dbc.Card(autores), #sm={  "offset": 1, }),#Variables Vivienda
        #dbc.Col(dbc.Card(card2),                      #población total
               style={'margin-top': '-380px',       #arriba
                      'margin-left': '255px', 
               #       'width': '479px',
               #       'height': '100%',
               }, sm={  "offset": 1, })
     ], className="blockquote"),
            
    
      ])  

app.layout = html.Div([body])
#app.layout = html.Div(children=[html.Img(className='icon')])

if __name__ == '__main__':
    app.run_server(use_reloader = False)
    

