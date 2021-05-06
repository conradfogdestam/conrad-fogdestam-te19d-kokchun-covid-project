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
fig4 = GenderDifference()

#-----------------------------------------------------------


app.layout = html.Div(children=[
    html.Br(),
    html.H1(children='''
        [CORONA VISUALIZER]
    '''),
    html.H6(children='''
        Conrad Fogdestam TE19D
    '''),
    html.H1(children='''
        __________________________________________________________________________
    '''),
    html.Br(),
    html.Br(),
    html.Div([

        html.H1(children='National Daily Deaths'),

        html.Div(children='''
        Det har skett två stora omgångar med smittspridning i sverige
    '''),

        dcc.Graph(
            id='NationalDailyDeaths',
            figure=fig1
        ),  
    ], style={'textAlign': 'center'}),

#----------------------------------------------------------------------

    html.Div([
        html.H1(children='National Daily ICU Admissions'),

        html.Div(children='''
        Antal patienter i ICU följer ganska exakt kurvan på antal smittade
    '''),

        dcc.Graph(
            id='NationalDailyIcuAdmissions',
            figure=fig2
        ),  
    ], style={'textAlign': 'center'}),

#-----------------------------------------------------------------------    

    html.Div([
        html.H1(children='Covid Mortality Rate'),

        html.Div(children='''
        Mortality raten på Covid patienter är väldigt låg,  ca 2% av besmittade omkommer
    '''),

        dcc.Graph(
            id='CasesVSDeaths',
            figure=fig3
        ),  
    ], style={'textAlign': 'center'}),

    #----------------------------------------------------------------------

    html.Div([
        html.H1(children='Gender Differences'),

        html.Div(children='''
        Mer män har omkommit i COVID-19 än kvinnor
    '''),

        dcc.Graph(
            id='Gender Differences',
            figure=fig4
        ),  
    ], style={'textAlign': 'center'}),


], style={'textAlign': 'center'})


if __name__ == "__main__":
    app.run_server(debug=True)