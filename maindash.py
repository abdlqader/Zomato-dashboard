#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:18:03 2020

@author: abdulkader
"""
from proccess import df_proccess

import dash
import dash_bootstrap_components as dbc

df = df_proccess()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
