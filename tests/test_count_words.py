'''
test_count_words.py
===================

This Python module contains testing functions for the `count_words` function.

Functions:
----------
- test_count_words()
    Test `count_words`.

- test_fail_count_words()
    Purposefully fail when testing `count_words`.

- test_bash_count_words()
    Test `count_words` using bash.

- test_count_words_skipper()
    Test function to show pytest mark and skipping.

- test_all_count_words()
    Test `count_words` on all the English texts.

- test_corbeau_count_words()
    Tests `count_words` against snippet from Le Corbeau
'''

import sys
import os
import warnings
from collections import Counter
from pkg_bdr6qz import (count_words, tokenize, run_bash, text, text_le_corbeau, text_dict, read_file)
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

def test_count_words():
    """
    Test the `count_words` function.

    GIVEN an input string of text
    WHEN a user passes `text` to the `count_words` function
    THEN check OS and Python version, and ensure `count_words` function works as expected.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert count_words(text) == text_dict
        assert count_words("Hello, hello, hello, hi, world") == {"hello": 3, "hi": 1, "world": 1}
        assert count_words("") == {}

@pytest.mark.xfail(reason="Fails purposefully")
def test_fail_count_words():
    """
    Test the `count_words` function with an expected failure.

    GIVEN an input string of text
    WHEN a user passes `text` to the `count_words` function
    THEN fail purposefully.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert count_words(text) == 5

def test_bash_count_words():
    """
    Test the `count_words` function against an equivalent bash command.

    GIVEN an input string of text
    WHEN a user passes `text` to the `count_words` function
    THEN check OS and Python version, and compare `count_words` output against equivalent bash command.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        bash_command = f'echo "{text}" | tr -d "[:punct:]" | tr "[:upper:]" "[:lower:]" | awk \'{{ for(i=1;i<=NF;i++) a[$i]++ }} END {{ for(k in a) print k, a[k] }}\''
        bash_output = run_bash(bash_command).split('\n')
        bash_output_dict = dict(line.split() for line in bash_output)
        bash_output_dict = {k: int(v) for k, v in bash_output_dict.items()}
        assert bash_output_dict == count_words(text)

@pytest.mark.skip(reason="Skips purposefully")
def test_count_words_skipper():
    """
    Test the `count_words` function with a purposeful skip.

    GIVEN any input
    WHEN a user passes the input to the `count_words` function
    THEN check OS and Python version, and skip the test purposefully.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert count_words(text) == ""

@pytest.mark.parametrize("name, input_text", test_cases, ids=test_ids)
def test_all_count_words(name, input_text):
    """
    Test the `count_words` function against multiple test cases.

    GIVEN all English texts as input strings
    WHEN a user passes `text` to the `count_words` function
    THEN check OS and Python version, and ensure `count_words` works correctly for all test cases.

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
        expected_text = Counter(tokenize(input_text))
        assert count_words(input_text) == expected_text

def test_corbeau_count_words():
    """
    Test the `count_words` function with a snippet of text from Le Corbeau.

    GIVEN a snippet of text from Le Corbeau
    WHEN a user passes `text_le_corbeau` to `count_words`
    THEN check OS and Python version, and ensure `count_words` output matches the expected output.

    Warns
    -----
    UserWarning
        If the test is run on a platform other than macOS or Python version other than 3.11.
    """
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_le_corbeau = Counter(tokenize(text_le_corbeau))
        assert count_words(text_le_corbeau) == expected_le_corbeau
