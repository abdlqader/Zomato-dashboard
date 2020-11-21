#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:36:02 2020

@author: abdulkader
"""


import re

from maindash import app,df

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

df_cuisines = df.df_cuisines
dataframe = df.dataframe

def cuis_trans(a,cuis):
    if type(a) == float:
        return False
    if re.search(cuis,a) == None:
        return False
    else:
        return True

def tab5_content():
    return html.Div([
       dbc.Card(
                
                dbc.CardBody(
                    [
                         html.Div([
            dcc.Dropdown(
                id='cuisines_vals',
                options=[{'label': i, 'value': i} for i in df_cuisines['Cuisines'].sort_values()],
                value='Asian'
            ),
            dcc.RadioItems(
                id='has_delievery',
                options=[
                    {'label': 'All', 'value': False},
                     {'label': 'Is Delievery now', 'value': 'Yes'},
                     {'label': 'Doesnt  Delievery now', 'value': 'No'},],
                value=False,
                labelStyle={'display': 'inline-block','padding':'10px'}
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            dcc.RadioItems(
                id='price',
                options=[
                    {'label': 'All Price range', 'value': False},
                     {'label': '1', 'value': 1},
                     {'label': '2' ,'value': 2},
                     {'label': '3', 'value': 3},
                     {'label': '4', 'value': 4},],
                value=False,
                labelStyle={'display': 'inline-block','padding':'10px'}
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
        dcc.Graph(id='interactive-graphic'),
                        ]
                    ),
                className="mt-3",
                )
       
            ])


         
    
@app.callback(
Output('interactive-graphic', 'figure'),
[Input('cuisines_vals', 'value'),
 Input('has_delievery', 'value'),
 Input('price', 'value')])
def update_graph(cuisines_vals,
             has_delievery,
             price_range):
    dff = dataframe.copy()
    if has_delievery:
        dff = dff[dff['Is delivering now'] == has_delievery]
    if price_range:
        dff = dff[dff['Price range'] == price_range ]
    dff['cuis_contain'] = dff.Cuisines.apply(lambda a : cuis_trans(a, cuisines_vals)) 
    fig = px.scatter_mapbox(dff[dff['cuis_contain']],
                 lat="Latitude",lon="Longitude",
                 color="Aggregate rating",
                 hover_name="Restaurant Name",
                 color_continuous_scale=px.colors.cyclical.IceFire ,
                 zoom=1, 
                 height=500
                 )
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig
