import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from datasets1 import ds, kp

train_dataset = ds(18720, 20160)  # для обучения сети
train_kp = kp(0, 8)

test_dataset = ds(20160, 21600)  # для тестирования
test_kp = kp(8, 16)

"""Код нейронки от сюда: https://habr.com/ru/articles/426797/"""

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(3400, 1)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(100, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.optimizers.Adam(learning_rate = 0.001), # tf.train.AdamOptimizer() не существует, изменил на то что есть
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(train_dataset, train_kp, epochs=50) # 50 єпох обучения, я пробовал и больше и меньше - лучше не становиться вроде бы

print("TEST")
test_loss, test_acc = model.evaluate(test_dataset, test_kp) # пишет процент правильных ответов исходя из тестирующего датасета
print('Test accuracy:', test_acc)