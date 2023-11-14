from flask import Flask, request

app = Flask(__name__)

message = 'Hello, world'

@app.route('/')
def index():
    return f'<h3>{message}</h3>'

@app.route('/spam')
def spam():
    person = { 'name': 'John', 'age': 21 }
    return person

@app.route('/hello')
def hello():
    print(request.args.get('name'))
    name = 'Jack'
    return { 'message': f'Hello, {name}!'}

@app.route('/add')
def add():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return { 'result': num1 + num2 }

@app.errorhandler(404)
def not_found(error):
    return {'error': str(error)}, 404

if __name__ == '__main__':
    app.run(debug=True)