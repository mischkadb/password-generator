# -*- coding: utf-8 -*-

"""Generate wordlist from DeReWo text file.

Works with 'DeReWo Grundformliste' with 326.946 entries released on 2012-12-31.
https://www1.ids-mannheim.de/kl/projekte/methoden/derewo.html
"""


def get_word_from_derewo_line(line):
    """Processor for individual line from DeReWo textfile.

    Args:
        line: Single line from DeReWo text file

    Returns:
        Lowercase word, None if invalid
    """
    line = line.split()

    # skip words with whitespace
    if len(line) > 2:
        return None

    # disregard DeReWo integer for frequency, only word is needed
    word = line[0]

    # lowercase passwords are good enough with sufficient word list length
    return word.lower()


def word_is_valid(word, min_word_length, max_word_length):
    """Checker for word validity.

    Args:
        word: Processed word from DeReWo text file
        min_word_length: Minimum length per word
        max_word_length: Maximum length per word

    Returns:
        True if word is valid, False otherwise
    """
    # passwords must suit international keyboard layouts,
    # so discard words with special characters including 'ß', 'ä' etc.
    if not word.isalnum():
        return False

    # word length must be in boundary
    if not min_word_length <= len(word) <= max_word_length:
        return False

    return True


def generate_wordlist(max_num_words=5000, min_word_length=3, max_word_length=8):
    """Wordlist generator from DeReWo text file.

    Args:
        max_num_words: Maximum number of words in wordlist
        min_word_length: Minimum length per word
        max_word_length: Maximum length per word

    Returns:
        Word list with lowercase, valid words
    """
    wordlist = set()

    with open('derewo-v-ww-bll-320000g-2012-12-31-1.0.txt', 'r', errors='replace') as derewo_file:
        for line in derewo_file.read().splitlines():
            word = get_word_from_derewo_line(line)

            if not word or not word_is_valid(word, min_word_length, max_word_length):
                continue

            wordlist.add(word)

            if len(wordlist) >= max_num_words:
                break

    return list(wordlist)


def save_to_file(wordlist, min_word_length, max_word_length):
    wordlist_length = len(wordlist)
    out_file_name = f'wordlist-{wordlist_length}-{min_word_length}-{max_word_length}.txt'

    with open(out_file_name, 'w') as out_file:
        wordlist = sorted(wordlist)
        for word in wordlist:
            out_file.write(word + '\n')


def load_from_file(filename):
    with open(filename, 'r') as in_file:
        return in_file.read().splitlines()


def generate_file(max_num_words=5000, min_word_length=3, max_word_length=8):
    wordlist = generate_wordlist(max_num_words, min_word_length, max_word_length)
    save_to_file(wordlist, min_word_length, max_word_length)


if __name__ == '__main__':
    # generate wordlists with different parameters and save them to a file
    min_word_length = 3
    for max_num_words in (3000, 5000, 10000):
        for max_word_length in (5, 6, 7, 8):
            generate_file(max_num_words, min_word_length, max_word_length)
