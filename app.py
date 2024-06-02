from flask import Flask, redirect, url_for, render_template, request
import os

app = Flask(__name__)

# Defining the home page of our site
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/start", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("start.html")
    else:
        os.system("python .\Drowsiness_Detection_System_Algo\drowsiness_detection_system.py")
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 50000, debug = True)