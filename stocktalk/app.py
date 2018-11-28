import os
import psycopg2
from flask import Flask, render_template, g


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')