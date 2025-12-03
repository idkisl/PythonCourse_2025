# Аргументы
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return "Main page"

@app.route('/say_hello/<name>')
def say_hello(name):
    return f"Hello, {name}!"

@app.route('/info/<name>/<int:number>')
def info(name, number):
    return name * number


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')