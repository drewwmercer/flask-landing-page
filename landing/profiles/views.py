from landing import app

@app.route('/user/<username>/')
def profile(username):
    return '<p>username: {username}</p>'.format(username=username)

@app.route('/users/')
def profiles_list():
    return '<p>users: </p>'