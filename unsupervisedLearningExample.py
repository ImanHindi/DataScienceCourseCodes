#import modules
from sklearn import datasets
import matplotlib.pyplot as plt

#load dataset
df=datasets.load_iris()
print(dir(df))
print(df.target_names)
print(df.target)
print(df.feature_names)
label={0:'red',1:'blue',2:'green'}#only for coloring

#dataset slicing
x_axis=df.data[:,0]#sepal length
y_axis=df.data[:,2]#sepal wedth

#plotting
plt.scatter(x_axis,y_axis,c=df.target)
plt.show()