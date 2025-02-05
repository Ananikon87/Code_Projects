# -*- coding: utf-8 -*-
"""Basic Dashboard Mini Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xxajbfhz2a4t5R7HJPPDpzUVQtuEuJ7i
"""

import dash
from dash import dcc
from dash import html

# Create a Dashboard Application
app = dash.Dash(__name__)

# Define the layout of the Dashboard
app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data':[
                    {'x':[1,2,3], 'y':[4,1,2],'type': 'bar', 'name':'Bar Chart'},
                    {'x':[1,2,3], 'y':[2,4,5],'type': 'line', 'name':'Line Chart'},
                ],
                'layout':{
                    'title': 'Graph Title',
                    'xaxis': {'title':'x-axis'},
                    'yaxis': {'title':'y-axis'}
                }
            }
        )
    ]
)

# Code that runs the application
if __name__ == '__main__':
    app.run_server(debug=True)