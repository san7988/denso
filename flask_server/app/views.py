from flask import render_template, jsonify, request
import base64
from app import app
import os
import json
import recognizer as rg
import shutil
import random
import datetime
import time
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

@app.route('/todo/api/v1.0/tasks2', methods=['POST'])
def get_tasks():
	testdata = request.data
	testdata = base64.b64decode(testdata[33:-2])
	if not testdata or len(testdata)<=0:
		return jsonify({"tasks":tasks})
	else:
		shutil.rmtree("app/test_images")
		os.makedirs("app/test_images")
		filename = "test.jpg"
		with open(os.path.join("app/test_images",filename), 'wb') as f:
			f.write(testdata)
		match = rg.test_on_face(os.path.join("app/test_images",filename))
		#match="sanjeev"
		return jsonify({'result': match})

@app.route('/api/test_tasks', methods=['GET'])
def post_tasks():
	randNum = random.randint(1,101)
	ts = time.time()
	dt = datetime.datetime.fromtimestamp(ts).strftime('%H:%M')
	tasks_tas = {'myData': randNum, 'timeStamp': dt}
	return jsonify({"tasks": tasks_tas})


