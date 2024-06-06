'''
test_tokenizer.py
=================
'''

from tokenizer import clean_text, tokenize, count_words
import pytest

def test_clean_text():
    '''
    Test the clean_text function.
    '''
    assert clean_text("Hello, World!") == "hello world"
    assert clean_text("!!!") == ""
    assert clean_text("") == ""
    assert clean_text("WoW, tHat Is CoOl!") == "wow that is cool"
    assert clean_text("864. 241,!!!") == "864 241"

def test_tokenize():
    '''
    Test the tokenize function.
    '''
    assert tokenize("Hello, World!") == ["hello", "world"]
    assert tokenize("...") == []
    assert tokenize("") == []
    assert tokenize("WoW, tHat Is CoOl!") == ["wow", "that", "is", "cool"]
    assert tokenize("864, 241, %(*") == ["864", "241"]

def test_count_words():
    '''
    Test the count_words function.
    '''
    assert count_words("Hello, hello, hello, hi, world") == {"hello": 3, "hi": 1, "world": 1}
    assert count_words("") == {}
    assert count_words("...") == {}
    assert count_words("864, 241, %(*") == {"864": 1, "241": 1}

if __name__ == "__main__":
    pytest.main()
    