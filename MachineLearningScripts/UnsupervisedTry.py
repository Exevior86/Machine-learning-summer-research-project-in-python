# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:59:49 2020
* 9  data points from Source IP, Dest IP, PacketSize, source port, dest port, Temp, Tasks, CPU, Memory used
@author: Adam
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from sklearn.ensemble import IsolationForest


data = pd.read_csv('C:/Users/Adam/Desktop/DataSet/DataSetDataCombinedNW.csv')
data2 = pd.read_csv('C:/Users/Adam/Desktop/DataSet/IdleDataBenign.csv')
data3 = pd.read_csv('C:/Users/Adam/Desktop/DataSet/Combined/CombinedDataLabeledUnsupervisedReady.csv')
array = data.values
array2 = data2.values
array3 = data3.values
x = array[:,0:8]
y = array[:,9]
a = array3[:, 0:9]
b = array3[:, 9]

