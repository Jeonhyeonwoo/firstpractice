import sys
import matplotlib.pyplot as plt
input = sys.stdin.readline
import numpy as np
import pandas as pd

can = np.array([101.8, 101.5, 102.6, 101, 101.8, 96.8, 102.4, 100
                ,98.8, 98.1,98.8, 98, 99.4, 95.5, 100.1, 100.5, 97.4
                ,100.2, 101.4, 98.7,101.4, 99.4, 101.7, 99, 99.7, 98.9
                ,99.5, 100, 99.7, 100.9,99.7, 99, 98.8, 99.7, 100.9, 99.9
                ,97.5, 101.5, 98.2, 99.2,98.6, 101.4, 102.1, 102.9, 100.8
                ,99.4, 103.7, 100.3, 100.2, 101.1,101.8, 100, 101.2, 100.5
                ,101.2, 101.6, 99.9, 100.5, 100.4, 98.1,100.1, 101.6, 99.3
                ,96.1, 100, 99.7, 99.7, 99.4, 101.5, 100.9,101.2, 99.9, 99.1
                ,100.7, 100.8, 100.8, 101.4, 100.3, 98.4,97.2])

k = 5
w = (np.max(can) - np.min(can) + 1) / k
x0 = np.min(can) - 0.5 
x1 = x0 + w
x2 = x1 + w
x3 = x2 + w
x4 = x3 + w
x5 = x4 + w

tmp = []
for i in can:
    if x0 <= i < x1:
        tmp.append('A')
    elif x1 <= i < x2:
        tmp.append('B')
    elif x2 <= i < x3:
        tmp.append('C')
    elif x3 <= i < x4:
        tmp.append('D')
    elif x4 <= i < x5:
        tmp.append('E')

can2 = np.array(tmp)
table1 = pd.crosstab(index = can2, colnames=['can range'], columns='Frequency',margins=True)
table1.index = ['95~96.84','96.84~98.68','98.68~100.52','100.52~102.36','102.36~104.2','Total']

for i in range(5):
    table1.iloc[i,1] = table1.iloc[i,1]/table1.iloc[5,0]

table1.rename(columns= {'All':'Relative Freq'}, inplace=True)
print(table1)

plt.barh(table1.index,table1['Frequency'],color='pink')
plt.show()

