obj = {
    "code": {
        "file": "kipu.py",
        "imports": [
            {
                "descripcion_import": "from flask import Flask, render_template",
                "comment_import": "# Flask framework - install from requirements.txt"
            },
            {
                "descripcion_import": "from vars import obj",
                "comment_import": "# file that contains a json object representing the source code"
            },

        ],

        "app_definition": {
            "definition": "app = Flask(__name__)",
            "comment_definition": "# determine root path"
        },
        "controllers": [
            {
                "decorator": "@app.route('/home')",
                "name": "def home():",
                "content": "return render_template('home.html')",
                "comment": "# router that defines path: /home and returns an html file with the main user interface"
            },
            {
                "decorator": "@app.route('/code')",
                "name": "def code():",
                "content": "return jsonify(**obj)",
                "comment": "# router that defines path: /code and returns a json object with the source code of the app"
            },
            {
                "decorator": "@app.route('/getcode')",
                "name": "def getcode():",
                "content": "return render_template('source.html')",
                "comment": "# router that defines path: /getcode used by home.html via ajax function "
                           "to return an html/text file with the source code of the app and then transform "
                           "it with prettify library and present data in python format to user"
            }
        ],
        "app_run": {
            "condition": "if __name__ == '__main__':",
            "content": "app.run()",
            "comment": "# run the app where we only start the web server whenever this file called directly"
        }
    }

}
