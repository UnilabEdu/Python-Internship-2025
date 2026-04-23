from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField,IntegerField,FileField


class ProductForm(FlaskForm):
    name = StringField("Product Name")
    surname = StringField("product Surname")
    price = IntegerField("Product Price")
    img = FileField("Product Image", validators =[FileAllowed(['jpg', 'png', 'jpeg'])])

    submit = SubmitField("Save")

