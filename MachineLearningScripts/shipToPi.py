#import ProgramA
#import toCSV
import sklearn
import pandas as pd
import numpy as np
from sklearn.externals import joblib 
import pickle

data = pd.read_csv('CombinedCsvWithGames')
array = data.values
x = array[:,0:5]
#y = array[:,6]
filename = 'MalwareDetectionModel4.pkl'
model = pickle.load(open(filename, 'rb'))
result = model.predict(x)
print(result)