from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits


digits=load_digits()

x=digits.data
y=digits.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=20,stratify=y)


knn=KNeighborsClassifier(n_neighbors=6)

knn.fit(x_train,y_train)

print(knn.score(x_test,y_test))