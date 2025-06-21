from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired, length
from flask_wtf.file import FileField, FileSize, FileAllowed, FileRequired

class AddTourForm(FlaskForm):
    title = StringField("Tour Title", validators=[DataRequired(message="Please enter a title"), length(max=100)])
    country = SelectField(
        "Country",
        choices=[
            ('', 'Select a country'),
            ('AF', 'Afghanistan'),
            ('AL', 'Albania'),
            ('DZ', 'Algeria'),
            ('AR', 'Argentina'),
            ('AU', 'Australia'),
            ('AT', 'Austria'),
            ('BD', 'Bangladesh'),
            ('BE', 'Belgium'),
            ('BR', 'Brazil'),
            ('BG', 'Bulgaria'),
            ('CA', 'Canada'),
            ('CL', 'Chile'),
            ('CN', 'China'),
            ('CO', 'Colombia'),
            ('HR', 'Croatia'),
            ('CZ', 'Czech Republic'),
            ('DK', 'Denmark'),
            ('EG', 'Egypt'),
            ('EE', 'Estonia'),
            ('FI', 'Finland'),
            ('FR', 'France'),
            ('DE', 'Germany'),
            ('GR', 'Greece'),
            ('HU', 'Hungary'),
            ('IS', 'Iceland'),
            ('IN', 'India'),
            ('ID', 'Indonesia'),
            ('IR', 'Iran'),
            ('IQ', 'Iraq'),
            ('IE', 'Ireland'),
            ('IL', 'Israel'),
            ('IT', 'Italy'),
            ('JP', 'Japan'),
            ('JO', 'Jordan'),
            ('KZ', 'Kazakhstan'),
            ('KE', 'Kenya'),
            ('KR', 'South Korea'),
            ('KW', 'Kuwait'),
            ('LV', 'Latvia'),
            ('LB', 'Lebanon'),
            ('LT', 'Lithuania'),
            ('MY', 'Malaysia'),
            ('MX', 'Mexico'),
            ('MA', 'Morocco'),
            ('NL', 'Netherlands'),
            ('NZ', 'New Zealand'),
            ('NG', 'Nigeria'),
            ('NO', 'Norway'),
            ('PK', 'Pakistan'),
            ('PE', 'Peru'),
            ('PH', 'Philippines'),
            ('PL', 'Poland'),
            ('PT', 'Portugal'),
            ('QA', 'Qatar'),
            ('RO', 'Romania'),
            ('RU', 'Russia'),
            ('SA', 'Saudi Arabia'),
            ('RS', 'Serbia'),
            ('SG', 'Singapore'),
            ('SK', 'Slovakia'),
            ('SI', 'Slovenia'),
            ('ZA', 'South Africa'),
            ('ES', 'Spain'),
            ('SE', 'Sweden'),
            ('CH', 'Switzerland'),
            ('SY', 'Syria'),
            ('TH', 'Thailand'),
            ('TR', 'Turkey'),
            ('UA', 'Ukraine'),
            ('AE', 'United Arab Emirates'),
            ('GB', 'United Kingdom'),
            ('US', 'United States'),
            ('VN', 'Vietnam'),
            ('YE', 'Yemen'),
            ('ZW', 'Zimbabwe'),
        ],
        validators=[DataRequired(message="Please select a country")]
    )
    description = StringField("Description", validators=[DataRequired(message="Please enter a description")])
    price = FloatField("Current Price",
                         validators=[DataRequired(message="Please enter the price")])
    currency = SelectField(
        "Currency",
        choices=[
            ("USD", "USD"),
            ("EUR", "EUR"),
            ("AUD", "AUD"),
            ("GBP", "GBP"),
            ("JPY", "JPY")
        ],
        validators=[DataRequired(message="Please select a currency")]
    )
    image = FileField("Upload Image",
                      validators=[FileSize(1024 * 1024), FileAllowed(["jpg", "png", "jpeg"])])
    duration = StringField("Duration (e.g. 4 days)", validators=[DataRequired(message="Please enter duration")])
    submit = SubmitField("Add Tour")