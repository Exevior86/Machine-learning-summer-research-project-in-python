#import ProgramA
#import toCSV
#import sklearn
#import pandas as pd
import numpy as np

# Used on raspberry pi to predict data collected, a test to see
# if the device could run it and at what cost.

data = pd.read_csv('CombinedCsvyep.csv')
filename = 'MalwareDetectionModel.sav'
model = joblib.load(filename)
result = model.predict(data)
print(result)
