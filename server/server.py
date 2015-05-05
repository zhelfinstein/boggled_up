import flask as f

app = f.Flask(__name__)
	

@app.route("/")
def mainPage():
	return f.send_file("../index.html")
	
@app.route("/board", methods=['POST'])
def board():
	return "Hello"
	
@app.route("/favicon.ico")
def func():
	return "what is this...?"
	
@app.route("/run.js")
def run():
	return f.send_file("../run.js")
	
	
if __name__ == "__main__":
	app.run(host="0.0.0.0")