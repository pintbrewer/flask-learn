from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Lee'}
  posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Mike'},
            'body': 'Cloudy here in cleveland!'
        },
        {
            'author': {'username': 'Jane'},
            'body': 'The Avengers movie was too long!'
        }
    ]
  return render_template('index.html', title='Home', user=user, posts=posts)