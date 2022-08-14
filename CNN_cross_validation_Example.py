import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.model_selection import cross_val_score




x,y =load_iris(return_X_y=True)
model=svm.SVC()
accuracy=cross_val_score(model,x,y,scoring='accuracy',cv=10)

print(accuracy.mean()*100)