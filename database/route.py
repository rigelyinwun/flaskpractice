from flask import render_template,request
from models import Person

def register_route(app,db):
    @app.route('/')
    def index():
        people=Person.query.all()
        return str(people)