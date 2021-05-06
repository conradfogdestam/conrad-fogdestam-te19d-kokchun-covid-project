import pandas as pd
import matplotlib.pyplot as plt


def NDD():
    dfndd = pd.read_csv('National_Daily_Deaths.csv')
    plt.bar(x=dfndd['Date'], height=dfndd['National_Daily_Deaths'])
        
    plt.show()

NDD()





