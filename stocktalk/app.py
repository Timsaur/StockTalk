import os
import psycopg2
import matplotlib.pyplot as plt
import numpy as np
#import test
from graph import *
from flask import Flask, render_template, g, request, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import create_engine
import graph
import json
import requests
from predict import *

# postgresql-spherical-72286
ticker = "help"
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')
db = create_engine('postgres://arbizklxkkfsjo:742246e607fcaaa7b1faf6e7dab54d082f551bd9abeeb3e51a4ef19dd3cca5bb@ec2-54-204-36-249.compute-1.amazonaws.com:5432/dcgq0vpeghnls2')

# db.execute("CREATE TABLE users (id int, username varchar(255), password varchar(255))")
# db.execute("CREATE TABLE stocks (id int, username varchar(255), stock varchar(255))")
# db = create_engine('postgres://arbizklxkkfsjo:742246e607fcaaa7b1faf6e7dab54d082f551bd9abeeb3e51a4ef19dd3cca5bb@ec2-54-204-36-249.compute-1.amazonaws.com:5432/dcgq0vpeghnls2')

# db.execute("CREATE TABLE stocks (id int, username varchar(255), ticker varchar(255))")

# DATABASE_URL = os.environ['DATABASE_URL']
# print(os.environ)
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
	if request.method == "POST":
		if not request.form.get("symbol"):
			return redirect("/")
		symbol = request.form.get("symbol")
		try:
			result = run(symbol)
		except:
			return render_template("base.html")
		ticker = symbol
		url = 'https://api.iextrading.com/1.0/stock/' + symbol + '/chart/2y'
		r = requests.get(url)
		raw = json.loads(r.text)
		data=[]
		open_price=[]
		date = []
		for element in raw:
			open_price.append(element["open"])
			date.append(element["date"])
		data.append({"date":date[len(date)-1],"open":raw[len(raw)-1]["open"], "volume":raw[len(raw)-1]["volume"], "close":raw[len(raw)-1]["close"], "predict":run(symbol), "ticker":symbol.upper()})
		return render_template("result.html", data=data)
	return render_template("base.html")

@app.route('/result', methods=['POST'])
@login_required
def result():
	db.execute("INSERT INTO stocks (username, stock) VALUES ('%s', '%s')" % (session.get("username"), ticker))
	return redirect("bookmarks")


@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("login.html")

        elif not request.form.get("password"):
            return render_template("login.html")

        rows = db.execute("SELECT * FROM users WHERE username = '%s'" % (request.form.get("username")))
        fetch = rows.fetchall()

        if not fetch or not check_password_hash(fetch[0]["password"], request.form.get("password")):
            return render_template("login.html")

        if len(fetch) == 0 or not check_password_hash(fetch[0]["password"], request.form.get("password")):
            return render_template("login.html")

        session["user_id"] = request.form.get("username")
        return redirect("/")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("register.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("register.html")

        elif not request.form.get("confirmation"):
            return render_template("register.html")

        # Define username and password, hashing password
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))

        # Query database for username
        try:
            rows = db.execute("SELECT * FROM users WHERE username = ('%s')" % (username))
            fetch = rows.fetchall()
            if len(fetch) >= 1:
                return render_template("register.html")
        except:
        	pass

        # Ensure password and confirmation password are the same
        if request.form.get("password") != request.form.get("confirmation"):
            return render_template("register.html")
        # Insert new user into users
        db.execute("INSERT INTO users (username, password) VALUES ('%s', '%s')" % (username, password))
        return redirect("login")
    return render_template("register.html")

@app.route("/check", methods=["GET"])
def check():
    if not request.args.get("username"):
        return jsonify(False)
    # Check if user input matches any existing username
    elements = db.execute("SELECT * FROM users WHERE username= '%s'" % request.args.get("username"))
    fetch = elements.fetchall()
    if len(fetch) >= 1:
        return jsonify(False)
    # If not, return true
    return jsonify(True)

@app.route("/bookmarks", methods=["GET", "POST"])
@login_required
def history():
    # Select all from purchase_histories so we can choose what to display in the html
    bookmarks = db.execute("SELECT * FROM stocks WHERE username= '%s'" % session.get("username"))
    fetch = bookmarks.fetchall()
    # fetch = [{"ticker":"aapl"},{"ticker":"amzn"}]
    data = []
    for stock in fetch:
        url = 'https://api.iextrading.com/1.0/stock/' + stock["ticker"] + '/chart/2y'
        r = requests.get(url)
        raw = json.loads(r.text)
        open_price=[]
        date = []
        for element in raw:
            open_price.append(element["open"])
            date.append(element["date"])
        #graph = graph.my_plotter(ax, open_price[len(open_price)-30:], date[len(open_price)-30:])
        data.append({"date":date[len(date)-1],"open":raw[len(raw)-1]["open"], "volume":raw[len(raw)-1]["volume"], "close":raw[len(raw)-1]["close"], "predict":run(stock["ticker"]), "ticker":stock["ticker"].upper()})

    return render_template("bookmarks.html", data=data)
