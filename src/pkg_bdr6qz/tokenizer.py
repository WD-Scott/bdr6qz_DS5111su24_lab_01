'''
tokenizer.py
============

This Python module file contains the functions and objects listed below:

Functions
---------
- clean_text(text)
    Remove punctuation from the input string and convert it to lowercase.

- tokenize(text)
    Split the input string into a list of words.

- count_words(text)
    Count the frequency of each word in the input string.

- run_bash(command)
    Run a bash command and return its output.

- read_file(file_path)
    Read the contents of a file.

Objects
-------
- text
    Testing sentence from The Raven.

- text_dict
    Dictionary of `text` testing sentence to compare with `count_words` output.

- text_list
    List of `text` testing sentence to compare with `tokenize` output.
'''

import string
import subprocess
from collections import Counter

TEXT = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."

TEXT_LE_CORBEAU = "Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"

text_dict = {"but": 1, "the": 2, "raven": 1, "sitting": 1,
             "lonely": 1, "on": 1, "placid": 1, "bust": 1,
             "spoke": 1, "only": 1, "that": 2, "one": 2,
             "word": 2, "as": 1, "if": 1, "his": 1, "soul": 1,
             "in": 1, "he": 1, "did": 1, "outpour": 1}

text_list = ["but", "the", "raven", "sitting", "lonely", "on",
             "the", "placid", "bust", "spoke", "only", "that",
             "one", "word", "as", "if", "his", "soul", "in",
             "that", "one", "word", "he", "did", "outpour"]

def clean_text(input_text):
    """
    Remove punctuation from the input string and convert it to lowercase.

    Params
    ----------
    input_text : str
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
    assert isinstance(input_text, str), f"Input must be a string, you inserted {type(input_text)}"
    cleaned_text = input_text.translate(str.maketrans('', '', string.punctuation)).lower()
    return cleaned_text

def tokenize(input_text):
    """
    Split the input string into a list of words.

    Params
    ----------
    input_text : str
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
    assert isinstance(input_text, str), f"Input must be a string, you inserted {type(input_text)}"
    tokens = clean_text(input_text).split()
    return tokens

def count_words(input_text):
    """
    Count the frequency of each word in the input string.
    
    Params
    ----------
    input_text : str
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
    assert isinstance(input_text, str), f"Input must be a string, you inserted {type(input_text)}"
    tokens = tokenize(input_text)
    word_counts = {}
    # for w in tokens:
    #     word_counts[w] = 1 if w not in word_counts else word_counts[w] + 1
    word_counts = Counter(tokens)
    return word_counts

def run_bash(command):
    '''
    Run a bash command and return its output.

    Params
    ------
    command : str
        The bash command to run.

    Returns
    -------
    str
        The output of the bash command.

    Raises
    ------
    subprocess.CalledProcessError
        If the command exits with a non-zero status.
    '''
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()

def read_file(file_path):
    '''
    Read the contents of a file.

    Params
    ------
    file_path : str
        The path to the file to read.

    Returns
    -------
    str
        The contents of the file.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
