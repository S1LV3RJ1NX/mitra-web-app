# This file is used to host MITRA bot website

# Imports
import os, sys
from flask import Flask, request, render_template

# Registering the app
app = Flask(__name__, static_url_path='/static')


@app.route('/', methods = ['GET'])
def index():
	"""This function renders the index page on GET request
	"""
	return render_template('index.html')

def log(message):
	"""Useful to log messages to server
	"""
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
	app.run(debug = True, port = 5000)