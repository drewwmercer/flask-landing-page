from landing import app

# url and view routing
@app.route('/contact-us/')
def contact_us():
    return '<h1>Contact Us</h1>'

@app.route('/about-us/')
def about_us():
    return '<h1>About Us</h1>'