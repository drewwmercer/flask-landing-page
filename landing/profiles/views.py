from flask import render_template
from landing import app

@app.route('/user/<username>/')
def profile(username):
    context = {'user': username}
    return render_template('profiles_detail.html', context=context, username=username, some_list=[1,22,333,4444,55555])

@app.route('/users/')
def profiles_list():
    return render_template('profiles_list.html')