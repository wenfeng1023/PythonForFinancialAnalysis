from typing import List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyecharts.options as opts
from pyecharts.charts import Line

def ReadData(file):
    data = pd.read_csv(file)    
    return data


data = ReadData("AAPL.csv")
list = data['Close']


Drawdown = (np.maximum.accumulate(list) - list) /np.maximum.accumulate(list)
l = np.argmax((np.maximum.accumulate(list) - list) /np.maximum.accumulate(list))
k = np.argmax(list[:l])
mdd = (list[k] - list[l])/(list[k])
print(Drawdown[l])
print(mdd)
print(len(Drawdown))

plt.plot(data['Date'], Drawdown)
plt.show()






