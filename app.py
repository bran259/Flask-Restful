from flask import Flask
from models import db, User, Post
from flask_migrate import Migrate

app = Flask(__name__)

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rest-api.db'

migrate = Migrate(db, app)
db.init_app(app)

@app.route('/')
def index():
    return f"<h1>Introduction to Flask-Restful API</h1>"
           

if __name__ == '__main__':
    app.run(port=5500, debug=True)