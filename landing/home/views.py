from flask import render_template, request
from landing import app

from .forms import LandingForm
from .models import EmailSignup

@app.route('/', methods=['GET','POST'])
def home():
    form = LandingForm()
    if form.validate_on_submit():
        # print(form.full_name.data)
        # print(form.email.data)
        data = form.data
        if 'csrf_token' in data:
            del data['csrf_token']
        obj = EmailSignup(**data)
        obj.save()

    return render_template('home.html', form=form)