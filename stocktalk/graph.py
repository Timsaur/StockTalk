import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from functools import wraps
from flask import g, request, redirect, url_for, session


def my_plotter(time, price): 
	plt.plot(time, price)
	plt.xlabel('Time')
	plt.ylabel('Price')
	plt.title('Stock Lookup')
	buf = io.BytesIO()
	plt.savefig(buf, format='png')
	buf.seek(0)
	buffer = b''.join(buf)
	b2 = base64.b64encode(buffer)
	fig2=b2.decode('utf-8')
	return fig2

#via http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("login")
        return f(*args, **kwargs)
    return decorated_function

