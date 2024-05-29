#!/bin/bash

# Create books directory
mkdir -p books

# List of book IDs
book_ids=("932" "1063" "1064" "2147" "2148" "2150" "10135" "17192" "32037" "51060")

# Loop through book_ids and download txt file
for id in "${book_ids[@]}"; do
	wget -O "books/poe_${id}.txt" "https://www.gutenberg.org/ebooks/${id}.txt.utf-8"
done
