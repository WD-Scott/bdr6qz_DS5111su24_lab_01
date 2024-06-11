'''
tokenize.py
===========
'''

import logging
import string
from collections import Counter

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

def clean_text(text):
    """
    Remove punctuation from the input string and convert it to lowercase.
    
    Params
    ----------
    text : str
        The input string.
        
    Returns
    -------
    str
        The cleaned string with all lowercase words and no punctuation.
    
    Raises
    ------
    AssertionError
        If the input is not a string.
    """
    assert isinstance(text, str), "Input must be a string"
    logging.debug("Cleaning text: %s", text)
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    logging.debug("Cleaned text: %s", cleaned_text)
    return cleaned_text

def tokenize(text):
    """
    Split the input string into a list of words.
    
    Params
    ----------
    text : str
        The input string.
        
    Returns
    -------
    list of str
        A list, where each item is a word from the input string.
    
    Raises
    ------
    AssertionError
        If the input is not a string.
    """
    assert isinstance(text, str), "Input must be a string"
    logging.debug("Tokenizing text: %s", text)
    tokens = clean_text(text).split()
    logging.debug("Tokens: %s", tokens)
    return tokens

def count_words(text):
    """
    Count the frequency of each word in the input string.
    
    Params
    ----------
    text : str
        The input string.
        
    Returns
    -------
    dict of {str: int}
        A dict, where keys are words and values are their counts.
    
    Raises
    ------
    AssertionError
        If the input is not a string.
    """
    assert isinstance(text, str), "Input must be a string"
    logging.debug("Counting words in text: %s", text)
    tokens = tokenize(text)
    word_counts = Counter(tokens)
    logging.debug("Word counts: %s", word_counts)
    return word_counts
