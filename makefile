default:
	@cat makefile | grep -E ".*:\s+#"
	
cat_makefile:          # this simply cats the makefile
	@cat makefile

setup:
	python3 -m venv env
	. env/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

# Job to download books by Edgar Allan Poe
get_texts:             # Create books directory and download texts
	@mkdir -p books
	@bash -c 'book_ids=("17192" "932" "1063" "10031" "14082"); \
	for id in $${book_ids[@]}; do \
		wget -O "books/poe_$${id}.txt" "https://www.gutenberg.org/ebooks/$${id}.txt.utf-8"; \
	done'
	
# Job to count lines in The Raven
raven_line_count:      # Count number of lines in The Raven
	@wc -l books/poe_17192.txt

# Job to count occurrences of 'raven' in The Raven
raven_counts:          # Count occurrences of 'raven' in The Raven
	@raven_lower=$$(grep -c 'raven' books/poe_17192.txt); \
	raven_title=$$(grep -c 'Raven' books/poe_17192.txt); \
	echo "Lines containing 'raven' (lowercase): $$raven_lower"; \
	echo "Lines containing 'Raven' (title case): $$raven_title"

# Job to count total lines in all downloaded books
total_lines:           # Count total number of lines in all books
	@wc -l books/*.txt

# Job to count total words in all downloaded books
total_words:           # Count total number of words in all books
	@wc -w books/*.txt

# Job to count words in The Raven
raven_word_count:      # Count the number of words in The Raven
	@wc -w books/poe_17192.txt

.PHONY: test
# Job to run only tests without the integration marker in the tests directory
test:
	pytest -m "not integration" tests -vvx

.PHONY: test_integration
# Job to run only tests with the integration marker in the tests directory
test_integration:
	pytest -m "integration" tests -vvx
