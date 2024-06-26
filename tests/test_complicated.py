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
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tokenizer import (clean_text, tokenize, count_words, read_file, books_dir, books_paths)

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
    TheRaven = read_file(books_paths['TheRaven'])
    assert isinstance(TheRaven, str), "TheRaven should be a string"
    raven_cleaned_actual = clean_text(TheRaven)
    raven_cleaned_expected = TheRaven.translate(str.maketrans('', '', string.punctuation)).lower()
    assert raven_cleaned_actual == raven_cleaned_expected

    raven_tokenize_actual = tokenize(raven_cleaned_actual)
    raven_tokenize_expected = raven_cleaned_actual.split()
    assert raven_tokenize_actual == raven_tokenize_expected

    raven_word_count_actual = count_words(raven_cleaned_actual)
    raven_word_count_expected = Counter(raven_tokenize_actual)
    assert raven_word_count_actual == raven_word_count_expected
