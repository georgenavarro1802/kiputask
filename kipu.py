# Flask framework - install from requirements.txt
from flask import Flask, render_template, jsonify

# file that contains a json object representing the source code
from vars import obj

# determine root path
app = Flask(__name__)


# router that defines paths: / and /home it returns an html file with the main user interface
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


# router that defines path: /code and returns a json object with the source code of the app
@app.route('/code')
def code():
    return jsonify(**obj)


# router that defines path: /getcode used by home.html via ajax function to return an html/text file with
# the source code of the app and then transform it with prettify library and present data in python format to user
@app.route('/getcode')
def getcode():
    return render_template("source.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


# run the app where we only start the web server whenever this file called directly
if __name__ == '__main__':
    app.run()
