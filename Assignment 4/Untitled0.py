
# coding: utf-8

# In[31]:

import pandas as pd
import matplotlib.pyplot as plt
import sys
plt.style.use('bmh')
print plt.style.available


# In[34]:

df = pd.read_csv('final.csv')
df['CO2 density'] = df['TOTAL CO2 IN MSA']/df['TOTAL POP IN MSA']*10000
df1 = df[['POP DENSITY', 'TOTAL CO2 IN MSA', 'CO2/CAPITA', 'CO2 density', 'TOTAL POP IN MSA']]
print df1.head()


# In[41]:

from sklearn.svm import SVR
import numpy as np
import statsmodels.api as sm
print np.log(df1['TOTAL POP IN MSA']).head()
#z = np. polyfit(df1['CO2 density'], np.log(df1['TOTAL POP IN MSA']),  3)

z = np. polyfit(np.log(df1['POP DENSITY']), df1['CO2 density'], 2)
f = np.poly1d(z)
#x_new = np.linspace(min(df1['CO2 density']), max(df1['CO2 density']), 100)

x_new = np.linspace(min(np.log(df1['POP DENSITY'])), max(np.log(df1['POP DENSITY'])), 100)
y_new = f(x_new)


# In[42]:

from math import log
plt.scatter(np.log(df1['POP DENSITY']), df1['CO2 density'])#, '.b')

plt.plot(np.log(df1['POP DENSITY']), df1['CO2 density'], 'o', x_new,y_new)
plt.title('Plot of Carbon Emissions as Population Density of the MSA Increases')
plt.xlabel('Population Density')
plt.ylabel('CO2 emission per person')
plt.show()


# In[25]:




# In[ ]:



