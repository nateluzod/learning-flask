from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
  user = {'nickname': 'Nate' }
  title = "Test"
  posts = [
    {
      'author' : {'nickname' : 'John'},
      'body' : 'Beautiful day in Portland!'
    },
    {
      'author' : {'nickname' : 'Susan'},
      'body' : 'This is another post you should not read'
    }
  ]


  return render_template('index.html', title=title, user=user, posts=posts)