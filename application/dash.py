import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import flask
import os
yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")

pobsindh = 7804407

##########################################################################
#Tabla Seccion 3. Variables de vivienda
##########################################################################



## Tabla de variables
row1v = html.Tr([dbc.Alert("Con sanitario y con agua", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("94%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                        })])


row2v = html.Tr([dbc.Alert("Viviendas habitadas", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("94%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                        })])

row3v = html.Tr([dbc.Alert("Con luz eléctrica",  color="#E0E0E0"),
                html.Td("5,162,569"),  
                dbc.Alert("99%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                              })])

row4v = html.Tr([dbc.Alert("Con agua entubada", color="#E0E0E0"), 
                html.Td("4,973,950"),  
                dbc.Alert("92%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                              })])

row5v = html.Tr([dbc.Alert("Con drenaje",color="#E0E0E0"), 
                html.Td("5,115,669"),  
                dbc.Alert("96%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                              })])

row6v = html.Tr([dbc.Alert("Con sanitario", color="#E0E0E0"), 
                html.Td("5,132,288"),  
                dbc.Alert("97%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                              })])

table_bodyv = ([row1v, row2v, row3v, row4v,row5v, row6v])

##########################################################################
#Tabla. Variables de DISCAPACIDAD
##########################################################################

row1d = html.Tr([dbc.Alert("Poblacion con discapacidad", color="#E0E0E0",), 
                html.Td("172,575"),
                dbc.Alert("4%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#BA68C8",       
                        })])


row2d = html.Tr([dbc.Alert("Poblacion con discapacidad derechohabiente", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#BA68C8",       
                        })])

table_bodyd = ([row1d, row2d,])

##########################################################################
#Tabla Variables de EDUCACION
##########################################################################


row1edu = html.Tr([dbc.Alert("De 15 años y más alfabeta", color="#E0E0E0",), 
                html.Td("172,575"),
                dbc.Alert("4%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#81C784",       
                        })])


row2edu = html.Tr([dbc.Alert("De 15 años y más con educación básica completa", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#81C784",       
                        })])

row3edu = html.Tr([dbc.Alert("De 15 años y más analfabeta", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#81C784",       
                        })])

table_bodyedu = ([row1edu, row2edu, row3edu])

##########################################################################
#Tabla. Variables de HOGARES CENSALES
##########################################################################

row1hc = html.Tr([dbc.Alert("Población en hogares con jefa(e) de 30 a 59 años", color="#E0E0E0",), 
                html.Td("172,575"),
                dbc.Alert("4%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])


row2hc = html.Tr([dbc.Alert("Población en hogares con jefa(e) de 60 años y más", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])

row3hc = html.Tr([dbc.Alert("Población en hogares con jefatura femenina", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])

row4hc = html.Tr([dbc.Alert("Población en hogares con jefa e hijos menores de 18 años", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])

table_bodyhc = ([row1hc, row2hc, row3hc, row4hc])
########################################################################
# A P P 
########################################################################



# identificadores

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                LUX, FONT_AWESOME], server=server)

body = html.Div([
     html.Br(),
       html.Br(),
       html.Br(),
    dbc.Row(
           [
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true",
                        ),width ={ "size": 1,  "offset": 1,
                                  "height": "5px"}),
               dbc.Col(html.H4("Reporte estadístico básico de ",
                        style={'offset' : 1, "size": 6,
                              "font-size": "15px",
                              "color": "grey",
                               "height": "5px",
                              'textAlign': 'center',
                               #"font-weight": 'bold',
                               "font-family": "Montserrat"
                              })),
                      ], justify= "center"),               
    dbc.Row(
           [
               dbc.Col(html.H1("Zonas Metropolitanas",
                        style={ "size": 6, "offset":2,
                              "font-size": "35px",
                               "height": "40px",
                              "color": "dark",
                              'textAlign': 'center',
                               #"font-weight": 'bold',
                               "font-family": "Montserrat",
                              },)),
                      ], justify= "center"),            
    
    #Cintillo 00    
    dbc.Row(
           [
               dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 1,
                      #'textAlign': 'center',
                     }), 
            ], justify= "center"),
    dbc.Row(
           [
               dbc.Col(html.H6("Fuente: Censo 2020, INEGI"),
                        width={'size' : "auto",
                               #"offset":1,
                              'textAlign': 'center',
                               "color": "grey",
}),
            ], justify= "center"),
               
    html.Br(),
    
    html.Br(),
    html.Br(),
    
    
##########################################################################
#Seccion 1. Variables de POBLACION
##########################################################################
    dbc.Row([
        dbc.Col([html.H6("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray", }),
            html.H2("de población", 
                    className="card-subtitle",
                    style={'textAlign': 'left',"color": "black", "font-weight": 'bold'}),
            html.Br(),
            html.Br(),
            html.Br(),
          
            html.P(
                "Sin derechohabiencia "
              "  7,804,407",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                      "height": "1px",}),

            
            
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-male", style={"color": "#E0E0E0"}),]),),
            html.Br(),
            
            html.P("42%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "40px",
                         "font-weight": 'bold',
                        "color": "dark",
                        "height": "1px",}),
           
            #Linea de separación tipo Aeleen
                        #Linea de separación tipo Aeleen
            dbc.Button(
                html.Span([html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),

                          ],style={"align" :"center",
                                   'margin-left': '-30px',
                                   "height": "1px",
                                  }),),
            
            html.P(
                "Primaria incompleta "
              "  3,829,453",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   "height": "1px",}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-user-graduate", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-user-graduate", style={"color": "#E0E0E0"}),
                          ]),),
            html.P("30%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "40px",
                         "font-weight": 'bold',
                        "height": "1px",}),
            

            #Linea de separación tipo Aeleen
                        #Linea de separación tipo Aeleen
            dbc.Button(
                html.Span([html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),
                           html.H6(className="fas fa-window-minimize", style={"color": "#CFD8DC"}),

                          ],style={"align" :"center",
                                   'margin-left': '-30px',
                                   #'margin-right': '120px',
                                  }),),
            
             html.P(
                "Con discapacidad "
              "  782,953",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   "height": "1px",}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-wheelchair", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),]),),
             html.P("4%", 
                  className="card-text",
                  style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "40px",
                         "height": "1px",
                         "font-weight": 'bold',}),
                    
        ],style={'margin-left': '50px',
                'margin-right': '370px',}),#style ={ 
           # 'margin-left': '30px',
           # 'margin-right': '870px',
           # 'margin-up': '1070px',},



##########################################################################
#Seccion 2. Variables de vivienda
##########################################################################
    
  
        dbc.Col([
            html.H6("Población total", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.H3("20,116,842", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "orange"}),
            html.Br(),
       
            dbc.ButtonGroup(
                html.Span(["", html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),
                               html.H1(className="fas fa-male", style={"background-color": "orange","color":"white"}),]),),
            
        ],style={ #'margin-right': '-10px', 
                  "background-color": "orange",
                # "margin-left": "150px",
                  #"offset": 2,
                  "height": "110px",
                  
                 }),
       ]),
    
    dbc.Row([
        dbc.Col([html.H6("De 18 años y más", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })])],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                   "background-color": "#0097A7",
                                      'margin-top': '-368px',
                                      'margin-left': '700px',
                                      'width': '482px',
                                      'height': '79px',}),
    html.Br(),
        dbc.Row([
        dbc.Col([html.H6("De 18 años y más", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })])],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                   "background-color": "#0097A7",
                                      
                                      'margin-left': '700px',
                                      'width': '482px',
                                      'height': '79px',}),
        html.Br(),
        dbc.Row([
        dbc.Col([html.H6("De 18 años y más", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })])],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                   "background-color": "#0097A7",
                                      
                                      'margin-left': '700px',
                                      'width': '482px',
                                      'height': '79px',}),
        html.Br(),
        dbc.Row([
        dbc.Col([html.H6("De 18 años y más", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })])],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                   "background-color": "#0097A7",
                                      
                                      'margin-left': '700px',
                                      'width': '482px',
                                      'height': '79px',}),
        html.Br(),
        dbc.Row([
        dbc.Col([html.H6("De 18 años y más", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })])],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                   "background-color": "#0097A7",
                                      
                                      'margin-left': '700px',
                                      'width': '482px',
                                      'height': '79px',}),
       ############################################################Variables de vivienda
    html.Br(),
    dbc.Row(
       dbc.Col([html.P([dbc.Button([html.H1(className="fas fa-home",
                                style={'textAlign': 'left',
                                       "color":"#FBC02D",
                                      "font-size": "80px"}),
            "  Variables de Vivienda"], 
                    style={'textAlign': 'left',"color":"#FBC02D",
                   "font-size": "30px",
                          })]),])),
     dbc.Row(
        [dbc.Col(dbc.Table(table_bodyv, 
                              bordered=False, 
                              dark=False,
                              hover=True,
                              #responsive=True,
                              striped=True,
                              #size="sm",
                              #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                              style={
           # 'margin-top': '9px',
            'margin-left': '50px',
            #'margin-right': '-370px',
            'width': '800px',
            'height': '46px',
            "font-size": "large" }
                                     ))]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([dbc.Button((["", html.H1(className="fas fa-wifi", style={"color": "black",
                                                                 "background-color": "light"}),
                 html.H6(" Con internet ",
                        style={"color":"black",
                                "background-color": "light"}),
                 html.H1("97%",
                        style={"color":"black",
                                "background-color": "light"}),
                 #html.H6("1,625,420")                      
        ]),style={ "background-color": "light"}),

            
         dbc.Button((["", html.H1(className="fas fa-tv", 
                                  style={"color": "lightgray",
                                         "background-color": "light"}),
                 html.H6(" Con televisor ", 
                         style={"color":"lightgray",
                                "background-color": "light"}),
                      
                 html.H1("97%",  
                         style={"color":"lightgray",
                                "background-color": "light"}),
                 #html.H6("1,625,420")                      
        ]),style={ "background-color": "light"}),

         dbc.Button((["", html.H1(className="fas fa-laptop", style={"color": "lightgray",
                                                                   "background-color": "light"}),
                 html.H6(" Con computadora ",
                         style={"color":"lightgray",
                                "background-color": "light"}),
                 html.H1("97%",
                        style={"color":"lightgray",
                                "background-color": "light"}),
                 #html.H6("1,625,420")                      
        ]),style={ "background-color": "light"}),
            

         dbc.Button((["", html.H1(className="fas fa-mobile-alt", style={"color": "black",
                                                                       "background-color": "light"}),
                 html.H6(" Con celular ",
                        style={"color":"black",
                                "background-color": "light"}),
                 html.H1("97%",
                        style={"color":"black",
                                "background-color": "light"}),
                 #html.H6("1,625,420")                      
        ]),style={ "background-color": "light"}),
            
     
        ])],style={"width": "50rem", 
                   "border": "0",
                   "background-color": "light",
                  "outline": "white",
                  'margin-left': '50px',}),

    html.Br(),
    html.Br(),
    
    ##############################################################                   MIGRACION
    dbc.Row([
        dbc.Col([
            html.P([dbc.Button([html.H1(className="fas fa-plane-departure",
                                style={'textAlign': 'left',
                                       "color":"#880E4F",
                                      "font-size": "70px"}),
            "  Variables de Migración"], 
                    style={'textAlign': 'left',"color":"#880E4F",
                   "font-size": "30px",
                           'margin-left': '50px',
                          }),])])]),
    
   dbc.Row([
        dbc.Col([html.H6("Población nacida en otra entidad", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#880E4F",
                           "height": "7px",}),
            html.H3("  6,957,622", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#880E4F",
                           "height": "7px",}),
            html.P("28%", 
                   style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "48px",
                         'margin-top': '-35px',
                         'margin-bottom': '37px',
                         "height": "7px",
                         })          
                
        ],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                  
                                      "margin-right": "500px",
                                      'margin-left': '50px',
                                      'width': '82px',
                                      'height': '79px',
                 #"width": "50 rem", 
          "border": "0",
          "background-color": "#880E4F"
          }
    ),]),
    
  html.Br(),  
 dbc.Row([
        dbc.Col([html.H6("Mujeres nacidas en otra entidad", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#BA68C8",
                           "height": "7px",}),
            html.H3("  6,957,622", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#BA68C8",
                           "height": "7px",}),
            html.P("28%", 
                   style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "48px",
                         "height": "7px",
                         })   
             
        ],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                  
                                      "margin-right": "500px",
                                      'margin-left': '50px',
                                      'width': '82px',
                                      'height': '79px',
                 #"width": "50 rem", 
          "border": "0",
          "background-color": "#BA68C8"
          }
    ),]),
  

  html.Br(),  
 dbc.Row([
        dbc.Col([html.H6("Hombres nacidos en otra entidad", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#880E4F",
                           "height": "7px",}),
            html.H3("  6,957,622", 
                    style={'textAlign': 'left',
                           "color": "white",
                          "background-color": "#880E4F",
                           "height": "7px",}),
            html.P("28%", 
                   style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "48px",
                         "height": "7px",
                         })          
                ],
    
    style={"width": "82px", 
          "border": "0",
          "margin-right": "500px",
          'margin-left': '50px',
          'height': '79px',
          "background-color": "#880E4F"
          },),]),
        
