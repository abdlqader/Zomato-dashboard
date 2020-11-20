#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:30:12 2020

@author: abdulkader
"""
import sys
sys.path.append("..")
from maindash import app 
from view.tab1 import tab1_content
from view.tab2 import tab2_content

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


def main_view():
    
    return dbc.Tabs(
        [
            dbc.Tab(tab1_content(), label="Word Distribution"),
            dbc.Tab(tab2_content(), label="Cost and Rating"),
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