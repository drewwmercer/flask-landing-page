from flask import render_template
from landing import app

@app.route('/user/<username>/')
def profile(username):
    return render_template('profiles_detail.html', username=username)

@app.route('/users/')
def profiles_list():
    return render_template('profiles_list.html')