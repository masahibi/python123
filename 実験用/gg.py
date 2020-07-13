import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname='C:\WINDOWS\Fonts\msgothic.ttc', size=14)
fname='OneDrive\デスクトップ\実験用\ex1.xlsx'
sname='Sheet1'
dataframe = pd.read_excel(fname, sheet_name=sname)
#print(dataframe)

values = dataframe.values
#print(values)

dataframe_label = dataframe.columns
ROOMTEMPERATURE1 = 23.0
ROOMTEMPERATURE2 = 25.2
ROOMTEMPERATURE3 = 24.5
time = values[:,0]
temperature1 = values[:,1] - ROOMTEMPERATURE1
temperature2 = values[:,2] - ROOMTEMPERATURE2
temperature3 = values[:,3] - ROOMTEMPERATURE3
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
ax.plot(time, temperature1, 'bo', label=dataframe_label[1][:])
ax.plot(time, temperature2, 'go', label=dataframe_label[2][:])
ax.plot(time, temperature3, 'ro', label=dataframe_label[3][:])
ax.set_yscale('log')
ax.grid(which='both')
ax.set_yticks(np.arange(35.0, 70.0, 10.0))
ax.set_xlabel('経過時間(分)', fontproperties=fp)
ax.set_ylabel('(測定温度‐室温)(℃)', fontproperties=fp)
ax.legend(prop=fp)
plt.show()

