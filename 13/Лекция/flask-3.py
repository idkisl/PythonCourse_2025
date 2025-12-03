# Параметры страницы
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/say_hello')
def say_hello():
    name = input()
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')