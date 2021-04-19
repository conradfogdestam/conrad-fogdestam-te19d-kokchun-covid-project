import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('National_Daily_Deaths.csv')

df = pd.DataFrame(data)
  
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
  
# Plot the data using bar() method
plt.bar(X, Y, color='r')
plt.title("NATIONAL DAILY DEATHS")
plt.xlabel("DATE")
plt.ylabel("NUMBER OF DEATHS")
  
plt.show()


