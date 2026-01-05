from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"<h1>Introduction to Flask-Restful API</h1>"
           

if __name__ == '__main__':
    app.run(port=5500, debug=True)