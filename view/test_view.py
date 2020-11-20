#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:31:21 2020

@author: abdulkader
"""

import dash_html_components as html
import dash_bootstrap_components as dbc

def tab1_content():
    return dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
    )