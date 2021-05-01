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




##########################################################################
#Seccion 1. Variables de POBLACION
##########################################################################



#################################### Card

card = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Variables", 
                    className="card-title",
                    style={'textAlign': 'left',"color": "gray"}),
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
                   #'FontColor': 120
                      }
            ),

            
            
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
                         "font-size": "48px",
                         "font-weight": 'bold',
                        "color": "dark",}),
           
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
                "Primaria incompleta "
              "  3,829,453",
                className="card-text",
                style={'textAlign': 'left',"color": "black",
                   'FontColor': 120}
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
                         "font-size": "48px",
                         "font-weight": 'bold',}),
            

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
                   'FontColor': 120}
            ),
            dbc.Button(
                html.Span(["", html.H1(className="fas fa-wheelchair", style={"color": "#FFD180"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),
                               html.H1(className="fas fa-wheelchair", style={"color": "#E0E0E0"}),]),),
             html.P("4%", 
                  className="card-text",
#                     style={'textAlign': 'center',
#                         "color": "black",  
#                         "font-size": "40px",
#                         "font-weight": 'bold',
#                        "color": "dark",
#                        "height": "30px",}),
                    style={'textAlign': 'right',
                         "color": "black",  
                         "font-size": "48px",
                         "font-weight": 'bold',}),

        ]
    ),
    
    style={"width": "22.5rem", 
          "border": "0",
           "card-border": "0",
           # 'margin-left': '-30px'
          },
)





##########################################################################
#Seccion 2. Variables de vivienda
##########################################################################

#################################### Card2 HAY QUE AJUSTARLA CON....


card2 = dbc.Card(
    dbc.CardBody(
        [
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
            
        ]
    ),
    
    style={"width": "25.5rem", 
          "border": "0",
          "margin-left": "-4px",
           
          "background-color": "orange"
          },
)




card21 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 18 años y más", 
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

                         })]), 
                            style={"width": "25.5rem", 
                                   "border": "0",
                         "margin-left": "18px",
                                   "background-color": "#0097A7",
                                  },)

card22 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 18 años y más", 
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

                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                         "margin-left": "18px",
                                      "background-color": "#0097A7",
                                  },)

card23 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 18 años y más", 
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

                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                         "margin-left": "18px",
                                      "background-color": "#0097A7",
                                  },),

card24 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 18 años y más", 
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

                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                         "margin-left": "18px",
                                      "background-color": "#0097A7",
                                  },)

card25 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 18 años y más", 
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

                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                         "margin-left": "18px",
                                      "background-color": "#0097A7",
                                  },)

card26 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 18 años y más", 
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

                         })]), 
                            style={"width": "25.5rem", 
                                      "border": "0",
                                     "margin-left": "18px",
                                      "background-color": "#0097A7",
                                  },)

card27 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("De 18 años y más", 
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

                         })]), 
                            style={"width": "25.5rem", 
                                   "border": "0px",
                                   "margin-left": "18px",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)


##########################################################################
#Seccion 3. Variables de vivienda
##########################################################################



