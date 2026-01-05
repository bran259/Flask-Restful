from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#models

class User(db.Model):
    __tablename = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, unique=True)

class Post(db.Model):
    __tablename = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    post_image = db.Column(db,String)

    #user primary key as foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

