from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Abhishek'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'A post from John'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'A post from Susan'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)