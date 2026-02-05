from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField, DateField, RadioField
from wtforms.validators import DataRequired, length, equal_to

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=8, max=64)])
    repeat_password = PasswordField('Confirm Password', validators=[DataRequired(), equal_to('password', message='Passwords must match')])
    birthday = DateField('Birthdate', validators=[DataRequired()])
    gender = RadioField('Choose Gender', validators=[DataRequired()], choices=[('Male','Male'),('Female','Female')])
    submit = SubmitField('Register')