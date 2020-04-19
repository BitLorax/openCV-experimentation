
import time
import tensorflow as tf
import numpy as np
import cv2

(xTrain, yTrain), (xTest, yTest) = tf.keras.datasets.fashion_mnist.load_data()
(xTrain, xValid) = xTrain[5000:], xTrain[:5000]
(yTrain, yValid) = yTrain[5000:], yTrain[:5000]

w, h = 28, 28
xTrain = xTrain.reshape(xTrain.shape[0], w, h, 1)
xValid = xValid.reshape(xValid.shape[0], w, h, 1)
xTest = xTest.reshape(xTest.shape[0], w, h, 1)

yTrain = tf.keras.utils.to_categorical(yTrain, 10)
yValid = tf.keras.utils.to_categorical(yValid, 10)
yTest = tf.keras.utils.to_categorical(yTest, 10)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=2, padding='same',
          activation='relu', input_shape=(28, 28, 1)))
model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=2, padding='same',
          activation='relu'))
# model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
# model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.summary()
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
score = model.evaluate(xTest, yTest, verbose=0)
print('\n', 'Test accuracy:', score[1])
