#  Подключение css
#  https://getbootstrap.com
from flask import Flask, request, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return f'''
        <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
                <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
                
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                
                <title>Bootstrap Example</title>
                <script defer img="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
              </head>
              <body class="p-3 m-0 border-0 bd-example m-0 border-0">
              
              <form class="login_form" method="post">
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                    <button type="submit" class="btn btn-primary">Записаться</button>
                </form>
                
              </body>
            </html>
            '''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        return "Форма отправлена"



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')