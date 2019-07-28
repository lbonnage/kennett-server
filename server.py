from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from configuration import Config

app = Flask(__name__)
CORS(app)



##
# Endpoint for loading the website homepage
##
@app.route("/")
def loadIndex():
	return render_template('index.html')