'''
test_complicated.py
==================

This Python module contains more complex testing functions.

Functions:
----------
- test_get_texts()
    Tests the get_texts job from the makefile.

- test_tokenizer_count_raven()
    Tests the main functions from tokenizer.py.
'''
import sys
import subprocess
import os
import string
from collections import Counter
from pkg_bdr6qz import (clean_text, tokenize, count_words, read_file)
import pytest
books_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'books'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

books_paths = {
    'TheRaven': os.path.join(books_dir, 'poe_17192.txt'),
    'FalloftheHouseofUsher': os.path.join(books_dir, 'poe_932.txt'),
    'CaskofAmontillado': os.path.join(books_dir, 'poe_1063.txt'),
    'ThePoems': os.path.join(books_dir, 'poe_10031.txt')
}

TheRaven = read_file(books_paths['TheRaven'])
FalloftheHouseofUsher = read_file(books_paths['FalloftheHouseofUsher'])
CaskofAmontillado = read_file(books_paths['CaskofAmontillado'])
ThePoems = read_file(books_paths['ThePoems'])

test_cases = [
    ("The Raven", TheRaven),
    ("Fall of the House of Usher", FalloftheHouseofUsher),
    ("Cask of Amontillado", CaskofAmontillado),
    ("The Poems", ThePoems)
]

test_ids = [name for name, _ in test_cases]

@pytest.mark.integration
def test_get_texts():
    '''
    Tests the get_texts job from the makefile.
    '''
    # GIVEN the pwd and books_dir
    # WHEN the integration tests are run
    # THEN check for "books" dir, if it doesn't exist, run 'make get_texts' and ensure books exist
    if not os.path.isdir(books_dir):
        r = subprocess.run(['make', 'get_texts'], capture_output=True, text=True, check=True)
        assert r.returncode == 0, "Failed to run `make get_texts`."

    books = ['poe_17192.txt', 'poe_932.txt', 'poe_1063.txt', 'poe_10031.txt', 'poe_14082.txt']

    for f_name in books:
        f_path = os.path.join(books_dir, f_name)
        assert os.path.isfile(f_path), f"{f_name} is not in the books directory"

@pytest.mark.integration
def test_tokenizer_count_raven():
    '''
    Tests the main functions from tokenizer.py.
    '''
    # GIVEN the text of The Raven by Edgar Allan Poe
    # WHEN `clean_text`, `tokenize`, and `count_words` are called on TheRaven
    # THEN check return of each function call against the expected returns
    The_Raven = read_file(books_paths['TheRaven'])
    assert isinstance(The_Raven, str), "TheRaven should be a string"
    raven_cleaned_actual = clean_text(The_Raven)
    raven_cleaned_expected = The_Raven.translate(str.maketrans('', '', string.punctuation)).lower()
    assert raven_cleaned_actual == raven_cleaned_expected

    raven_tokenize_actual = tokenize(raven_cleaned_actual)
    raven_tokenize_expected = raven_cleaned_actual.split()
    assert raven_tokenize_actual == raven_tokenize_expected

    raven_word_count_actual = count_words(raven_cleaned_actual)
    raven_word_count_expected = Counter(raven_tokenize_actual)
    assert raven_word_count_actual == raven_word_count_expected
