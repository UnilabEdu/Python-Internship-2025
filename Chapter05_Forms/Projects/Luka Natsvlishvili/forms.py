from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, DateField
from wtforms.fields.choices import RadioField, SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize

class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    password = PasswordField("Enter Password", validators=[DataRequired(), length(min=8,max=64)])
    repeat_password = PasswordField("Confirm Password", validators=[DataRequired("განმეორებითი პაროლის ველი სავალდებულოა!"), equal_to("password", message="პაროლი და განმეორებითი პაროლი არ ემთხვევიან")])
    birthdate = DateField("Enter Birthday", validators=[DataRequired()])
    gender = RadioField("Choose Gender", choices=[(0,"Male"), (1,"Female")], validators=[DataRequired()])
    country = SelectField("Choose Country", choices=["Georgia","United States","Germany"], validators=[DataRequired()])
    profile_image = FileField("Upload profile image", validators=[FileSize(1024 * 1024),
                                                                  FileAllowed(["jpg","png", "jpeg"])])
    about = TextAreaField("About You", validators=[DataRequired()])
    submit = SubmitField("Register")
    cancel = SubmitField("Cancel")
    def validate_password(self,field):
        contains_uppercase = False
        contains_lowercase = False
        contains_digits = False
        contains_symbols = False

        for char in field.data:
            if char in ascii_uppercase:
                contains_uppercase = True
            if char in ascii_lowercase:
                contains_lowercase = True
            if char in digits:
                contains_digits = True
            if char in punctuation:
                contains_symbols = True

        if not contains_uppercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს")
        if not contains_lowercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს")
        if not contains_digits:
            raise ValidationError("პაროლი უნდა შეიცავდეს რიცხვებს")
        if not contains_symbols:
            raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს")
