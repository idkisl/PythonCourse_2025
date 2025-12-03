from flask import Flask
# Страницы сайта
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/help')
def help_page():
    return '''Мы умеем выводить на экран различную информацию! Ура!'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')