from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm

class LoggingForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message='Invalid Username')])
    email = StringField(label='Email', validators=[DataRequired(), Email(message='Invalid email address.')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message='Field must be at least 8 characters long.')])
    submit = SubmitField(label='Log in')