import os, sys
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html')

def log(message):
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
	app.run(debug = True, port = 5000)