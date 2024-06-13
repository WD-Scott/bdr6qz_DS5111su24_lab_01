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
assert os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'books')), "The `books` directory does not yet exist. You must run `make get_texts` to first download the books"
import string
import warnings
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tokenizer import (clean_text, run_bash, text, test_cases, test_ids, text_le_corbeau, TheRaven, FalloftheHouseofUsher, CaskofAmontillado, ThePoems)

def test_clean_text():
    # GIVEN an input string of text
    # WHEN a user passes `text` to `clean_text`
    # THEN check os and python version, check `clean_text` works as expected (lower case, no punctuation)
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert clean_text(text) == "but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"
        assert clean_text("!!!") == ""
        assert clean_text("") == ""

@pytest.mark.xfail(reason="Fails purposefully", strict=True)
def test_fail_clean_text():
    # GIVEN an input string of text
    # WHEN a user passes `text` to `clean_text`
    # THEN fail purposefully
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert clean_text(text) == "BUT the raven sitting lonely on the placid bust spoke"

def test_bash_clean_text():
    # GIVEN an input string of text
    # WHEN a user passes `text` to `clean_text`
    # THEN check os and python version, check `clean_text` output against equivalent bash command
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert run_bash(f'echo "{text}" | tr -d "[:punct:]" | tr "[:upper:]" "[:lower:]"') == clean_text(text)

@pytest.mark.skip(reason="Skips purposefully")
def test_clean_text_skipper():
    # GIVEN any input
    # WHEN a user passes the input to `clean_text`
    # THEN check os and python version, skipped purposefully
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert clean_text(text) == ""

@pytest.mark.parametrize("name, text", test_cases, ids=test_ids)
def test_all_clean_text(name, text):
    # GIVEN all English texts as input strings
    # WHEN a user passes `text` to `clean_text`
    # THEN check os and python version, check `clean_text` against all English texts
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        assert clean_text(text) == expected_text

def test_corbeau_clean_text():
    # GIVEN a snippet of text from Le Corbeau
    # WHEN a user passes `text_le_corbeau` to `clean_text`
    # THEN check os and python version, check that `clean_text` output matches expected output
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_le_corbeau = text_le_corbeau.translate(str.maketrans('', '', string.punctuation)).lower()
        assert clean_text(text_le_corbeau) == expected_le_corbeau
