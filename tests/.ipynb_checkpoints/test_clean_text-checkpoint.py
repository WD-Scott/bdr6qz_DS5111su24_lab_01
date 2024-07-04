'''
test_clean_text.py
==================

This Python module contains testing functions for the `clean_text` function.

Functions:
----------
- test_clean_text()
    Test `clean_text`.

- test_fail_clean_text()
    Purposefully fail when testing `clean_text`.

- test_bash_clean_text()
    Test `clean_text` using bash.

- test_clean_text_skipper()
    Test function to show pytest mark and skipping.

- test_all_clean_text()
    Test `clean_text` on all the English texts.

- test_corbeau_clean_text()
    Tests `clean_text` against snippet from Le Corbeau
'''

import sys
import os
import string
import warnings
import pytest
from pkg_bdr6qz import (clean_text, run_bash, read_file, text, text_le_corbeau)
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

def test_clean_text():
    """
    Test the `clean_text` function.

    GIVEN an input string of text
    WHEN a user passes `text` to `clean_text`
    THEN check OS and Python version, and ensure `clean_text` works as expected (lowercase, no punctuation).

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert clean_text(text) == "but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"
        assert clean_text("!!!") == ""
        assert clean_text("") == ""

@pytest.mark.xfail(reason="Fails purposefully")
def test_fail_clean_text():
    """
    Test the `clean_text` function with an expected failure.

    GIVEN an input string of text
    WHEN a user passes `text` to `clean_text`
    THEN fail purposefully.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert clean_text(text) == "BUT the raven sitting lonely on the placid bust spoke"

def test_bash_clean_text():
    """
    Test the `clean_text` function against an equivalent bash command.

    GIVEN an input string of text
    WHEN a user passes `text` to `clean_text`
    THEN check OS and Python version, and compare `clean_text` output against equivalent bash command.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert run_bash(f'echo "{text}" | tr -d "[:punct:]" | tr "[:upper:]" "[:lower:]"') == clean_text(text)

@pytest.mark.skip(reason="Skips purposefully")
def test_clean_text_skipper():
    """
    Test the `clean_text` function with a purposeful skip.

    GIVEN any input
    WHEN a user passes the input to `clean_text`
    THEN check OS and Python version, and skip the test purposefully.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert clean_text(text) == ""

@pytest.mark.parametrize("name, input_text", test_cases, ids=test_ids)
def test_all_clean_text(name, input_text):
    """
    Test the `clean_text` function against multiple test cases.

    GIVEN all English texts as input strings
    WHEN a user passes `text` to `clean_text`
    THEN check OS and Python version, and ensure `clean_text` works correctly for all test cases.

    Parameters
    ----------
    name : str
        The name of the test case.
    input_text : str
        The input text for the test case.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_text = input_text.translate(str.maketrans('', '', string.punctuation)).lower()
        assert clean_text(input_text) == expected_text

def test_corbeau_clean_text():
    """
    Test the `clean_text` function with a snippet of text from Le Corbeau.

    GIVEN a snippet of text from Le Corbeau
    WHEN a user passes `text_le_corbeau` to `clean_text`
    THEN check OS and Python version, and ensure `clean_text` output matches the expected output.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_le_corbeau = text_le_corbeau.translate(str.maketrans('', '', string.punctuation)).lower()
        assert clean_text(text_le_corbeau) == expected_le_corbeau
