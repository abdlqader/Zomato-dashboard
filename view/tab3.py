#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:52:01 2020

@author: abdulkader
"""

from maindash import app,df

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px

df_cuisine = df.make_df_cuisine()
df_countries = df.df_countries


def tab3_content():
    fig1 = px.bar(df_countries.sort_values('Count Cuisines'), x='Count Cuisines', y='Country', title='Cuisine per Country',
             labels={'Count' : 'Cuisines per country'}, height=400)
    fig2 = px.bar(df_cuisine.sort_values('Average Cost for two in dollars',ascending=False), y='Average Cost for two in dollars', x='Cuisines', title='Cuisine per Country',
             labels={'Count' : 'Cuisines Cost for two in dollars'},height=400)
    fig2.update_xaxes(rangeslider_visible=True)
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
                        dcc.Graph(id='bar-graph-cuisines-country',figure=fig1)
                        ]
                    ),
                className="mt-3",
                ),
            dbc.Card(
                dbc.CardBody(
                    [
                        dcc.Graph(id='bar-graph-cuisines-cost',figure=fig2)
                        ],
                    ),
                className="mt-3"
                )
            ])

