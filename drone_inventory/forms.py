# form validation for Sign in page(signin.html and signup.html)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    # create email, password, and submit attribute
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()