## Tabla de variables
row1 = html.Tr([dbc.Alert("Con sanitario y con agua", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("94%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                        })])


row2 = html.Tr([dbc.Alert("Viviendas habitadas", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("94%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                        })])

row3 = html.Tr([dbc.Alert("Con luz eléctrica",  color="#E0E0E0"),
                html.Td("5,162,569"),  
                dbc.Alert("99%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                              })])

row4 = html.Tr([dbc.Alert("Con agua entubada", color="#E0E0E0"), 
                html.Td("4,973,950"),  
                dbc.Alert("92%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                              })])

row5 = html.Tr([dbc.Alert("Con drenaje"), 
                html.Td("5,115,669"),  
                dbc.Alert("96%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                              })])

row5 = html.Tr([dbc.Alert("Con sanitario", color="#E0E0E0"), 
                html.Td("5,132,288"),  
                dbc.Alert("97%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#FBC02D",       
                              })])

table_body = [html.Tbody([row1, row2, row3, row4,row5])]




#################################### Card3
card3 = dbc.Card(
    dbc.CardBody(
        [
            
            html.P([dbc.Button([html.H1(className="fas fa-home",
                                style={'textAlign': 'left',
                                       "color":"#FBC02D",
                                      "font-size": "80px"}),
            "  Variables de Vivienda"], 
                    style={'textAlign': 'left',"color":"#FBC02D",
                   "font-size": "30px",
                           'margin-bottom':'-30px'
                          })]),
            
     dbc.Table( table_body, bordered=False)
                    ]),
    
    
    style={"width": "50rem", 
          "border": "0",
           "margin-left": "40px",
           "margin-top": "-40px",
           "fill" : "orange"},
)



##########################################################################
#Seccion 4 Variables de INTERNET
##########################################################################


#################################### Card2p3
card2p3 = dbc.Card(
    dbc.CardBody(
        [
         dbc.Button((["", html.H1(className="fas fa-wifi", style={"color": "black",
                                                                 "background-color": "light"}),
                 html.H6(" Con internet ",
                        style={"color":"black",
                                "background-color": "light"}),
                 html.H1("97%",
                        style={"color":"#FBC02D",
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
                         style={"color":"#FBC02D",
                                "background-color": "light"}),
                 #html.H6("1,625,420")                      
        ]),style={ "background-color": "light"}),

         dbc.Button((["", html.H1(className="fas fa-laptop", style={"color": "lightgray",
                                                                   "background-color": "light"}),
                 html.H6(" Con computadora ",
                         style={"color":"lightgray",
                                "background-color": "light"}),
                 html.H1("97%",
                        style={"color":"#FBC02D",
                                "background-color": "light"}),
                 #html.H6("1,625,420")                      
        ]),style={ "background-color": "light"}),
            

         dbc.Button((["", html.H1(className="fas fa-mobile-alt", style={"color": "black",
                                                                       "background-color": "light"}),
                 html.H6(" Con celular ",
                        style={"color":"black",
                                "background-color": "light"}),
                 html.H1("97%",
                        style={"color":"#FBC02D",
                                "background-color": "light"}),
                 #html.H6("1,625,420")                      
        ]),style={ "background-color": "light"}),
            
     
        ]), style={"width": "50rem", 
                   "border": "0",
                   "background-color": "light",
                  "outline": "white"
                #  "border-width": "1px"
                  })


        


##########################################################################
#Seccion 5 Variables de RELIGION
##########################################################################


card_religion1 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Religión católica", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                  },)

card_religion2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Protestantes, Evangélicas y diferentes de Evangélicas", 
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

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)





#########
card_v_religionAA = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fas fa-church",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de Religion"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                          })]),
            
            dbc.Card(card_religion1),
            html.Br(),
            dbc.Card(card_religion2),
            
        ]),
    style={"width": "50rem", 
           "border": "0",
           "fill" : "orange"},
)





##########################################################################
#Seccion 7. Variables de MIGRACION
##########################################################################


card_migra1 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población nacida en otra entidad", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                  },)

card_migra2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Mujeres nacidas en otra entidad", 
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

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)

card_migra3 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Hombres nacidas en otra entidad", 
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

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)


#################################### card_v_migracion
#"fas fa-hospital-user"
#"fas fa-procedures"
card_v_migracion = dbc.Card(
    dbc.CardBody([
        html.P([dbc.Button([html.H1(className="fas fa-plane-departure",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de migración"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                          })]),
        
        dbc.Card(card_migra1),
        html.Br(),
        dbc.Card(card_migra2),
        html.Br(),
        dbc.Card(card_migra3),
        
    ],  style={"width": "50rem", 
           "border": "0",
           "fill" : "orange"},))


    
##########################################################################
#Seccion 8. Variables de HOGARES CENSALES
##########################################################################

row1 = html.Tr([dbc.Alert("Población en hogares con jefa(e) de 30 a 59 años", color="#E0E0E0",), 
                html.Td("172,575"),
                dbc.Alert("4%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])


row2 = html.Tr([dbc.Alert("Población en hogares con jefa(e) de 60 años y más", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])

row3 = html.Tr([dbc.Alert("Población en hogares con jefatura femenina", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])

row4 = html.Tr([dbc.Alert("Población en hogares con jefa e hijos menores de 18 años", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#F48FB1",       
                        })])

table_body = [html.Tbody([row1, row2, row3, row4])]



#################################### card_v_hog_cens

           
card_v_hog_cens = dbc.Card(
    dbc.CardBody(
        [

        html.P([dbc.Button([html.H1(className= "fas fa-users",
                                    #"fas fa-house",
                                style={'textAlign': 'left',
                                       "color":"#F48FB1",
                                      "font-size": "80px"}),
            "  Variables de hogares censales"], 
                    style={'textAlign': 'left',"color":"#F48FB1",
                   "font-size": "30px",
                           'margin-bottom':'-30px'
                          })]),            
            
            
     dbc.Table( table_body, bordered=False)
                    ]),
    
    
    style={"width": "50rem", 
          "border": "0",
          "fill" : "orange"},
)

    
##########################################################################
#Seccion 9. Variables de DISCAPACIDAD
##########################################################################

row1 = html.Tr([dbc.Alert("Poblacion con discapacidad", color="#E0E0E0",), 
                html.Td("172,575"),
                dbc.Alert("4%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#BA68C8",       
                        })])


row2 = html.Tr([dbc.Alert("Poblacion con discapacidad derechohabiente", color="#E0E0E0",), 
                html.Td("19,172,575"),
                dbc.Alert("59%", color="light",
                        style={"font-size": "35px",
                        "font-weight": 'bold',
                        "color": "#BA68C8",       
                        })])

table_body = [html.Tbody([row1, row2,])]


card_v_discapacidad = dbc.Card(
    dbc.CardBody(
        [
            
            html.P([dbc.Button([html.H1(className="fa fa-wheelchair",
                                style={'textAlign': 'left',
                                       "color":"#BA68C8",
                                      "font-size": "80px"}),
            "  Variables de Discapacidad"], 
                    style={'textAlign': 'left',"color":"#BA68C8",
                   "font-size": "30px",
                           'margin-bottom':'-30px'
                          })]),
            
     dbc.Table( table_body, bordered=False)
                    ]),
                    style={"width": "50rem", 
                          "border": "0",
                          "fill" : "orange"},
        )


##########################################################################
#Seccion 10. Variables de ECONOMIA
##########################################################################


card_econom1 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población ocupada", 
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

                         })]),style={"width": "36rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                    },)




card_econom2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población masculina ocupada", 
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

                         })]),style={"width": "36rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                    },)


card_econom3 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Población femenina ocupada", 
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

                         })]),style={"width": "36rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                    },)


card_econom4 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("12 años y más, no ecónomicamente activa estudiante", 
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

                         })]),style={"width": "36rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                    },)

card_economia = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fas fa-hand-holding-usd",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de economía"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                          })],),
            dbc.Card(card_econom1),
            html.Br(),
            dbc.Card(card_econom2),
            html.Br(),
            dbc.Card(card_econom3),
            html.Br(),
            dbc.Card(card_econom4),
        ],style={"width": "38rem", }))
            

    
    
    
    
    
    
