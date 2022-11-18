from flask import Flask , render_template , request

app = Flask(__name__)
app.secret_key = "hiii"

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/home")                                      
def home():
	return render_template("home.html")

@app.route("/form")                                      
def form():
	return render_template("form.html")
