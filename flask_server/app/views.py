from flask import render_template, jsonify, request
import base64
from app import app
import os
import json
import shutil
import random
import datetime
import time
import sense
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

tasks = [
	{
		'id': 1,
		'title': u'Buy groceries',
		'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
		'done': False
	},
	{
		'id': 2,
		'title': u'Learn Python',
		'description': u'Need to find a good Python tutorial on the web', 
		'done': False
	}
]

@app.route('/api/send_data', methods=['GET'])
def post_tasks():
        '''
	sensorData = sense.sen(22)
	'''
        sensorData = random.randint(1,101)
	ts = time.time()
	dt = datetime.datetime.fromtimestamp(ts).strftime('%H:%M')
	dataToSend = {'myData': sensorData, 'timeStamp': dt}
	return jsonify({"tasks": dataToSend})

@app.route('/api/rcv_instruction', methods=['POST'])
def receive_instruction():
	instruction = request.data
        
	return jsonify({"retData": instruction})


