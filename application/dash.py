
#presentación de autores 

import dash
from dash.dependencies import Input, Output, State
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
                           "color": "gray",
                           "background-color": "light"}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            
            html.H5("¿Quienes somos?", 
                    style={'textAlign': 'left',
                           "color": "gray",
                           "background-color": "light"}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
           
 
     

            html.H5("Contacto", 
                    style={'textAlign': 'left',
                           "color": "gray",
                           "background-color": "light"}),

            dbc.Button(html.Span(["", html.H1(className="far fa-envelope", 
                                      style={"background-color": "light","color":"lightgray"} 
                                             )]),
                      style={"background-color": "light"},),
                                  
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
          
 
     

            html.H5("Productos", 
                    style={'textAlign': 'left',
                           "color": "gray",
                           "background-color": "light"}),

#            dbc.Button(html.Span(["", html.H1(className="far fa-envelope", 
#                                      style={"background-color": "light","color":"lightgray"} 
#                                             )]),
#                      style={"background-color": "light"},),
                                  
   #         dbc.Button(
   #             html.Span(["", html.H1(className="far fa-envelope", style={"color": "white",
   #                        "background-color": "#6A1B9A"}),]),),
        ]),
    style={"width": "13rem", 
          "border": "0",
           #"margin-left": "40px",
          "background-color": "light",
           'color':'#BA68C8',
           "height": "1400px",
          })



autores = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Felipe de Alba", 
                    style={'textAlign': 'left',
                           "color": "black",
                          "background-color": "light"}),
            html.P("Doctor en Planeación Urbana por la Universidad de Montreal (2004-2008) con estancias de dos años en el Massachusetts Institute of Technology (MIT) (2009-2011) y de un año en l´École normale supérieure (ENS) de Lyon (Francia) (2012). También fue profesor invitado de tiempo completo “C” en la Universidad Autónoma Metropolitana (Cuajimalpa) (2012- 2014). Es investigador “A” del Centro de Estudios Sociales y de Opinión Publica (CESOP). Ha publicado más de 60 artículos en revistas internacionales y 12 libros", 
                    style={'textAlign': 'left',
                           "font-size": 12,
                           "color": "black",
                          "background-color": "light"}),
 
            html.H5("Winik Morales", 
                    style={'textAlign': 'left',
                           "color": "black",
                          "background-color": "lignt"}),
            html.P("Ingeniero ambiental por el Instituto Tecnológico de Misantla (Veracruz), ha colaborado en varias publicaciones anteriores tanto del CESOP como de la Cámara de Diputados. Actualmente es consultor ambiental", 
                    style={'textAlign': 'left',
                           "color": "black",
                           "font-size": 12,
                          "background-color": "light"}),

            html.H5("Aeelen Miranda", 
                    style={'textAlign': 'left',
                           "color": "black",
                          "background-color": "light"}),
            html.P("Especialista en Sistemas de Información Geográfica (SIG) con licenciatura en Estudios Socio territoriales por la Universidad Autónoma Metropolitana (UAM Cuajimalpa). Se ha desarrollado principalmente en consultoría, donde haelaborado estudios de impacto en mercados", 
                    style={'textAlign': 'left',
                           "color": "black",
                           "font-size": 12,
                          "background-color": "info"}),
            
            html.H5("Josefina Pérez Espino", 
                    style={'textAlign': 'left',
                           "color": "black",
                          "background-color": "light"}),
            html.P("Doctora en Geografía Humana por la Universidad de Sussex (2003-2007) y Maestra en Relaciones Internacionales por la Universidad de San Diego (1993-1996) con estancia de investigación en la Universidad de Turín (2017). Profesora de tiempo completo en la Universidad Pedagógica Nacional (UPN), Unidad Tijuana (de 2017 a la fecha) donde es coordinadora de Posgrado (2020 a la fecha). ha publicado artículos en revistas nacionales e internacionales y en 5 libros, además de participación y coordinación en proyectos de investigación a nivel nacional e internacional. Fundadora y miembros de RECFronteras", 
                    style={'textAlign': 'left',
                           "color": "black",
                           "font-size": 12,
                          "background-color": "info"}),

                        
            html.H5("Elena Hernández Palomino", 
                    style={'textAlign': 'left',
                           "color": "black",
                          "background-color": "light"}),
            html.P("Es Maestra en Planeación Espacial por el CentroGeo. Experta en SIG y en investigación para la argumentación de proyectos y experimentos de innovación social. Ha coordinado proyectos de publicidad y mercadotécnia, tanto para la iniciativa pública como la privada", 
                    style={'textAlign': 'left',
                           "color": "black",
                           "font-size": 12,
                          "background-color": "info"}),
            
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Hr(),
            html.H5("Productos interactivos", 
                    style={'textAlign': 'left',
                           "color": "black",
                          "background-color": "light"}),
            
             dbc.Nav(
            [
                dbc.NavLink("Contagios y decesos por COVID-19 ", href="https://camaradiputados.herokuapp.com/", active="exact"),
                dbc.NavLink("Feminicidios", href="https://camaradiputados.herokuapp.com/", active="exact"),
                dbc.NavLink("Violencia familiar", href="https://violenciafamiliar.herokuapp.com/", active="exact"),
                dbc.NavLink("Violaciones", href="https://violacion.herokuapp.com/", active="exact"),
                dbc.NavLink("Abuso sexual", href="https://abusosexual.herokuapp.com/", active="exact"),
                #dbc.NavLink("Dashboard sobre el proceso de vacunación (utilizado por la SRE)", href="https://vacunassre.herokuapp.com/", active="exact"),
                dbc.NavLink("Metrópolis mexicanas en 2020", href="https://plataformacenso2020.herokuapp.com/", active="exact"),
            ],
                
           # vertical=True,
            #pills=True,
        ),
           html.Br(),
            html.H5("Análisis estratégicos", 
                    style={'textAlign': 'left',
                           "color": "black",
                          "background-color": "light"}),
             dbc.Nav(
            [
                dbc.NavLink("¿Cómo se vive en la metrópolis? Propuesta analítica ", href="https://www.researchgate.net/publication/352064996_2021_Como_se_vive_en_la_metropolis_Propuesta_analitica (2021)", active="exact"),
                dbc.NavLink("Decesos por COVID-19. Evidencia estadística de sus ritmos y temporalidades", href="https://www.researchgate.net/publication/352106923_Decesos_por_COVID-19. Evidencia estadistica de sus ritmos y temporalidades (2020)", active="exact"),
                dbc.NavLink("Perfil socioeconómico de 50 municipios metropolitanos con más contagiosshboard sobre el delito de violaciones", href="https://www.researchgate.net/publication/352106838_Perfil_socioeconomico_de_50_municipios_metropolitanos_con_mas_contagios", active="exact"),
                dbc.NavLink("Ranking Municipal de los Delitos en México (2015-2019). Ejercicios de visualización", href="https://www.researchgate.net/publication/352106653_Ranking_Municipal_de_los_Delitos_en_Mexico_2015-2019_Ejercicios_de_visualizacion", active="exact"),
                dbc.NavLink("Ranking Estatal de los Delitos en México (2015-2019). Ejercicios de visualización", href="https://www.researchgate.net/publication/352106653_Ranking_Municipal_de_los_Delitos_en_Mexico_2015-2019_Ejercicios_de_visualizacion", active="exact"),
                dbc.NavLink("Metrópolis mexicanas en cifras. Propuesta visual de la Estadística Metropolitana", href="https://www.researchgate.net/publication/352227273_Metropolis_mexicanas_en_cifras", active="exact"),
                dbc.NavLink("Municipios Mexicanos en Cifras. Propuesta Visual de la Estadística Municipal", href="https://www.researchgate.net/publication/352136229_2019_Municipios_mexicanos_en_cifras", active="exact"),
               # dbc.NavLink("Dashboard sobre las metrópolis en 2020", href="https://plataformacenso2020.herokuapp.com/", active="exact"),
            ],
                
                
                
           # vertical=True,
            #pills=True,
        ),  

        ]),
    
    style={"width": "58rem", 
          "border": "0",
          "margin-left": "-4px",
          "background-color": "light",
           "justify": "justify"
          })


