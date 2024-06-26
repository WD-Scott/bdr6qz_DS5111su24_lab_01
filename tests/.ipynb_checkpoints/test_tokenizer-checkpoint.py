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
import bdr6qz as pkg
import subprocess
import string
import warnings
import pytest
books_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'books'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from bdr6qz import (tokenize, clean_text, text, text_list, test_cases, test_ids, text_le_corbeau, run_bash, TheRaven, FalloftheHouseofUsher, CaskofAmontillado, ThePoems)

def test_tokenize():
    # GIVEN an input string of text
    # WHEN a user passes `text` to the `tokenize` function
    # THEN check os and python version, check `tokenize` function works as expected
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert tokenize(text) == text_list
        assert isinstance(tokenize(text), list), f"Tokenizer failed on sample text: {text}"
        assert tokenize("864, 241, %(*") == ["864", "241"]

@pytest.mark.xfail(reason="Fails purposefully")
def test_fail_tokenize():
    # GIVEN an input string of text
    # WHEN a user passes `text` to the `tokenize` function
    # THEN check os and python version, fail purposefully
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert tokenize(text) == ["."]

def test_bash_tokenize():
    # GIVEN an input string of text
    # WHEN a user passes `text` to the `tokenize` function
    # THEN check os and python version, check `tokenize` output against equivalent bash command
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        bash_output = run_bash(f'echo "{text}" | tr -d "[:punct:]" | tr "[:upper:]" "[:lower:]" | awk \'{{ for(i=1;i<=NF;i++) print $i }}\'').split()
        assert bash_output == tokenize(text)

@pytest.mark.skip(reason="Skips purposefully")
def test_tokenize_skipper():
    # GIVEN any input
    # WHEN a user passes the input to the `tokenize` function
    # THEN check os and python version, skipped purposefully
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert tokenize(text) == ""

@pytest.mark.parametrize("name, text", test_cases, ids=test_ids)
def test_all_tokenize(name, text):
    # GIVEN all English texts as input strings
    # WHEN a user passes `text` to the `tokenize` function
    # THEN checks os and python version, checks `tokenize` against all English texts
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_text = clean_text(text).split()
        assert tokenize(text) == expected_text

def test_corbeau_tokenize():
    # GIVEN a snippet of text from Le Corbeau
    # WHEN a user passes `text_le_corbeau` to `tokenize`
    # THEN check os and python version, check that `tokenize` output matches expected output
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_le_corbeau = clean_text(text_le_corbeau).split()
        assert tokenize(text_le_corbeau) == expected_le_corbeau
