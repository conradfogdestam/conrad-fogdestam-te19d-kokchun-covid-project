import dash
from plotlyfunktions import *
import matplotlib as plt
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#--------------------------------------------------------------

fig1 = NationalDailyDeaths()
fig2 = NationalDailyIcuAdmissions()
fig3 = CasesVsDeaths()

#-----------------------------------------------------------


app.layout = html.Div(children=[
    html.Div([
        html.H1(children='National Daily Deaths'),

        dcc.Graph(
            id='National Daily',
            figure=fig1
        ),  
    ], style={'textAlign': 'center'}),

#----------------------------------------------------------------------

    html.Div([
        html.H1(children='National Daily ICU Admissions'),

        dcc.Graph(
            id='NationalDailyIcuAdmissions',
            figure=fig2
        ),  
    ], style={'textAlign': 'center'}),

#-----------------------------------------------------------------------    

    html.Div([
        html.H1(children='Covid Mortality Rate'),

        dcc.Graph(
            id='CasesVSDeaths',
            figure=fig3
        ),  
    ], style={'textAlign': 'center'}),


])


if __name__ == "__main__":
    app.run_server(debug=True)