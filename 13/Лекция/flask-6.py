# Статический контент
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, World!'

@app.route('/mipt')
def mipt():
    return f'''<img src="{url_for('static', filename='img/mipt.jpg')}">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')