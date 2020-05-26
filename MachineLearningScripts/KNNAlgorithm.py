import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import pickle
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


data = pd.read_csv('AllHostDataCombined.csv')
array = data.values

x = array[:,0:5]
y = array[:,6]

validation_size = .25
seed = 10
x_train, x_validation, y_train, y_validation = model_selection.train_test_split(x, y, test_size=validation_size, random_state=seed)
scoring = 'accuracy'

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

filename = 'MalwareDetectionModel4.pkl'
pickle.dump(knn, open(filename, 'wb'))


