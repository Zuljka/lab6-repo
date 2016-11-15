from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	return "Hello Flasj from DIT DT228 Program!"
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=500, debug=True)
