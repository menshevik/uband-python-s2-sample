from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

def read_json(filepath):
	jsonfile = open(filepath, 'r+')
	jsontext = jsonfile.read()
	data = json.loads(jsontext)
	return data

@app.route('/')
def hello_world():
	data = read_json('static/data/index.json')
	print data
	return render_template('index.html', data = data)

@app.route('/details/<string:student_number>')
def show_details(student_number):
	print 'details'
	data = read_json('static/data/index.json')
	user_data ={}
	for item in data:
		if item['student_number'] == student_number:
			user_data = item
			break
	return render_template('/details.html', data=user_data)

if __name__ == '__main__':
    app.run(debug=True)