card_economia_discap = dbc.Card(
    dbc.CardBody(
        [
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
                         "background-color": "#6A1B9A"}),]),
    style={"width": "13rem", 
          "border": "0",
           #"margin-left": "40px",
          "background-color": "#6A1B9A",
           'color':'#BA68C8',
           "height": "550px",
          })


##########################################################################
#Seccion 11. Variables de RELIGION
##########################################################################


card_religion1 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Religión católica", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                  },)

card_religion2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Protestantes, Evangélicas y diferentes de Evangélicas", 
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

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)





#########
card_v_religionAA = dbc.Card(
    dbc.CardBody(
        [
            html.P([dbc.Button([html.H1(className="fas fa-church",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de Religion"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                          })]),
            
            dbc.Card(card_religion1),
            html.Br(),
            dbc.Card(card_religion2),
            
        ]),
    style={"width": "50rem", 
           "border": "0",
           "fill" : "orange"},
)






##########################################################################
#Seccion 6 Variables de EDUCACION
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

table_body = [html.Tbody([row1edu, row2edu, row3edu])]



#################################### card_v_edu

           
card_v_edu = dbc.Card(
    dbc.CardBody(
        [
         html.P([dbc.Button([html.H1(className="fas fa-book-reader",
                                style={'textAlign': 'left',
                                       "color":"#81C784",
                                      "font-size": "80px"}),
            "  Variables de educación"], 
                    style={'textAlign': 'left',"color":"#81C784",
                   "font-size": "30px",
                           'margin-bottom':'-30px'
                          })]),
            
     dbc.Table( table_body, bordered=False)
                    ]),
    
    
    style={"width": "50rem", 
     #   "border":"none",
     #    "border-color": "transparent",
    #"background-color": "transparent",
     #     " border-bottom":" 1px solid rgba(0,0,0,.8)",
          # "border": "0",
          # "border-top":"0",
          # "border-right":"0",
          # "border-bottom":"0",
          # "border-left":"0",
          #  "padding": "0",
          # "card-border": 0,
           "border-color": "white",
           
         },
)
    

    

##########################################################################
#Seccion 7. Variables de DERECHOHABIENCIA
##########################################################################


card_derechohab1 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Derechohabiente del IMSS", 
                    style={'textAlign': 'left',
                           "color": "white",
                            "height": "7px",
                          "background-color": "#9cd9e0"}),
            html.H5("13,660,403", 
                    style={'textAlign': 'left',
                            "height": "7px",
                           "color": "white",
                          "background-color": "#9cd9e0"}),
            html.H2("64%", 
                  style={'textAlign': 'right',
                         "color": "white",
                         "height": "7px",
                         "font-size": "38px",
                         'margin-top': '-32px',
                         'margin-bottom': '30px',

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#9cd9e0",
                                  },)

card_derechohab2 = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Derechohabiente del Seg. Pop. o Seguro Médico para una Nueva Generación", 
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

                         })]), 
                            style={"width": "48rem", 
                                      "border": "0",
                                       #"height": "10px",
                                      "background-color": "#0097A7",
                                  },)
                
