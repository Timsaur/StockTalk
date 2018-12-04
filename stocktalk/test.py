from __future__ import absolute_import, division, print_function
import tensorflow as tf
import requests
import json
from tf import keras
import numpy as np


def get_data(ticker):
	url = 'https://api.iextrading.com/1.0/stock/' + ticker + '/chart/2y'
	r = requests.get(url)
	raw = json.loads(r.text)

	sp_url = 'https://api.iextrading.com/1.0/stock/SPY/chart/2y'
	r = requests.get(sp_url)
	raw_sp = json.loads(r.text)

	history = []
	volume = []
	sp = []

	for element in raw:
		history.append(element["open"])
		volume.append(element["volume"])

	for element in raw_sp:
		sp.append(element["open"])

	temp = sum(history)/len(history)
	history = [x / temp for x in history]
	temp = sum(volume)/len(volume)
	volume = [x / temp for x in volume]
	temp = sum(sp)/len(sp)
	sp = [x / temp for x in sp]

	print(history[len(history)-10:])
	print(volume[len(history)-10:])
	print(sp[len(history)-10:])

get_data("aapl")
# print(tf.__version__)

# boston_housing = keras.datasets.boston_housing

# (train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()

# # Shuffle the training set
# order = np.argsort(np.random.random(train_labels.shape))
# train_data = train_data[order]
# train_labels = train_labels[order]

# # print("Training set: {}".format(train_data.shape))  # 404 examples, 13 features
# # print("Testing set:  {}".format(test_data.shape))   # 102 examples, 13 features

# # import pandas as pd

# # column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
# #                 'TAX', 'PTRATIO', 'B', 'LSTAT']

# # df = pd.DataFrame(train_data, columns=column_names)
# # df.head()

# # Test data is *not* used when calculating the mean and std

# mean = train_data.mean(axis=0)
# std = train_data.std(axis=0)
# train_data = (train_data - mean) / std
# test_data = (test_data - mean) / std

# # print(train_data[0])  # First training sample, normalized

# print(type(train_data))
# print(type(train_labels))

# print(train_data.shape)
# # print(train_data[0])
# # print(train_labels[0])

# def build_model():
#   model = keras.Sequential([
#     keras.layers.Dense(64, activation=tf.nn.relu,
#                        input_shape=(train_data.shape[1],)),
#     keras.layers.Dense(64, activation=tf.nn.relu),
#     keras.layers.Dense(1)
#   ])

#   optimizer = tf.train.RMSPropOptimizer(0.001)

#   model.compile(loss='mse',
#                 optimizer=optimizer,
#                 metrics=['mae'])
#   return model

# # exit(0)
# model = build_model()
# # model.summary()

# # Display training progress by printing a single dot for each completed epoch
# class PrintDot(keras.callbacks.Callback):
#   def on_epoch_end(self, epoch, logs):
#     if epoch % 100 == 0: print('')
#     print('.', end='')

# EPOCHS = 500

# # Store training stats
# history = model.fit(train_data, train_labels, epochs=EPOCHS,
#                     validation_split=0.2, verbose=0,
#                     callbacks=[PrintDot()])

# import matplotlib.pyplot as plt


# def plot_history(history):
#   plt.figure()
#   plt.xlabel('Epoch')
#   plt.ylabel('Mean Abs Error [1000$]')
#   plt.plot(history.epoch, np.array(history.history['mean_absolute_error']),
#            label='Train Loss')
#   plt.plot(history.epoch, np.array(history.history['val_mean_absolute_error']),
#            label = 'Val loss')
#   plt.legend()
#   plt.ylim([0, 5])

# plot_history(history)

# model = build_model()

# # The patience parameter is the amount of epochs to check for improvement
# early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)

# history = model.fit(train_data, train_labels, epochs=EPOCHS,
#                     validation_split=0.2, verbose=0,
#                     callbacks=[early_stop, PrintDot()])

# plot_history(history)

# print(test_data.shape)

# test_predictions = model.predict(test_data).flatten()

# plt.scatter(test_labels, test_predictions)
# plt.xlabel('True Values [1000$]')
# plt.ylabel('Predictions [1000$]')
# plt.axis('equal')
# plt.xlim(plt.xlim())
# plt.ylim(plt.ylim())
# _ = plt.plot([-100, 100], [-100, 100])

# print(test_predictions)
