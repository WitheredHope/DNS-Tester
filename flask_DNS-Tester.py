from flask import Flask
app = Flask(__name__)

file = open("pretty.txt", "r")
data = str(file.read())

@app.route("/")
def output():
    return data
