"""Flask view endpoints."""

from flask import render_template

from password import generate_passwords
from web.app import app
from web.app.forms import GeneratePasswordForm
from wordlist import wordlist as wl


@app.route('/', methods=['GET', 'POST'])
def index():
    """Index endpoint.

    Returns:
        Rendered index template
    """
    form = GeneratePasswordForm()

    wordlist_params = {
        'max_words_in_wordlist': int(form.max_words_in_wordlist.data),
        'min_word_length': form.min_word_length.data,
        'max_word_length': form.max_word_length.data,
    }

    filename = 'wordlist-{0}-{1}-{2}.txt'.format(
        wordlist_params['max_words_in_wordlist'],
        wordlist_params['min_word_length'],
        wordlist_params['max_word_length'],
    )

    try:
        wordlist = wl.load_from_file(f'wordlist/{filename}')
    except FileNotFoundError:
        wordlist = wl.generate_wordlist(
            max_num_words=wordlist_params['max_words_in_wordlist'],
            min_word_length=wordlist_params['min_word_length'],
            max_word_length=wordlist_params['max_word_length'],
        )

    passwords = generate_passwords(
        wordlist=wordlist,
        words_per_password=form.words_per_password.data,
        num_passwords=form.amount.data,
    )

    return render_template('index.html', form=form, passwords=passwords)
