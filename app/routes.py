from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Mia'}
    return '''
<html>
    <head>
        <title> Home - Microblog </title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html> '''