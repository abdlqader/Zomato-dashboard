#   !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:31:21 2020

@author: abdulkader
"""
from maindash import app,df

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px

dff = df.dataframe.copy()
    

def tab1_content():

    fig = px.scatter_geo(dff,lat='Latitude',lon='Longitude', color="Country",
                    color_continuous_scale=px.colors.sequential.Plasma)
    return dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id='world-distribution',figure=fig)
        ]
    ),
    className="mt-3",
    )


    