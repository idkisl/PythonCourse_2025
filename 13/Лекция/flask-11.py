# Шаблоны и управляющие конструкции
# Немного про HTML https://basicweb.ru/html/vvedenie.php?ysclid=mipm1sjyq4596765738
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, World!'


@app.route('/nice_page/<password>')
def nice_page(password):
    name = "Вася"
    day = "2025-12-3"
    return render_template('flask-11.html',
                           name=name,
                           date=day,
                           password=password,
                           nice_words=["Хороший день!", "Любви!", "Программирования!"])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')