#################################################################              DISCAPACIDAD
    
    html.Br(),
    html.Br(),
      dbc.Row([
        dbc.Col([
            html.P([dbc.Button([html.H1(className="fa fa-wheelchair",
                                style={'textAlign': 'left',
                                       "color":"#BA68C8",
                                      "font-size": "70px"}),
            "  Variables de Discapacidad"], 
                    style={'textAlign': 'left',"color":"#BA68C8",
                   "font-size": "30px",
                           'margin-left': '50px',
                          }),])])]),
    dbc.Row(
        [dbc.Col(dbc.Table(table_bodyd, 
                              bordered=False, 
                              dark=False,
                              hover=True,
                              #responsive=True,
                              striped=True,
                              #size="sm",
                              #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                              style={
           # 'margin-top': '9px',
            'margin-left': '50px',
            #'margin-right': '-370px',
            'width': '800px',
            'height': '46px',
            "font-size": "large" }
                                     ))]),
####################################################################            ECONOMIA
    html.Br(),
    html.Br(),
    dbc.Row([
         html.Br(),
        dbc.Col([
            html.P([dbc.Button([html.H1(className="fas fa-hand-holding-usd",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "70px"}),
            "  Variables de economía"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                           'margin-left': '50px',
                          }),])])]),
       dbc.Row([
           dbc.Col([
               html.H6("No económicamente activa con limitación física o mental", 
                    style={'textAlign': 'left',
                           "color": "white",
                           "background-color": "#6A1B9A"}),
            html.H3("112,842", style={'textAlign': 'left',
                                      "color": "white",
                                      "background-color": "#6A1B9A"}),
            html.Br(),
            html.Br(),
            
            dbc.ButtonGroup(html.Span([
                html.H1(className="fas fa-wheelchair", 
                        style={"background-color": "#6A1B9A",
                               "color":"white",
                               "font-size": "110px",
                              #'size':'80px',
                              'textAlign': 'center',
                               #'margin-left':'10px'
                              }),]),),
            html.Br(),
            html.Br(),
            
            html.H2("2%", 
                  style={'textAlign': 'center',
                         "color": "white",
                            #"height": "7px",
                         "font-size": "40px",
                         #'margin-top': '-32px',
                         #'margin-bottom': '30px',
                         "background-color": "#6A1B9A"}),]
               ,style={"width": "13rem", 
          "border": "0",
          "background-color": "#6A1B9A",
           'color':'#BA68C8',
          # "height": "200px",
          }),],style={"width": "13rem", 
                                   "border": "0",
                                   #"height": "10px",
                                   "background-color": "#9cd9e0",
                                      "margin-up": "-5px",
                                      'margin-left': '680px',
                                      'width': '182px',
                                      'height': '20px',}),
    

    

    
  dbc.Row([
      dbc.Col([html.H6("Población ocupada", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2("95%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',
                       

                         })],style={ 
                                      "border": "0",
                                    "margin-left": "50px",
                                    "margin-right": "800px",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                    })]),
    html.Br(),
     dbc.Row([
      dbc.Col([ html.H6("Población masculina ocupada", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.H2("95%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })],style={ 
                                      "border": "0",
                                    "margin-left": "50px",
                                    "margin-right": "800px",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                    })]),
     html.Br(),
     dbc.Row([
      dbc.Col([html.H6("Población femenina ocupada", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2("95%", 
                  style={'textAlign': 'right',
                         "color": "white",
                            "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })],style={ 
                                      "border": "0",
                                    "margin-left": "50px",
                                    "margin-right": "800px",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                    }),
         
     ]),
    ####################################################################################### RELIGION
     html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row([
         html.Br(),
        dbc.Col([
            html.P([dbc.Button([html.H1(className="fas fa-church",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de Religion"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                           'margin-left': '50px',
                          })]),
            ])],
    style={"width": "50rem", 
           "border": "0",
           "fill" : "orange"},
),
    
       dbc.Row([
        dbc.Col([html.H6("Religión católica", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H3("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.P("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })          
                
        ],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                  
                                      "margin-right": "500px",
                                      'margin-left': '50px',
                                      'width': '82px',
                                      'height': '79px',
                 #"width": "50 rem", 
          "border": "0",
          "background-color": "#9cd9e0"
          }
    ),]),
    html.Br(),
    dbc.Row([
        dbc.Col([html.H6("Protestantes, Evangélicas y diferentes de Evangélicas", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H3("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.P("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })          
                
        ],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                  
                                      "margin-right": "500px",
                                      'margin-left': '50px',
                                      'width': '82px',
                                      'height': '79px',
                 #"width": "50 rem", 
          "border": "0",
          "background-color": "#0097A7"
          }
    ),]),
#########################################################################                        EDUCACION
      html.Br(),
    html.Br(),
     dbc.Row([
         html.Br(),
        dbc.Col([
            html.P([dbc.Button([html.H1(className="fas fa-book-reader",
                                style={'textAlign': 'left',
                                       "color":"#81C784",
                                      "font-size": "80px"}),
            "  Variables de educación"], 
                    style={'textAlign': 'left',"color":"#81C784",
                   "font-size": "30px",   'margin-left': '50px', 
                          })]),
        
            ])],
    style={"width": "50rem", 
           "border": "0",
           "fill" : "orange"},
),
    html.Br(),
    html.Br(),
     dbc.Row(
        [dbc.Col(dbc.Table(table_bodyedu, 
                              bordered=False, 
                              dark=False,
                              hover=True,
                              #responsive=True,
                              striped=True,
                              #size="sm",
                              #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                              style={
           # 'margin-top': '9px',
            'margin-left': '50px',
            #'margin-right': '-370px',
            'width': '800px',
            'height': '46px',
            "font-size": "large" }
                                     ))]),
     html.Br(),
    html.Br(),
    ################################################################################################ derechohabientes
     dbc.Row([
         html.Br(),
        dbc.Col([
            html.P([dbc.Button([html.H1(className="fas fa-procedures",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de derechohabiencia"], 

                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",   'margin-left': '50px', 
                          })]),
        
            ])],
    style={"width": "50rem",  },),

    dbc.Row([
        dbc.Col([html.H6("Derechohabiente del IMSS", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H3("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.P("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })          
                
        ],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                  
                                      "margin-right": "500px",
                                      'margin-left': '50px',
                                      'width': '82px',
                                      'height': '79px',
                 #"width": "50 rem", 
          "border": "0",
          "background-color": "#9cd9e0"
          }
    ),]),
    html.Br(),        

    dbc.Row([
        dbc.Col([html.H6("Derechohabiente del Seg. Pop. o Seguro Médico para una Nueva Generación", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#0097A7"}),
            html.H3("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#0097A7"}),
            html.P("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })          
                
        ],style={"width": "25.5rem", 
                                   "border": "0",
                                   #"height": "10px",
                                  
                                      "margin-right": "500px",
                                      'margin-left': '50px',
                                      'width': '82px',
                                      'height': '79px',
                 #"width": "50 rem", 
          "border": "0",
          "background-color": "#0097A7"
          }
    ),]),
     html.Br(),
    html.Br(),
 #################################################################################### hogares censales   
     dbc.Row([
         html.Br(),
        dbc.Col([
            html.P([dbc.Button([html.H1(className="fas fa-users",
                                style={'textAlign': 'left',
                                       "color":"#F48FB1",
                                      "font-size": "80px"}),
            "  Variables de hogares censales"], 

                    style={'textAlign': 'left',"color":"#F48FB1",
                   "font-size": "30px",   'margin-left': '50px', 
                          })]),
        
            ])],
    style={"width": "50rem",  },),
    html.Br(), 
     dbc.Row(
        [dbc.Col(dbc.Table(table_bodyhc, 
                              bordered=False, 
                              dark=False,
                              hover=True,
                              #responsive=True,
                              striped=True,
                              #size="sm",
                              #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                              style={
           # 'margin-top': '9px',
            'margin-left': '50px',
            #'margin-right': '-370px',
            'width': '800px',
            'height': '46px',
            "font-size": "large" }
                                     ))]),
         
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    dbc.Row([
                                    #https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width=4, lg={'size': 1,  "offset": 3, }),
            
           dbc.Col(html.H6(" S e c r e t a r í a   G e n e r a l," 
                           " Secretaría de Servicios Parlamentarios, "
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0}),
               ], justify="start",),
     dbc.Row([    
           dbc.Col(html.H5([dbc.Badge("Equipo responsable", 
                          href="https://raw.githubusercontent.com/fdealbam/feminicidios/main/Autores.pdf",
                          #color="light",
                          #className="ml-1")
                                     )]),
                  width={'size': 3,  "offset": 4}),
                       ], justify="start",),
    html.Br(),
    html.Br(),
    html.Br(),

    

    
    html.Br(),
        
            ])
    

app.layout = html.Div([body])


if __name__ == '__main__':
    app.run_server(use_reloader = False)
    
