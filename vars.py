obj = {
    "code": {
        "file": "kipu.py",
        "imports": {
            "first_import": "from flask import Flask, render_template",
            "second_import": "from vars import obj"
        },
        "app_definition": "app = Flask(__name__)",
        "controllers": [
            {
                "decorator": "@app.route('/home')",
                "name": "def home():",
                "content": "return render_template('home.html')"
            },
            {
                "decorator": "@app.route('/code')",
                "name": "def code():",
                "content": "return jsonify(**obj)"
            },
            {
                "decorator": "@app.route('/getcode')",
                "name": "def getcode():",
                "content": "return render_template('source.html')"
            }
        ],
        "app_run": {
            "condition": "if __name__ == '__main__':",
            "content": "app.run()"
        }
    }

}
