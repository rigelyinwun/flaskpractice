from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2

conn = psycopg2.connect("dbname=flasktutorialdb user=postgres password=ali1234 host=localhost")


db=SQLAlchemy()

def create_app():
    app = Flask(__name__,template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./testdb.db'
    #app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:ali1234@localhost:5432/flasktutorialdb'
    db.init_app(app)

    from route import register_route
    register_route(app,db)

    migrate=Migrate(app,db)

    return app