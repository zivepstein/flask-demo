from flask import Flask, render_template,url_for
app = Flask(__name__)
#connect to psql

@app.route('/<user>')
def hello_world(user):
	return render_template('index.html', user = user)

@app.route('/bio/<dingus>')
def bio_page(dingus):
	return "this is my bio!" + dingus	

@app.route('/login/<dingus>')
def bio_page(dingus):
	return "this is my bio!" + dingus		


if __name__ == '__main__':
	app.debug = True
	app.run()