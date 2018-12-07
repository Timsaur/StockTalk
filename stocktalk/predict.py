from __future__ import absolute_import, division, print_function
from tensorflow import keras
import requests
import json
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sys

FACTORS = 4
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

	for element in raw:
		history.append(element["open"])
		volume.append(element["volume"]/10000000)

	for element in raw_sp:
		sp.append(element["open"]/100)

	train_data = np.zeros((len(history)-LAG,FACTORS))
	train_labels = np.zeros((len(history)-LAG,1))

	for i in range(0,len(history)-LAG):
		avg = sum(history[i:i+LAG])/LAG
		temp = history[i+LAG-1] - avg
		train_data[i] = np.array([temp,avg,volume[i+LAG-1],sp[i+LAG-1]])
		train_labels[i] = np.array(history[i+LAG]-avg)

	return (train_data, train_labels)

def build_model(train_data):
	model = keras.Sequential([
		keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(train_data.shape[1],)),
		keras.layers.Dense(64, activation=tf.nn.relu),
		keras.layers.Dense(1)
	])
	optimizer = tf.train.RMSPropOptimizer(0.001)
	model.compile(loss='mse', optimizer=optimizer, metrics=['mae'])
	return model

def train(data):
	model = build_model(data[0])
	model.fit(data[0], data[1], epochs=10)
	return model

def run(ticker):
	(train_data, train_labels) = get_data(ticker)
	model = train((train_data, train_labels))

	test_data = np.zeros((1,FACTORS))
	avg = sum(history[len(history)-LAG:])/LAG
	temp = history[len(history)-1] - avg
	test_data[0] = np.array([temp,avg,volume[len(history)-1],sp[len(history)-1]])

	test_prediction = model.predict(test_data)
	print("Predicted stock price tomorrow: " + str(test_prediction[0][0]+avg))

	test_predictions = model.predict(train_data).flatten()
	error = test_predictions - train_labels.flatten()
	print("Error of model run on training data: " + str(sum(error)/len(error)))

	return(round(test_prediction[0][0]+avg, 2))


if __name__ == '__main__':
	try:
		run(sys.argv[1])
	except:
		print("Please input a stock ticker symbol.")
