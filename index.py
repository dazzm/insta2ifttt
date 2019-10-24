from flask import Flask
app = Flask(__name__)

@app.route('/')
def catch_all():    
	return "Welcome visitor"