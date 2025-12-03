# Работа с запросами
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, World!'


@app.route('/search')
def search():
    query = request.args.get('q', '')  # /search?q=python
    all_args = request.args.to_dict()
    tags = request.args.getlist('tag')  # /search?tag=python&tag=flask

    return f'Поиск по q: {query}, Теги: {tags}, all_args: {all_args}'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')