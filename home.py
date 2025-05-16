from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/dinamica")
def hello_world_dinamica():
    return render_template("dinamica.html")


