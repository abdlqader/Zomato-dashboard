#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:30:12 2020

@author: abdulkader
"""
import sys
sys.path.append("..")
from maindash import app 
from view.test_view import tab1_content

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

def main_view():

    tab2_content = dbc.Card(
        dbc.CardBody(
            [
                html.P("This is tab 2!", className="card-text"),
                dbc.Button("Don't click here", color="danger"),
            ]
        ),
        className="mt-3",
    )
    
    
    return dbc.Tabs(
        [
            dbc.Tab(tab1_content(), label="Tab 1"),
            dbc.Tab(tab2_content, label="Tab 2"),
            dbc.Tab(
                "This tab's content is never seen", label="Tab 3", disabled=True
            ),
        ]
    )

    @app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
    def switch_tab(at):
        if at == "tab-1":
            return tab1_content
        elif at == "tab-2":
            return tab2_content
        return html.P("This shouldn't ever be displayed...")