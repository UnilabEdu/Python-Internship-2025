import re
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

BAD_WORDS = [
    # ქართული
    "პიდარ", "მუტ", "მუდელ", "ბოზ", "ნაბოზ", "ნაძაღლ", "ნაძირალ", "ნამუდლ",
    "მოვტყ", "ტყნ", "ტყვ", "ტყვნ", "გატყ", "ჩაგატყ", "დედამოვტყ",
    "გაუპატიურ", "დედაშენი", "მამაშენი",
    "მოკვდი", "მოკვდე", "ჩაიხრჩე",
    "იდიოტ", "კრეტინ", "სულელ", "გიჟ",
    "ყლე", "ტრაკ", "შევეცი", "ლახვარ", "ხოარ", "ხოარო", "ხოარის", "შიგ", "ზანგ",

    # English
    "fuck", "fck", "fuk", "f u c k", "motherfuck",
    "shit", "sh1t", "bitch", "b1tch", "bastard",
    "asshole", "cunt", "dick", "d1ck", "cock", "c0ck",
    "pussy", "pus5y", "whore", "wh0re", "slut",
    "nigger", "nigga", "negga", "n1gg",
    "faggot", "retard", "idiot", "moron", "imbecile",
    "douche", "loser", "jerk", "pervert", "creep",
    "wtf", "stfu", "gtfo", "a55",

    # Latin transliteration
    "yle", "yleo", "kle", "traki", "trako",
    "mut", "bozi", "bozo", "pidar", "laxvar",
    "sheveci", "giJ", "mokvdi", "tyv", "shvc",
    "shig", "shig xoar gaq", "shig xoar gak",
]

LEET_MAP = {
    '0': 'o', '1': 'i', '3': 'e', '4': 'a',
    '5': 's', '6': 'g', '7': 't', '8': 'b', '@': 'a',
    '$': 's', '!': 'i', '+': 't',
}

def normalize(text):
    text = text.lower()
    for leet, normal in LEET_MAP.items():
        text = text.replace(leet, normal)
    text = re.sub(r'(.)\1+', r'\1', text)
    text = re.sub(r'\s+', '', text)
    text = re.sub(r'[^\w\u10D0-\u10FF]', '', text)
    return text

def build_pattern(word):
    return ''.join([f"{re.escape(char)}+" for char in word])

def no_bad_words(form, field):
    normalized = normalize(field.data)
    for word in BAD_WORDS:
        pattern = build_pattern(normalize(word))
        if re.search(pattern, normalized):
            raise ValidationError("კომენტარი შეიცავს დაუშვებელ სიტყვებს.")

class CommentForm(FlaskForm):
    text = StringField("კომენტარი", validators=[DataRequired(), no_bad_words])
    submit = SubmitField("გაგზავნა")