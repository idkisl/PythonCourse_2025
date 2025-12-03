# Обработка ошибок
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, World!'


@app.errorhandler(404)
def page_not_found(error):
    return f'Возникла ошибка :( <BR> {error}'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')