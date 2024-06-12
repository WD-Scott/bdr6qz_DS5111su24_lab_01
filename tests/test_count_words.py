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
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tokenizer import (count_words, tokenize, run_bash, text, test_cases, test_ids, text_le_corbeau, TheRaven, FalloftheHouseofUsher, CaskofAmontillado, ThePoems, text_dict)

def test_count_words():
    # GIVEN an input string of text
    # WHEN a user passes `text` to the `count_words` function
    # THEN check os and python version, check `count_words` function works as expected
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert count_words(text) == text_dict
        assert count_words("Hello, hello, hello, hi, world") == {"hello": 3, "hi": 1, "world": 1}
        assert count_words("") == {}

@pytest.mark.xfail(reason="Fails purposefully", strict=True)
def test_fail_count_words():
    # GIVEN an input string of text
    # WHEN a user passes `text` to the `count_words` function
    # THEN check os and python version, fail purposefully
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert count_words(text) == 5

def test_bash_count_words():
    # GIVEN an input string of text
    # WHEN a user passes `text` to the `count_words` function
    # THEN check os and python version, check `count_words` output against equivalent bach command
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
    # GIVEN any input
    # WHEN a user passes the input to the `count_words` function
    # THEN check os and python version, skipped purposefully
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        assert count_words(text) == ""

@pytest.mark.parametrize("name, text", test_cases, ids=test_ids)
def test_all_count_words(name, text):
    # GIVEN all English texts as input strings
    # WHEN a user passes `text` to the `count_words` function
    # THEN check os and python vresion, check `count_words` against all English texts
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_text = Counter(tokenize(text))
        assert count_words(text) == expected_text

def test_corbeau_count_words():
    # GIVEN a snippet of text from Le Corbeau
    # WHEN a user passes `text_le_corbeau` to `count_words`
    # THEN check os and python version, check that `count_words` output matches expected output
    if sys.platform != "darwin" or sys.version_info[:2] != (3, 11):
        warnings.warn("Heads Up! This test has only been validated on macOS, Python 3.11.")
    else:
        expected_le_corbeau = Counter(tokenize(text_le_corbeau))
        assert count_words(text_le_corbeau) == expected_le_corbeau
