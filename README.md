# bdr6qz_DS5111su24_lab_01
Wyatt Scott's (bdr6qz) repo for DS5111 Labs

<details>
<summary><h1 style="font-size: 16px;">Manifest</h1></summary>

### makefile

### README.md

### License

<details>
<summary><h3 style="font-size: 14px;">tokenizer.py</h3></summary>

This Python module file contains the functions and objects available in the dropdown menus below.

<details>
<summary><strong>Click here to see the functions in tokenizer.py</strong></summary>

- `clean_text(text)`:

  Remove punctuation from the input string and convert it to lowercase.

- `tokenize(text)`:

  Split the input string into a list of words.

- `count_words(text)`:

  Count the frequency of each word in the input string.

- `run_bash(command)`:

  Run a bash command and return its output.

- `read_file(file_path)`:

  Read the contents of a file.
</details>

<details>
<summary><strong>Click here to see the objects in tokenizer.py</strong></summary>

- text

  Testing sentence from The Raven.

- text_dict

  Dictionary of `text` testing sentence to compare with `count_words` output.

- test_list

  List of `text` testing sentence to compare with `tokenize` output.

- books_dir

  The path for the `books` directory (available only after a user runs `make get_texts`).

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
</details>
</details>

<details>
<summary><h3 style="font-size: 14px;">Tests.py</h3></summary>
    
This directory contains Python module files for testing the functions in `tokenizer.py`.


#### - `test_count_words.py`

<details>
<summary><strong>Click here to see the functions in test_count_words.py</strong></summary>

- `test_count_words()`:

  Test `count_words`.

- `test_fail_count_words()`:

  Purposefully fail when testing `count_words`.

- `test_bash_count_words()`:

  Test `count_words` using bash.

- `test_count_words_skipper()`:

  Test function to show pytest mark and skipping.

- `test_all_count_words()`:

  Test `count_words` on all the English texts.

- `test_corbeau_count_words()`:

  Tests `count_words` against snippet from Le Corbeau
</details>

#### - `test_tokenizer.py`

<details>
<summary><strong>Click here to see the functions in test_tokenizer.py</strong></summary>

- `test_tokenize()`:

  Test `tokenize`.

- `test_fail_tokenize()`:

  Purposefully fail when testing `tokenize`.

- `test_bash_tokenize()`:

  Test `tokenize` using bash.

- `test_tokenize_skipper()`:

  Test function to show pytest mark and skipping.

- `test_all_tokenize()`:

  Test `tokenize` on all the English texts.

- `test_corbeau_tokenize()`:

  Tests `tokenize` against snippet from Le Corbeau
</details>

#### - `test_clean_text.py`

<details>
<summary><strong>Click here to see the functions in test_clean_text.py</strong></summary>

- `test_clean_text()`:

  Test `clean_text`.

- `test_fail_clean_text()`:

  Purposefully fail when testing `clean_text`.

- `test_bash_clean_text()`:

  Test `clean_text` using bash.

- `test_clean_text_skipper()`:

  Test function to show pytest mark and skipping.

- `test_all_clean_text()`:

  Test `clean_text` on all the English texts.

- `test_corbeau_clean_text()`:

  Tests `clean_text` against snippet from Le Corbeau
</details>
</details>
</details>

<details>
<summary><h1 style="font-size: 16px;">Minimal Reproducible Code</h1></summary>

### Getting Started:

To get started, clone this repo and in the Command Line run:

```
make setup
```

This will create a virtual environment with Python 3 and install the required packages stored in `requirements.txt`.

### Downloading Books

To download the books, in the Command Line you can run:

```
make get_texts
```

This will create a new directory, `books`, within which it will download the specified books by Edgar Allan Poe.

### Checking various characteristics of the books

The makefile includes several jobs that allow you to check difference characteristics of the now-downloaded books. To see how many words are in "The Raven," for example, you can run:

```
make raven_word_count
```
