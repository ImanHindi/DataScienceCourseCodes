from matplotlib import pyplot as plt
from sklearn.utils import shuffle
import tensorflow.keras as keras
import tensorflow.keras.layers as layers
from tensorflow.keras.datasets import mnist
import numpy as np
from tensorflow.keras import regularizers


input_img = keras.Input(shape=(28, 28, 1))

encoded = layers.Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
encoded = layers.MaxPooling2D((2, 2), padding='same')(encoded)
encoded = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
encoded = layers.MaxPooling2D((2, 2), padding='same')(encoded)
encoded = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
encoded = layers.MaxPooling2D((2, 2), padding='same')(encoded)

decoded = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
decoded = layers.UpSampling2D((2, 2))(decoded)
decoded = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(decoded)
decoded = layers.UpSampling2D((2, 2))(decoded)
decoded = layers.Conv2D(16, (3, 3), activation='relu')(decoded)
decoded = layers.UpSampling2D((2, 2))(decoded)
decoded = layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(decoded)

autoencoder=keras.Model(input_img,decoded)

#encoder = keras.Model(input_img, encoded)
#
#encoded_input = keras.Input(shape=(32,))
#
#decoder_layer = autoencoder.layers[-1]
#decoder = keras.Model(encoded_input, decoder_layer(encoded_input))

autoencoder.compile(optimizer='adam',loss='binary_crossentropy')
(x_train,_),(x_test,_)=mnist.load_data()

x_train=x_train.astype('float32')/255.
x_test=x_test.astype('float32')/255.
#x_train=x_train.reshape(len(x_train),np.prod(x_train.shape[1:]))
#x_test=x_test.reshape(len(x_test),np.prod(x_test.shape[1:]))

autoencoder.fit(x_train,x_train,
epochs=1,
batch_size=256,
shuffle=True,
validation_data=(x_test,x_test))

#encoded_imgs=encoder.predict(x_test)
#decoded_imgs=decoder.predict(encoded_imgs)
decoded_imgs=autoencoder.predict(x_test)
n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
    # Display original
    ax = plt.subplot(2, n, i+1)
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Display reconstruction
    ax = plt.subplot(2, n, i +1+ n)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()