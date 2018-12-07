from __future__ import absolute_import, division, print_function
from tensorflow import keras
import requests
import json
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# print(tf.__version__)
FACTORS = 3
LAG = 25
history = []
volume = []
sp = []

def get_data(ticker):
	url = 'https://api.iextrading.com/1.0/stock/' + ticker + '/chart/2y'
	r = requests.get(url)
	raw = json.loads(r.text)

	sp_url = 'https://api.iextrading.com/1.0/stock/SPY/chart/2y'
	r = requests.get(sp_url)
	raw_sp = json.loads(r.text)
	# print(len(raw))
	# history = []
	for element in raw:
		history.append(element["open"])
		volume.append(element["volume"]/10000000)

	for element in raw_sp:
		sp.append(element["open"]/100)

	train_data = np.zeros((len(history)-LAG,FACTORS))
	train_labels = np.zeros((len(history)-LAG,1))

	for i in range(0,len(history)-LAG):
		avg = sum(history[i:i+LAG])/LAG
		temp = avg - history[i+LAG-1]
		train_data[i] = np.array([temp,volume[i+LAG-1],sp[i+LAG-1]])
		train_labels[i] = np.array(history[i+LAG]-avg)
	# print(train_data)
	# print(train_labels)

	# for i in range(0,len(history)-FACTORS-1):
	# 	avg = sum(history[i:i+FACTORS])/FACTORS
	# 	temp = [j - avg for j in history[i:i+FACTORS]]
	# 	train_data[i] = np.array(temp)
	# 	train_labels[i] = np.array(history[i+FACTORS]-avg)

	return (train_data, train_labels)

def build_model(train_data):
	# print(type(train_data))
	# print(train_data.shape)
	model = keras.Sequential([
		keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(train_data.shape[1],)),
		keras.layers.Dense(64, activation=tf.nn.relu),
		keras.layers.Dense(1)
	])
	optimizer = tf.train.RMSPropOptimizer(0.001)
	model.compile(loss='mse', optimizer=optimizer, metrics=['mae'])
	return model

def train(data):
	# print(type(data[0]))
	# print(data[0].shape)
	model = build_model(data[0])

	# mean = train_data.mean(axis=0)
	# std = train_data.std(axis=0)
	# train_data = (train_data - mean) / std
	# test_data = (test_data - mean) / std

	model.fit(data[0], data[1], epochs=10)
	return model

def run(ticker):
	(train_data, train_labels) = get_data(ticker)
	model = train((train_data, train_labels))

	avg = sum(history[len(history)-FACTORS:])/FACTORS
	temp = np.array([np.array([j - avg for j in history[len(history)-FACTORS:]])])
	# print(temp.shape)
	train_data = np.zeros((1,FACTORS))

	avg = sum(history[len(history)-LAG:])/LAG
	temp = avg - history[len(history)-1]
	train_data[0] = np.array([temp,volume[len(history)-1],sp[len(history)-1]])

	test_prediction = model.predict(train_data)
	print(test_prediction[0][0]+avg)

	test_predictions = model.predict(train_data).flatten()
	error = test_predictions - train_labels.flatten()
	print(sum(error)/len(error))

	return(round(test_prediction[0][0]+avg, 2))


if __name__ == '__main__':
	run("amzn")
	# get_data("aapl")
	# model = build_model()
	# model.summary()