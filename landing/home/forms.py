from flask_wtf import FlaskForm
from wtforms import StringField, validators

class LandingForm(FlaskForm):
    full_name = StringField('Full Name', validators=[validators.DataRequired(message='Full name is required')])
    email = StringField('Email', validators=[validators.DataRequired(message='Email is required')])
