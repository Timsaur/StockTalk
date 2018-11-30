import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def my_plotter(ax, time, price):
	ax.plot(time, price)
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
