from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, SubmitField, DateField, RadioField, SelectField, \
    IntegerField, FloatField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from string import ascii_uppercase, ascii_lowercase, ascii_letters, digits, punctuation
from flask_wtf.file import FileField, FileSize, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField(
        "Enter username",
        validators=[DataRequired(message="Username is required")])
    password = PasswordField(
        "Enter password",
        validators=[DataRequired(message="Password is required")])
    login = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Enter username", validators=[DataRequired(message='Please enter your username')])
    email = EmailField("Enter email", validators=[DataRequired(message='Please enter your email')])
    password = PasswordField("Enter password",
                             validators=[DataRequired(message='Please enter your password'), length(min=8, max=64)])
    repeat_password = PasswordField("Repeat password", validators=[DataRequired(message='Please confirm your password'),
                                                                   equal_to("password",
                                                                            message="Passwords must match.")])
    birthday = DateField("Enter birthday", validators=[DataRequired(message='Please enter your birthday')])
    gender = RadioField("Choose gender", choices=[(0, "Male"), (1, "Female")],
                        validators=[DataRequired(message='Please choose your gender')])
    country = SelectField(
        "Choose country",
        choices=[
            ("us", "United States"),
            ("ca", "Canada"),
            ("gb", "United Kingdom"),
            ("au", "Australia"),
            ("de", "Germany"),
            ("fr", "France"),
            ("it", "Italy"),
            ("es", "Spain"),
            ("jp", "Japan"),
            ("cn", "China"),
            ("in", "India"),
            ("br", "Brazil"),
            ("mx", "Mexico"),
            ("ru", "Russia"),
            ("za", "South Africa"),
            ("ng", "Nigeria"),
            ("eg", "Egypt")
        ],
        validators=[DataRequired()])
    profile_image = FileField("Upload Profile Image",
                              validators=[FileSize(1024 * 1024), FileAllowed(["jpg", "png", "jpeg"])])
    submit = SubmitField("Sign Up")

    def validate_password(self, field):
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
            raise ValidationError("Password must contain at least one uppercase letter")
        if not contains_lowercase:
            raise ValidationError("Password must contain at least one lowercase letter")
        if not contains_digits:
            raise ValidationError("Password must contain at least one digit (0-9)")
        if not contains_symbols:
            raise ValidationError("Password must contain at least one special character (e.g., !, @, #, etc.)")