#################################### card_v_derechohab
#"fas fa-hospital-user"
#"fas fa-procedures"
card_v_derechohab = dbc.Card(
    dbc.CardBody([
        html.P([dbc.Button([html.H1(className="fas fa-procedures",
                                style={'textAlign': 'left',
                                       "color":"#0097A7",
                                      "font-size": "80px"}),
            "  Variables de derechohabiencia"], 
                    style={'textAlign': 'left',"color":"#0097A7",
                   "font-size": "30px",
                          })]),
        
        dbc.Card(card_derechohab1),
        html.Br(),
        dbc.Card(card_derechohab2),]),
    style={"width": "50rem", 
           "border": "0",
           "fill" : "orange"},)
    
    
    
    
    
########################################################################
# A P P 
########################################################################



# identificadores
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                LUX, FONT_AWESOME], server=server)

body = html.Div([
   
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
    

    
    ################## SECCION 1 (pag1)_VARIABLES DE POBLACION
    dbc.Row([
        dbc.Col(dbc.Card(card), sm={  "offset": 1, }),#Variables Vivienda
        dbc.Col(dbc.Card(card2),                      #población total
               style={#'margin-top': '-540px',       #arriba
                      'margin-left': '40px', 
               #       'width': '479px',
               #       'height': '100%',
               }, sm={  "offset": 1, })
     ], className="blockquote"),
    
    dbc.Row([
        dbc.Col(dbc.Card(card21), #cuadros azules
                style={'margin-top': '-678px', #arriba
                       'margin-left': '467px', 
                       'width': '382px',
                       'height': '379px',})
    ]),
    
    dbc.Row([
       dbc.Col(dbc.Card(card22),#cuadros azules
               style={'margin-top': '-593px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '379px',
                     })
    ]),

    dbc.Row([
        dbc.Col(dbc.Card(card23),#cuadros azules
                style={'margin-top': '-508px', #arriba
                       'margin-left': '467px', 
                       'width': '382px',
                       'height': '379px',})
    ]),

     dbc.Row([
       dbc.Col(dbc.Card(card24),#cuadros azules
               style={'margin-top': '-423px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '379px',
                     })
    ]),
      dbc.Row([
       dbc.Col(dbc.Card(card25),#cuadros azules
               style={'margin-top': '-338px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '379px',
                     })
    ]),
       dbc.Row([
      dbc.Col(dbc.Card(card26, outline=False),#cuadros azules
              style={'margin-top': '-293px', #arriba
                     'margin-left': '467px', 
                     'width': '382px',
                      'height': '279px',
                   })
    ]),
         dbc.Row([
       dbc.Col(dbc.Card(card27),#cuadros azules
               style={'margin-top': '-208px', #arriba
                      'margin-left': '467px', 
                      'width': '382px',
                      'height': '19px',
                     })
    ]),
    
    ################## SECCION 2 (pag1)_VARIABLES DE VIVIENDA
    dbc.Row([
       
  
        
        dbc.Col(dbc.Card(card3, color="white", inverse=True, outline =False  ),sm={  "offset": 1, }),
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),


    
    ################## SECCION 4 (pag1)_VARIABLES DE INTERNET

    dbc.Row([
        dbc.Col(dbc.Card(card2p3, color="green"),
         sm={  "offset": 1, }),
    
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    html.Br(),
    

    
    ################## SECCION 5 (pag1)__VARIABLES DE MIGRACION
     
    dbc.Row([
        dbc.Col(dbc.Card(card_v_migracion), #cuadros azules
                sm={ 'size': 9.5,
                    "offset": 1, }),
                 ], style={"border": "0px",
                          "border-color": "red",
                          "border-width": "0px"}, 
                    no_gutters= True, justify= "start",
                 className="blockquote"),

    
    
    #############################>>>>>>> II <<<<<<<<<#############################
    
    ################## SECCION 1 (pag 2)__VARIABLES DE DISCAPACIDAD
    dbc.Row([
        dbc.Col(dbc.Card(card_v_discapacidad, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={"offset": 1, }),
         
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),

    
 
    
    dbc.Row([
        dbc.Col(dbc.Card(card_economia), sm={  "offset": 1, }),#Variables Vivienda
        dbc.Col(dbc.Card(card_economia_discap),                      #población total
               style={#'margin-top': '-540px',       #arriba
                      'margin-left': '15px',
                   "color":"#BA68C8"
               #       'width': '479px',
               #       'height': '100%',
               }, sm={  "offset": 1, })
     ],  no_gutters= True, justify= "start",
     className="blockquote"),
    
 

    # ejemplo card in card
    dbc.Row([
        dbc.Col(dbc.Card(card_v_religionAA),
                sm={  "offset": 1, }),
    ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    
    #############################>>>>>>> III <<<<<<<<<#############################
    
    ################## SECCION 1 (3a pag)__VARIABLES DE EDUCACION      
    dbc.Row([
        dbc.Col(dbc.Card(card_v_edu, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",
     ),
    
    
    ################## SECCION 2 (3a pag)__VARIABLES DE DERECHOHABIENCIA
    dbc.Row([
        dbc.Col(dbc.Card(card_v_derechohab, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={ "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",),
    
    ################## SECCION 3 (3a pag)__VARIABLES DE HOGARES CENSALES 
    dbc.Row([
        dbc.Col(dbc.Card(card_v_hog_cens, #color="#FBFBFB", outline=True,
                         #inverse=False
                        ),
         sm={  "offset": 1, }),
     ], no_gutters= True, justify= "start",
     className="blockquote",),

    html.Br(),
    html.Br(),
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
                  width={'size': 5, 'offset': 0}),
               ], justify="start",),
     dbc.Row([    
           dbc.Col(html.H5([dbc.Badge("Equipo responsable", 
                          href="https://raw.githubusercontent.com/fdealbam/feminicidios/main/Autores.pdf",
                                     )]),
                  width={'size': 3,  "offset": 4}),
                       ], justify="start",),
    html.Br(),
    html.Br(),
    html.Br(),

    

    
    html.Br(),
        
            ])
    

app.layout = html.Div([body])
#app.layout = html.Div(children=[html.Img(className='icon')])

if __name__ == '__main__':
    app.run_server()
    
