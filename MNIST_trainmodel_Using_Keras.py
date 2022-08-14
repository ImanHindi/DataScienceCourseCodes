from calendar import EPOCH
import numpy as np
import mnist 
from tensorflow import keras
from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Conv2D, MaxPooling2D,Dense,Flatten

from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder
from tensorflow.keras.utils import to_categorical
train_images=mnist.train_images()
train_labels=mnist.train_labels()

print(train_images.shape)
print(train_labels.shape)



test_images=mnist.test_images()
test_labels=mnist.test_labels()


train_images=(train_images/255)-.5
test_images=(test_images/255)-.5

train_images=np.expand_dims(train_images,axis=3)
test_images=np.expand_dims(test_images,axis=3)
#train_images=np.array(train_images)
print(train_images.shape)

#encoding part:
#le=LabelEncoder()
#train_labels=le.fit_transform(train_labels)
#ohe=OneHotEncoder(categories=[0])
#train_labels=ohe.fit_transform(train_labels).toarray()
train_labels=to_categorical(train_labels)
test_labels=to_categorical(test_labels)

#model=keras.Sequential()


num_filters=8
filter_size=3
pool_size=2

model=Sequential([
    Conv2D(num_filters,filter_size,input_shape=(28,28,1)),
    MaxPooling2D(pool_size),
    Flatten(),
    Dense(10,activation='softmax')
])
model.compile('adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
model.fit(train_images,train_labels,epochs=3,validation_data=(test_images,test_labels))
model.summary()
model.save_weights('MnistModel.h5')

model.load_weights('MnistModel.h5')
prediction=model.predict(test_images[:5])
print(np.argmax(prediction,axis=1))

print(np.argmax(test_labels[:5],axis=1))