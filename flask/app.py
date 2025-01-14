from flask import Flask, render_template, request, make_response, redirect, url_for,send_from_directory,Response,jsonify,session,flash
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='templates',static_folder='static',static_url_path='/')
app.secret_key = 'ali1234'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username=='nnn' and password=='pass1234':
            return 'success'
        else:
            return 'fail'
        
@app.route('/set_data')
def set_data():
    session['name']='mike'
    session['other']='hello world'
    return render_template('index.html',message='session data set')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name=session['name']
        other=session['other']
        return render_template('index.html',message=f'name:{name},other:{other}')
    else:
        return render_template('index.html',message='no session found')
    
@app.route('/clear')
def clear():
    session.clear()
    return render_template('index.html',message='session clear')

@app.route('/set_cookie')
def set_cookie():
    response=make_response(render_template('index.html',message='cookie set'))
    response.set_cookie('cookie_name','cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value=request.cookies['cookie_name']
    return render_template('index.html',message=f'cookie value:{cookie_value}')
        
@app.route('/remove_cookie')
def remove_cookie():
    response=make_response(render_template('index.html',message='cookie removed'))
    response.set_cookie('cookie_name',expires=0)
    return response

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username=='nnn' and password=='pass1234':
            flash('successful login')
            return render_template('index.html',message='')
        else:
            flash('login failed')
            return render_template('index.html',message='')

@app.route('/file_upload',methods=['POST'])
def file_upload():
    file=request.files['file']
    if file.content_type=='text/plain':
        return file.read().decode()
    elif file.content_type=='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type=='application/vnd.ms-excel':
        df=pd.read_excel(file)
        return df.to_html()
    
@app.route('/convert_csv',methods=['POST'])
def convert_csv():
    file=request.files['file']
    df=pd.read_excel(file)
    response=Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition':'attachment;filename=result.csv'
        }
    )
    return response

@app.route('/convert_csv_two',methods=['POST'])
def convert_csv_two():
    file=request.files['file']
    df=pd.read_excel(file)
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    filename=f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads',filename))
    return render_template('download.html',filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads',filename,download_name='result.csv')

@app.route('/handle_post',methods=['POST'])
def handle_post():
    greeting= request.json['greeting']
    name=request.json['name']
    with open('file.txt','w') as f:
        f.write(f'{greeting}, {name}')
    return jsonify({'message':'successful'})

@app.route('/other')
def other():
    some_text='hello jjj'
    return render_template('other.html',some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s,times=2):
    return s*times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i%2==0 else c.lower() for i, c in enumerate(s)])

@app.route('/hello')
def hello():
    response=make_response('hello world\n')
    response.status_code=202
    response.headers['content-type']='application/octet-stream'
    return response

@app.route('/greet/<name>')
def greet(name):
    return f"hello {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f'{num1}+{num2}={num1+num2}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting=request.args['greeting']
        name=request.args.get('name')
        return f'{greeting},{name}'
    else:
        return 'some parameters are missing'

if __name__ == '__main__':
    app.run(debug=True)