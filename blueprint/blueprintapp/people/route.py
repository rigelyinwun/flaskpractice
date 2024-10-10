from flask import render_template,request,redirect,url_for,Blueprint
from blueprintapp.app import db
from blueprintapp.people.models import Person

people=Blueprint('people',__name__,template_folder='templates')

@people.route('/')
def index():
    people=Person.query.all()
    return render_template('people.html',people=people)

@people.route('/new',methods=['GET','POST'])
def create():
    if request.method=='GET':
        return render_template('new.html')
    elif request.method=='POST':
        name=request.form.get('name')
        age=int(request.form.get('age'))
        job=request.form.get('job')
        person=Person(name=name,age=age,job=job)
        
        db.session.add(person)
        db.session.commit()

        return redirect(url_for('people.index'))

    