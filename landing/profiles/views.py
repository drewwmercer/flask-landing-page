from flask import render_template
from landing import app

@app.route('/user/<username>/')
def profile(username):
    context = {'user': username, 'right_user': True}
    if username == 'amercer':
        context['admin_user_msg'] = "Access level: admin"
    else:
        context['admin_user_msg'] = "Access level: regular user"
    return render_template('profiles_detail.html', context=context, some_list=[1,22,333,4444,55555])

@app.route('/users/')
def profiles_list():
    return render_template('profiles_list.html')