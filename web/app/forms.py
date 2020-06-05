"""Flask forms file."""

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import NumberRange

wordlist_lengths = (3000, 5000, 10000)


class GeneratePasswordForm(FlaskForm):
    """Form class for password generation parameters."""

    amount = IntegerField(label='Anzahl der Passwörter', default=5, validators=[NumberRange(1, 10)])
    max_words_in_wordlist = SelectField(
        label='Wörter in Wortliste',
        choices=[(length, str(length)) for length in wordlist_lengths],
        default=wordlist_lengths[1],
    )
    words_per_password = IntegerField(label='Wörter pro Passwort', default=5, validators=[NumberRange(3, 10)])
    min_word_length = IntegerField(label='Min. Wortlänge', default=3, validators=[NumberRange(3, 5)])
    max_word_length = IntegerField(label='Max. Wortlänge', default=7, validators=[NumberRange(4, 12)])  # noqa: WPS432
    submit = SubmitField('Generieren')
