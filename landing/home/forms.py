from flask_wtf import FlaskForm
from wtforms import StringField

class LandingForm(FlaskForm):
    full_name = StringField('Full Name')
    email = StringField('Email')
