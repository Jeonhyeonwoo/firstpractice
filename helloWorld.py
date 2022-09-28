import sys
import matplotlib.pyplot as plt
input = sys.stdin.readline
import numpy as np
import pandas as pd

data = np.random.binomial(n=1, p=0.5, size=1000)

x = []
coin_cnt = 0
y = []
idx = 1
i = 0

while idx != 1000:
    x.append(idx)
    idx+=1

while i != 1000:
  if data[i] == 0: 
    coin_cnt+=1
  
  if i == 0:
    y.append(0.0)
  else:
    y.append(coin_cnt/i)
  i+=1

plt.title('Coin : p(H)=' + str(sum(data)/1000))
plt.grid()
plt.plot(x,y,linestyle = '-')
plt.show()