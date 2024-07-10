'''
test_tokenizer.py
=================

This Python module contains testing functions for the `tokenize` function.

Functions:
----------
- test_tokenize()
    Test `tokenize`.

- test_fail_tokenize()
    Purposefully fail when testing `tokenize`.

- test_bash_tokenize()
    Test `tokenize` using bash.

- test_tokenize_skipper()
    Test function to show pytest mark and skipping.

- test_all_tokenize()
    Test `tokenize` on all the English texts.

- test_corbeau_tokenize()
    Tests `tokenize` against snippet from Le Corbeau
'''

import sys
import os
import warnings
from pkg_bdr6qz import (tokenize, clean_text, TEXT, text_list, TEXT_LE_CORBEAU, run_bash, read_file)
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

def test_tokenize():
    """
    Test the `tokenize` function.

    GIVEN an input string of text
    WHEN a user passes `text` to the `tokenize` function
    THEN check OS and Python version, and ensure `tokenize` function works as expected.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert tokenize(TEXT) == text_list
        assert isinstance(tokenize(TEXT), list), f"Tokenizer failed on sample text: {TEXT}"
        assert tokenize("864, 241, %(*") == ["864", "241"]

@pytest.mark.xfail(reason="Fails purposefully")
def test_fail_tokenize():
    """
    Test the `tokenize` function with an expected failure.

    GIVEN an input string of text
    WHEN a user passes `text` to the `tokenize` function
    THEN fail purposefully.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert tokenize(TEXT) == ["."]

def test_bash_tokenize():
    """
    Test the `tokenize` function against an equivalent bash command.

    GIVEN an input string of text
    WHEN a user passes `text` to the `tokenize` function
    THEN check OS and Python version, and compare `tokenize` output against equivalent bash command.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        bash_output = run_bash(f'echo "{TEXT}" | tr -d "[:punct:]" | tr "[:upper:]" "[:lower:]" | awk \'{{ for(i=1;i<=NF;i++) print $i }}\'').split()
        assert bash_output == tokenize(TEXT)

@pytest.mark.skip(reason="Skips purposefully")
def test_tokenize_skipper():
    """
    Test the `tokenize` function with a purposeful skip.

    GIVEN any input
    WHEN a user passes the input to the `tokenize` function
    THEN check OS and Python version, and skip the test purposefully.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert tokenize(TEXT) == ""

@pytest.mark.parametrize("name, input_text", test_cases, ids=test_ids)
def test_all_tokenize(name, input_text):
    """
    Test the `tokenize` function against multiple test cases.

    GIVEN all English texts as input strings
    WHEN a user passes `text` to the `tokenize` function
    THEN check OS and Python version, and ensure `tokenize` works correctly for all test cases.

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
        expected_text = clean_text(input_text).split()
        assert tokenize(input_text) == expected_text

def test_corbeau_tokenize():
    """
    Test the `tokenize` function with a snippet of text from Le Corbeau.

    GIVEN a snippet of text from Le Corbeau
    WHEN a user passes `text_le_corbeau` to `tokenize`
    THEN check OS and Python version, and ensure `tokenize` output matches the expected output.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_le_corbeau = clean_text(TEXT_LE_CORBEAU).split()
        assert tokenize(TEXT_LE_CORBEAU) == expected_le_corbeau
