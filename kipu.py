from flask import Flask, render_template, jsonify
from vars import obj

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/code')
def code():
    return jsonify(**obj)


@app.route('/getcode')
def getcode():
    return render_template("source.html")

if __name__ == '__main__':
    app.run()
