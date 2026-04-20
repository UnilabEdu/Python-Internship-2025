from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class MovieForm(FlaskForm):
    name = StringField("Movie Name", validators=[DataRequired()])
    release_date = StringField("Release Date", validators=[DataRequired()])
    genre = StringField("Genre", validators=[DataRequired()])
    comment1_author = StringField("First Comment Author", validators=[DataRequired()])
    comment1_text = StringField("Comment", validators=[DataRequired()])
    comment2_author = StringField("Second Comment Author", validators=[DataRequired()])
    comment2_text = StringField("Comment", validators=[DataRequired()])
    img = FileField("Movie Image", validators=[FileAllowed(["jpg","jpeg","png"])])
    submit = SubmitField("Save")