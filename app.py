from flask import Flask, make_response, request
from models import db, User, Post
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rest-api.db'

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class UserResource(Resource):
    def get(self):
        return make_response ([user.to_dict() for user in User.query.all()], 200)
    
    def post(self):
        data = request.get_json()
        new_user = User(username=data.get('username'), email=data.get('email'))

        db.session.add(new_user)
        db.session.commit()

        return make_response(new_user.to_dict(), 201)
    
class UserResourceById(Resource):
    def get(self, id):
        user = User.query.get(id)
        if not user:
            return make_response({"message" : "User not found"})
        return make_response(user.to_dict(), 200)
    
    def patch(self, id):
        pass

    def delete(self, id):
        pass

# mapping endpoints to their resources        
api.add_resource(UserResource, '/users')
api.add_resource(UserResourceById, '/users/<int:id>')



# @app.route('/')
# def index():
#     return f"<h1>Introduction to Flask-Restful API</h1>"
           

if __name__ == '__main__':
    app.run(port=5500, debug=True)