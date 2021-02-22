from landing import app

# url and view routing
@app.route('/')
def hello():
    return '<h1>hello world</h1>'

@app.route('/contact-us/')
def contact_us():
    return '<h1>Contact Us</h1>'

@app.route('/about-us/')
def about_us():
    return '<h1>About Us</h1>'

# more dynamic routing
@app.route('/user/<username>/')
def profile(username):
    # return '<h1>Hello</h1>'
    return '<p>username: {username}</p>'.format(username=username)