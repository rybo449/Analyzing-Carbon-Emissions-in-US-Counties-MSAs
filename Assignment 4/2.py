import pandas as pd
import matplotlib.pyplot as plt
import sys

df = pd.read_csv(sys.argv[1])
#df['population densty'] = df['TOTAL POP IN MSA']/df['TOTAL LAND IN MSA']
df1 = df[['POP DENSITY', 'CO2/CAPITA']]
df1.plot(kind = 'scatter')
plt.show()