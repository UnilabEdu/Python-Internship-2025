from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, equal_to

class RegisterForm(FlaskForm):
    username = StringField("სახელი", validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired(), length(min=8,max=64)])
    repeat_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired("განმეორებითი პაროლის ველი სავალდებულოა!"), equal_to("password", message="პაროლი და განმეორებითი პაროლი არ ემთხვევიან")])
    submit = SubmitField("რეგისტრაცია")
    cancel = SubmitField("გაუქმება")

class LoginForm(FlaskForm):
    username = StringField("სახელი")
    password = PasswordField("პაროლი")
    login = SubmitField("შესვლა")
    cancel = SubmitField("გაუქმება")
