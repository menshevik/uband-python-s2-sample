from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	jsonfile = open('static/data/index.json', 'r+')
	jsontext = jsonfile.read()
	data = json.loads(jsontext)
	print data
	return render_template('index.html', data = data)


if __name__ == '__main__':
    app.run(debug=True)