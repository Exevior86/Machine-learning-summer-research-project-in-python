#import ProgramA
#import toCSV
import sklearn
import pandas as pd
import numpy as np
from sklearn.externals import joblib 
import pickle

# A script to test loading a machine learning model to the raspberry pi
# to make predictions on the device after training the model.

data = pd.read_csv('CombinedCsvWithGames')
array = data.values
x = array[:,0:5]
#y = array[:,6]
filename = 'MalwareDetectionModel4.pkl'
model = pickle.load(open(filename, 'rb'))
result = model.predict(x)
print(result)
