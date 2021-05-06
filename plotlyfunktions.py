import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def NationalDailyDeaths():
    ndd = pd.read_csv('National_Daily_Deaths.csv')
    fig = px.bar(ndd, x= 'Date', y='National_Daily_Deaths')
    return fig
    
def NationalDailyIcuAdmissions():
    ndicua = pd.read_csv('National_Daily_ICU_Admissions.csv')
    fig = px.bar(ndicua, x='Date', y='National_Daily_ICU_Admissions')
    return fig

def CasesVsDeaths():
    dfndd = pd.read_csv('National_Daily_Deaths.csv') #däser in csv filen
    sumdeaths = dfndd['National_Daily_Deaths'].sum()
    dfrdc = pd.read_csv('Regional_Daily_Cases.csv')
    sumcases = dfrdc['Sweden_Total_Daily_Cases'].sum()

    labels = ['Cases', 'Deaths']
    values = [sumcases, sumdeaths]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    return fig

