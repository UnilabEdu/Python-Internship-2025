from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, DateField
from wtforms.fields.choices import RadioField, SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from flask_wtf.file import FileField, FileAllowed, FileSize


class RegisterForm(FlaskForm):

    username = StringField("მომხმარებლის სახელი", validators=[DataRequired()])


    password = PasswordField("პაროლი", validators=[
        DataRequired(),
        length(min=8, max=64)
    ])

    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[
        DataRequired("განმეორებითი პაროლის ველი სავალდებულოა!"),
        equal_to("password", message="პაროლი და განმეორებითი პაროლი არ ემთხვევიან")
    ])


    birthdate = DateField("დაბადების თარიღი", validators=[DataRequired()])

    gender = RadioField("სქესი", choices=[(0, "მამაკაცი"), (1, "ქალბატონი")], validators=[DataRequired()])

    country = SelectField("რეგიონი", choices=[
        ("Tbilisi", "თბილისი"),
        ("Kutaisi", "ქუთაისი"),
        ("Batumi", "ბათუმი"),
        ("Rustavi", "რუსთავი"),
        ("Other", "სხვა")
    ], validators=[DataRequired()])

    # ფაილის ატვირთვა
    profile_image = FileField("პროფილის სურათი", validators=[
        FileSize(max_size=1024 * 1024),
        FileAllowed(["jpg", "png", "jpeg"], "მხოლოდ სურათები!")
    ])

    about = TextAreaField("თქვენს შესახებ", validators=[DataRequired()])


    submit = SubmitField("რეგისტრაცია")
    cancel = SubmitField("გაუქმება")


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
            raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს")
        if not contains_lowercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს")
        if not contains_digits:
            raise ValidationError("პაროლი უნდა შეიცავდეს რიცხვებს")
        if not contains_symbols:
            raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს")