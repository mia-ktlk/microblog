from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Mia'}
    posts = [
        {
            'author':{'username':'Paul'},
            'body': 'I wish there were ten of them.'
        },
        {
            'author': {'username': 'George'},
            'body': 'Self Defense tips: Strike Scream Run.'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)