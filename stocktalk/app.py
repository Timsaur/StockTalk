import os
import psycopg2
import matplotlib.pyplot as plt
import numpy as np
import test
from flask import Flask, render_template, g, request


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		data = {'Jan': 10, 'Feb': 15, 'Mar': 5, 'Apr': 20}
		time = list(data.keys())
		price = list(data.values())
		fig=test.my_plotter(ax, time, price)
		#if not request.form.get("symbol"):
        	#return render_template("base.html")
		# result = lookup(request.form.get("symbol"))
		# if result == None:
		# 	return render_template("base.html")
		return render_template("result.html", fig=fig)
	return render_template("base.html")
