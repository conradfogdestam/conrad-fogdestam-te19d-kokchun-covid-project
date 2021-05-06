#imports
import pandas as pd
import matplotlib.pyplot as plt

#funktion som gör en barchart för National daily deaths
def NationalDailyDeaths():
    dfndd = pd.read_csv('National_Daily_Deaths.csv') #däser in csv filen

#använder Datum som x axel och height den andra columnen national dily deaths
    plt.bar(x=dfndd['Date'], height=dfndd['National_Daily_Deaths']) 
#labels på charten
    plt.title('Nationella Dagliga Dödsfall')
    plt.xlabel('Datum')
    plt.ylabel('Antal Döda Per Dag')
    plt.show()

#funktion för antal ICU admissions per dag på en nationell nivå
def NationalDailyIcuAdmissions():
    dfndd = pd.read_csv('National_Daily_ICU_Admissions.csv')
#bar chart för med labels som visar efter datum
    plt.bar(x=dfndd['Date'], height=dfndd['National_Daily_ICU_Admissions'])
    plt.show()


#funktion för att räkna death rate för covid 19 inom sverige
def CasesVsDeaths():
    #räknar totala summan av både national deaths och national cases
    dfndd = pd.read_csv('National_Daily_Deaths.csv') #däser in csv filen
    sumdeaths = dfndd['National_Daily_Deaths'].sum()
    dfrdc = pd.read_csv('Regional_Daily_Cases.csv')
    sumcases = dfrdc['Sweden_Total_Daily_Cases'].sum()

#pie charten med labels och legends, explode och allt sånt fint
    sizes = [sumcases, sumdeaths]
    explode = (0, 0.1)
    mylabels = ['Cases', 'Deaths']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=mylabels, autopct='%1.1f%%',
            shadow=True, startangle=180)
    plt.title("Deathrate by COVID-19", bbox={'facecolor':'1'}) #title
    plt.legend()
    plt.show()

CasesVsDeaths()
