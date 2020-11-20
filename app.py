#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:36:02 2020

@author: abdulkader
"""
from maindash import app
from view.main_view import main_view

server = app.server

app.layout = main_view()

if __name__ == '__main__':
    app.run_server(debug=False)