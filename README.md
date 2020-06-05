# German multi-word password generator

This project generates multi-word passwords and contains a German wordlist generator.

The wordlists are created based on the [DeReWo](https://www1.ids-mannheim.de/kl/projekte/methoden/derewo.html) 'Grundformliste' dataset released on 2012-12-31 containing 326.946 German words sorted by frequency.

Wordlist generation
----

Wordlist generation takes the maximum amount of words and a pre-defined min/max length per word as parameters. Bigger wordlists contain more entropy per word in generated passwords in exchange for less used words. Smaller maximum word lengths result in shorter passwords, but contain less used words which might be more difficult to memorize.

An example for wordlist generation with sane values:

    wordlist = wordlist.generate_wordlist           (max_num_words=5000, min_word_length=3, max_word_length=8)

Pre-made wordlists
----

There are a couple of pre-made wordlists containing the number of words and min/max word length in the file name. They can be loaded with 

    wordlist = wordlist.load_from_file('file-name')

Password generation
----
Generate single passwords with

    password = password.generate_password(wordlist, num_words=6)

Set `whitespace_separation=False` if you want the password without whitespaces ready for copy and paste.

Multiple (here 5) passwords can be generated with 

    passwords = password.generate_passwords(wordlist, words_per_password=6, num_passwords=5)

Security
----

Password security highly depends on the chosen parameters and used algorithms for random number generation. This project uses the [Python3 secrets](https://docs.python.org/3/library/secrets.html) module which is designed to be cryptographically strong.