laboratorio = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Laboratorio para el Aprendizaje de la Innovación", 
                    style={'textAlign': 'left',
                           "color": "gray",
                          "background-color": "light"}),
            html.P("Somos una iniciativa para integrar procesos de Machine Learning (aprendizaje automatizado) e Inteligencia Artificial a las decisiones ejecutivas y de política pública. Colaboramos con cualquier entidad o institucion por el placer de innovar", 
                    style={'textAlign': 'left',
                           "color": "gray",
                          "background-color": "info"}),
 


            
        ]),
    
    style={"width": "48rem", 
          "border": "0",
          "margin-left": "-4px",
          "background-color": "info",
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
               }, sm={  "offset": 1, })
     ],  no_gutters= True, justify= "start",
     className="blockquote"),

 
    

    dbc.Row([
        dbc.Col(dbc.Card(laboratorio), #sm={  "offset": 1, }),#Variables Vivienda
               style={'margin-top': '-1400px',
                      'margin-left': '240px', 
                     }),
    
        dbc.Col(dbc.Card(autores), #sm={  "offset": 1, }),#Variables Vivienda
               style={'margin-top': '-1250px',       #arriba
                      'margin-left': '255px', 
               }, sm={  "offset": 1, })
     ], className="blockquote"),
            
    
      ])  

#
#
############################################################################

#App

app.layout = html.Div([body, 
                       #collapse, fade
                      ])


if __name__ == '__main__':
    app.run_server(use_reloader = False)
    
