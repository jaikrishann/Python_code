import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

bike = pd.read_csv('Used_Bikes.csv')

bin = [0,5,10,15,20,40]
plt.hist(bike['age'],bin,edgecolor='k')
plt.show()