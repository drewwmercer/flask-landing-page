from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

class LandingForm(FlaskForm):
    full_name = StringField('Full Name', render_kw={'class': 'form-control', 'placeholder': 'Your name'}, validators=[validators.DataRequired(message='Full name is required.')])
    email = StringField('Email', render_kw={'class': 'form-control', 'placeholder': 'Your email'}, validators=[validators.DataRequired(message='Email is required.'), validators.Email()])

    def validate_email(self, field):
        if field.data.endswith('.edu'):
            raise ValidationError('Do not use a school email address.')