from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	# Prepare some data to pass to the template (optional)
	greeting = "Welcome to the Violin Learner App!"
	return render_template('index.html', greeting=greeting)

if __name__ == "__main__":
	app.run(debug=True, port=5547)
