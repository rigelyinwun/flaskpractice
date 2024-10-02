from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__, template_folder='templates')

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
        
@app.route('/file_upload')
def file_upload():
    return ""

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