#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:36:02 2020

@author: abdulkader
"""


import re

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('zomato/zomato.csv',encoding='latin-1')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)
server = app.server


cuisines_val = sorted(set([cuisine.strip() for cuisines in df['Cuisines'] if type(cuisines) != float for cuisine in cuisines.split(',')]))

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='cuisines_vals',
                options=[{'label': i, 'value': i} for i in cuisines_val],
                value='Asian'
            ),
            dcc.RadioItems(
                id='has_delievery',
                options=[
                    {'label': 'All', 'value': False},
                     {'label': 'Is Delievery now', 'value': 'Yes'},
                     {'label': 'Doesnt  Delievery now', 'value': 'No'},],
                value=False,
                labelStyle={'display': 'inline-block'}
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
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})

    ],style={'padding-bottom': '10px'}),

    dcc.Graph(id='indicator-graphic'),
    dcc.Markdown('''
    # Extra insights  
    #### Firstly column names need to be normalized and standardized  
    #### There is a couple of data inconsistency such as float in Cuisines column  
    #### Some restaurant located in the middle of the water (with zero Latitude and Longitude) which cases data to be falsy.  
    ** ps. ** this is a totally free dashboard made with python with no styling, which can be achieved by normal front end developments
    ''')

],style={'padding': '20px'})
def cuis_trans(a,cuis):
    if type(a) == float:
        return False
    if re.search(cuis,a) == None:
        return False
    else:
        return True
    


@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('cuisines_vals', 'value'),
     Input('has_delievery', 'value'),
     Input('price', 'value')])
def update_graph(cuisines_vals,
                 has_delievery,
                 price_range):
    dff = df.copy()
    print(has_delievery)
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

if __name__ == '__main__':
    app.run_server(debug=False)
