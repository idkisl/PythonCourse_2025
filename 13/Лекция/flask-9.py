# Перенаправление страниц
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, World!'


@app.route('/old')
def old_page():
    return redirect(url_for('new_page'))

@app.route('/new')
def new_page():
    return 'Новая страница'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')