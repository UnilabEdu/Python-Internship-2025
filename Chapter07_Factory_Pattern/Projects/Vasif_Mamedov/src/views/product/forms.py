from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FloatField
from flask_wtf.file import FileAllowed, FileField

class ProductForm(FlaskForm):
    name = StringField("Product Name")
    price = FloatField("Product Price")
    img = FileField("Product Image", validators= [FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    submit = SubmitField('Save')