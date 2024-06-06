# Default target
default: show_makefile

# Job to print the content of the Makefile
show_makefile:
	cat makefile

# Job to download 10 books by  Edgar Allan Poe
get_texts:
	bash get_the_books.sh
	
# Job to count lines in The Raven
raven_line_count:
	bash raven_line_count.sh

# Job to count occurrences of 'raven' in The Raven
raven_counts:
	bash raven_counts.sh

# Job to count total lines in all downloaded books
total_lines:
	bash total_lines.sh

# Job to count total words in all downloaded books
total_words:
	bash total_words.sh

# Job to count words in The Raven
raven_word_count:
	bash raven_word_count.sh
