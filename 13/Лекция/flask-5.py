# HTML-страницы
# Немного про HTML https://basicweb.ru/html/vvedenie.php?ysclid=mipm1sjyq4596765738
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    with open('templates/flask-5.html', 'r') as f:
        txt = f.read()
    return txt


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')