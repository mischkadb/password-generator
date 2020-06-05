# -*- coding: utf-8 -*-

"""Generate multi-word passwords from a wordlist.

Based on Diceware passwords.
Password strength depends on number of words in wordlist and number of words per password.
"""

import secrets

secure_random = secrets.SystemRandom()


def generate_password(wordlist, num_words=6, whitespace_separation=True):
    """Generate a single multi-word password.

    Args:
        wordlist: List of words to sample password phrases from
        num_words: Number of words in the password
        whitespace_separation: Bool indicator for word separation by whitespace

    Returns:
        Password of sampled strings from wordlist
    """
    words = secure_random.sample(wordlist, num_words)
    separator = ' ' if whitespace_separation else ''
    return separator.join(words)


def generate_passwords(wordlist, words_per_password=6, num_passwords=5, whitespace_separation=True):
    """Generate multiple multi-word passwords.

    Args:
        wordlist: List of words to sample password phrases from
        words_per_password: Number of words in an individual password
        num_passwords: Number of passwords to be generated
        whitespace_separation: Bool indicator for word separation by whitespace

    Returns:
        List of generated passwords
    """
    return [generate_password(wordlist, words_per_password, whitespace_separation) for _ in range(num_passwords)]
