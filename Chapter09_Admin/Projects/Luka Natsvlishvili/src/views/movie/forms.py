from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class MovieForm(FlaskForm):
    name = StringField("ფილმის სახელი", validators=[DataRequired()])
    release_date = StringField("გამოშვების თარიღი", validators=[DataRequired()])
    genre = StringField("ჟანრი", validators=[DataRequired()])
    comment1_author = StringField("პირველი კომენტარის ავტორი", validators=[DataRequired()])
    comment1_text = StringField("კომენტარი", validators=[DataRequired()])
    comment2_author = StringField("მეორე კომენტარის ავტორი", validators=[DataRequired()])
    comment2_text = StringField("კომენტარი", validators=[DataRequired()])
    img = FileField("ფილმის სურათი", validators=[FileAllowed(["jpg","jpeg","png"])])
    submit = SubmitField("შენახვა")