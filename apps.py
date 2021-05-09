import dash
from covid19_plotlyfunctions import *
import matplotlib as plt
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

fig1 = NationalDailyDeaths()
fig2 = NationalDailyIcuAdmissions()
fig3 = GenderDifference1()
fig4 = CasesVsDeaths()
fig5 = GenderDifference2()
fig6 = GenderDifference3()

apps = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

title = {
    'display':'flex',
    'justify-content':'center',
    'font-size':'100px',
    'font-family':'impact'
}

center = {
    'display':'flex',
    'justify-content':'center',
}

apps.layout = row = html.Div(
    [   
        html.Div(
            dbc.Row(
            [
                dbc.Col(html.Div("COVID-19 VIZUALIZER")),
            ],
        ),
        style=title
        ),

        html.H4('Conrad Fogdestam TE19D', style=center),
        html.Br(),

        html.Div(
            dbc.Row(
            [
                dbc.Col(dcc.Graph(id='NationalDailyDeaths', figure=fig1),
                ),
                dbc.Col(dcc.Graph(id='NationalDailyIcuAdmissions', figure=fig2),
                ),
            ],
        ),
        style=center
        ),
        html.Br(),

        html.H5('Deathrate By COVID-19 (%)', style=center),

        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='DeathRate', figure=fig4),
                ),
            ],
        
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='GenderDifferences1', figure=fig3),
                ),
                dbc.Col(dcc.Graph(id='GenderDifferences2', figure=fig6),
                ),
                dbc.Col(dcc.Graph(id='GenderDifferences3', figure=fig6),
                ),


            ]
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div('© 2011-2021 MICRODOSINGLLC™. All Rights Reserved', style=center),
        html.Br(),
        html.Br(),
        html.Br(),
    ],

)

if __name__ == "__main__":
    apps.run_server(debug=True)