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

df_cost_rating = df.make_df_cost_rating()

def tab4_content():
    fig1 =px.treemap(df_cost_rating,path=[px.Constant('All'),'Rating text','Price range text'],values='Price range',
                     title = 'Price range percentage according to Rating')
    fig2 = px.scatter(df_cost_rating[['Rating text','Price range','Aggregate rating']].groupby('Rating text').mean().reset_index().sort_values('Price range')
                      ,x='Price range',y='Aggregate rating',color='Rating text',
                      title = 'Rating and Cost Correlation')
    fig2.update_traces(marker=dict(size=12,
                              line=dict(width=2)),
                  selector=dict(mode='markers'))
    fig3 = px.scatter(df_cost_rating
                      ,x='Aggregate rating',y='Average Cost for two in dollars',color='Aggregate rating',
                      title = 'Average Cost for two in dollars vs Rating')
    fig3.update_traces(marker=dict(size=12,
                              ),
                  selector=dict(mode='markers'))
    return html.Div([
            dbc.Card(
                
                dbc.CardBody(
                [
                    html.H4("Restaurants", className="card-title"),
                    html.H6("There is a good partion of Rating unrated", className="card-text"),
                    html.H6("There is correlation between Rating and cost", className="card-text"),
                    html.H6("Restaurants with high price range tend to have good rating", className="card-text"),
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
            dbc.Card(
                
                dbc.CardBody(
                    [
                        dcc.Graph(id='scatter-graph-cost-rating',figure=fig2)
                        ]
                    ),
                className="mt-3",
                ),
            dbc.Card(
                
                dbc.CardBody(
                    [
                        dcc.Graph(id='scatter-graph-cost-two',figure=fig3)
                        ]
                    ),
                className="mt-3",
                ),
    
            ])