from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

class LandingForm(FlaskForm):
    full_name = StringField('Full Name', validators=[validators.DataRequired(message='Full name is required.')])
    email = StringField('Email', validators=[validators.DataRequired(message='Email is required.'), validators.Email()])

    def validate_email(self, field):
        if field.data.endswith('.edu'):
            raise ValidationError('Do not use a school email address.')