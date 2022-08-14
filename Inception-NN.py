import tensorflow.keras as keras
import tensorflow.keras.layers as layers
from tensorflow.keras.datasets import mnist, cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import SGD
import numpy as np


(X_train, y_train), (X_test, y_test) = cifar10.load_data()
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train / 255.0
X_test = X_test / 255.0

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


input_img = layers.Input(shape = (32, 32, 3))

tower_1 = layers.Conv2D(64, (1,1), padding='same', activation='relu')(input_img)
tower_1 = layers.Conv2D(64, (3,3), padding='same', activation='relu')(tower_1)
tower_2 = layers.Conv2D(64, (1,1), padding='same', activation='relu')(input_img)
tower_2 = layers.Conv2D(64, (5,5), padding='same', activation='relu')(tower_2)
tower_3 = layers.MaxPooling2D((3,3), strides=(1,1), padding='same')(input_img)
tower_3 = layers.Conv2D(64, (1,1), padding='same', activation='relu')(tower_3)


output = keras.layers.concatenate([tower_1, tower_2, tower_3], axis = 3)
output = layers.Flatten()(output)
out    = layers.Dense(10, activation='softmax')(output)

model = keras.Model(inputs = input_img, outputs = out)


epochs = 25
lrate = 0.01
decay = lrate/epochs
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=32)

scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))