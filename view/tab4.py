#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:45:00 2020

@author: abdulkader
"""

from maindash import app,df

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px

dataframe = df.dataframe

def tab4_content():
    fig1 =px.treemap(dataframe,path=[px.Constant('All'),'Rating text'],values='Price range')
    return html.Div([
            dbc.Card(
                
                dbc.CardBody(
                [
                    html.H4("Cuisines", className="card-title"),
                    html.H6("India has the most Cuisines", className="card-text"),
                    html.H6("Sum Dim is the most expensive cuisine for two in dollars", className="card-text"),
                    html.H6("Some data inconsistancy such as float in Cuisines Column, 9 occurence", className="card-text"),
                ]
    ),
                className="mt-3",
                ),
            dbc.Card(
                
                dbc.CardBody(
                    [
                        dcc.Graph(id='bar-graph-restaurant-rating',figure=fig1)
                        ]
                    ),
                className="mt-3",
                ),
    
            ])