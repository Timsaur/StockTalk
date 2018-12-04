import os
import psycopg2
from sqlalchemy import create_engine
from flask import Flask, render_template, g

# postgresql-spherical-72286
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

db = create_engine('postgres://arbizklxkkfsjo:742246e607fcaaa7b1faf6e7dab54d082f551bd9abeeb3e51a4ef19dd3cca5bb@ec2-54-204-36-249.compute-1.amazonaws.com:5432/dcgq0vpeghnls2')

db.execute("CREATE TABLE stocks (id int, username varchar(255), ticker varchar(255))")

# DATABASE_URL = os.environ['DATABASE_URL']
# print(os.environ)
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')




@app.route('/')
def index():
    return render_template('base.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')