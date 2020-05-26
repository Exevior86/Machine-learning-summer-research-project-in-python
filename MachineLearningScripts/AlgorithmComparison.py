# This file is kind of a mess and was used for fast comparison of
# many different ML models both supervised and unsupervised

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
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import roc_curve  
from sklearn.metrics import roc_auc_score 
from sklearn.externals import joblib

print('The scikit-learn version is {}.'.format(sklearn.__version__))
print('the joblib version is {}.'.format(joblib.__version__))
data = pd.read_csv('C:/Users/Adam/Desktop/DataSet/DataSetDataCombinedNW.csv')
data2 = pd.read_csv('C:/Users/Adam/Desktop/DataSet/IdleDataBenign.csv')
array = data.values
array2 = data2.values
x = array[:,0:8]
y = array[:,9]
#g = array2[:,0:5]
#h = array2[:,6]
print(y)
print(x)

validation_size = .25
seed = 10
x_train, x_validation, y_train, y_validation = model_selection.train_test_split(x, y, test_size=validation_size, random_state=seed)
scoring = 'accuracy'

models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, x_train, y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
    
fig = plt.figure()
fig.suptitle('Machine Learning Model Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
ax.set_xlabel('Machine Learning Models')
ax.set_ylabel('Accuracy of Predictions')
plt.show()

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
#predictions = knn.predict(x_validation)
predictions2 = knn.predict(x_validation)
print(predictions2)
print(accuracy_score(y_validation, predictions2))
print(confusion_matrix(y_validation, predictions2))
print(classification_report(y_validation, predictions2))

filename = 'MalwareDetectionModel4.pkl'
pickle.dump(knn, open(filename, 'wb'))

def plot_roc_curve(fpr, tpr):  
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()

probs = knn.predict_proba(x_validation)     
probs = probs[:, 1] 
auc = roc_auc_score(y_validation, probs)  
print('AUC: %.2f' % auc) 
fpr, tpr, thresholds = roc_curve(y_validation, probs) 
plot_roc_curve(fpr, tpr)    

cm = confusion_matrix(y_validation, predictions2)
plt.clf()
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Wistia)
classNames = ['Negative','Positive']
plt.title('KNN with host and network data confusion matrix')
plt.ylabel('True label')
plt.xlabel('Predicted label')
tick_marks = np.arange(len(classNames))
plt.xticks(tick_marks, classNames, rotation=45)
plt.yticks(tick_marks, classNames)
s = [['TN','FP'], ['FN', 'TP']]
for i in range(2):
    for j in range(2):
        plt.text(j,i, str(s[i][j])+" = "+str(cm[i][j]))
plt.show()
 
