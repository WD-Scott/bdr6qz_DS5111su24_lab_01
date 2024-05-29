#!/bin/bash

# Case-sensitive and case-insensitive  count of number of lines in The Raven containing 'raven'
raven_lower=$(grep -c 'raven' books/poe_17192.txt)
raven_title=$(grep -c 'Raven' books/poe_17192.txt)

echo "Lines containing 'raven' (lowercase): $raven_lower"
echo "Lines containing 'Raven' (title case): $raven_title"
