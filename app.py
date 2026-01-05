from flask import Flask

app = FLASK(__name__)

@app.route('/')
def index():
    return f"<h1>Introduction to Flask-Restful API</h1>"
           

if __name__ == '__name__':
    app.run(port=5500, debug=True)