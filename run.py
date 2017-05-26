#! flask/bin/python
# coding=utf-8

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return '''
              <html>
                <head>
                    <title>Home Page</title>
                </head>
                <body>
                    <h1>Hello, ''' + user['nickname'] + '''</h1>
                </body>
              </html>
              '''


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
