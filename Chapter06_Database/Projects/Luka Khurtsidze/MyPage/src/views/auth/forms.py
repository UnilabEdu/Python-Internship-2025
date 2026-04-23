from flask_wtf import FlaskForm

from wtforms.fields import (StringField, PasswordField, SubmitField)
from wtforms.validators import DataRequired, length, equal_to



class RegisterForm(FlaskForm):
    username = StringField('მიუთითეთ სახელი',
                           validators = [DataRequired()])
    password = PasswordField('მიუთითეთ პაროლი',
                             validators = [DataRequired("განმეორებითი პაროლის ველო სავალდებულოა"), length(min=8, max=64)])
    repeat_password = PasswordField('დაადასტურეთ პაროლი',
                                    validators = [DataRequired(), equal_to("password",
                                                                           message= "პაროლი და განმეორებითი პაროლი არ ემთხვევა!")])
    submit = SubmitField('რეგისტრაცია')


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    login = SubmitField("Login")
















