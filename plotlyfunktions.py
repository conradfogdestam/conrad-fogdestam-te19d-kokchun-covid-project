import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

def NationalDailyDeaths():
    nationaldailydeaths = pd.read_csv('National_Daily_Deaths.csv')
    fig = px.bar(nationaldailydeaths, x= 'Date', y='National_Daily_Deaths')
    return fig

def NationalDailyIcuAdmissions():
    nationaldailyicuadmissions = pd.read_csv('National_Daily_ICU_Admissions.csv')
    fig = px.bar(nationaldailyicuadmissions, x='Date', y='National_Daily_ICU_Admissions')
    return fig

def CasesVsDeaths():
    dfnationaldailydeaths = pd.read_csv('National_Daily_Deaths.csv') #däser in csv filen
    sumdeaths = dfnationaldailydeaths['National_Daily_Deaths'].sum()
    dfregionaldailycases = pd.read_csv('Regional_Daily_Cases.csv')
    sumcases = dfregionaldailycases['Sweden_Total_Daily_Cases'].sum()

    labels = ['Total Cases', 'Deaths']
    values = [sumcases, sumdeaths]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    return fig


def GenderDifference():
    dfgenderdata = pd.read_csv('Gender_Data.csv')
    fig = px.bar(dfgenderdata, x='Gender', y='Total_Deaths')
    return fig
