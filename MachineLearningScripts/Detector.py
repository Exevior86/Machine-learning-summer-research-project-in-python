#import ProgramA
#import toCSV
#import sklearn
#import pandas as pd
import numpy as np

data = pd.read_csv('CombinedCsvyep.csv')
filename = 'MalwareDetectionModel.sav'
model = joblib.load(filename)
result = model.predict(data)
print(result)