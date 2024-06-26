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

- books_dir
    The path for the `books` directory (available only after a user runs `make get_the_books`).

- books_paths
    Dictionary of the necessary book filepaths inside of `books_dir`.

- TheRaven
    The text of The Raven.
    
- FalloftheHouseofUsher
    The text of Fall of the House of Usher.

- CaskofAmontillado
    The text of Cask of Amontillado.

- ThePoems
    The text of The Poems.

- test_cases
    List of test files for testing the functions against all English texts.

- test_ids
    List of names in test cases for cleaner output of parameterized functions.
'''

import logging
import string
import os
import subprocess
from collections import Counter

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."

text_le_corbeau = "Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"

text_dict = {"but": 1, "the": 2, "raven": 1, "sitting": 1,
             "lonely": 1, "on": 1, "placid": 1, "bust": 1,
             "spoke": 1, "only": 1, "that": 2, "one": 2,
             "word": 2, "as": 1, "if": 1, "his": 1, "soul": 1,
             "in": 1, "he": 1, "did": 1, "outpour": 1}

text_list = ["but", "the", "raven", "sitting", "lonely", "on",
             "the", "placid", "bust", "spoke", "only", "that",
             "one", "word", "as", "if", "his", "soul", "in",
             "that", "one", "word", "he", "did", "outpour"]

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
    with open(file_path, 'r') as file:
        return file.read()

books_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'books'))

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