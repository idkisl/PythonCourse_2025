# Шаблоны
# Немного про HTML https://basicweb.ru/html/vvedenie.php?ysclid=mipm1sjyq4596765738
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, World!'


@app.route('/nice_page/<name>')
def nice_page(name):
    day = "2025-12-3"
    return render_template('flask-10.html',
                           name=name,
                           date=day)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')