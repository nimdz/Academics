import re

# Define the regular expressions
regex_integer_in_range = r"^[1-9][0-9]{5}$"  # Matches six-digit numbers from 100000 to 999999
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"  # Matches alternating repetitive digit pairs

# Read input
P = input().strip()

# Validate the postal code
is_valid = (bool(re.match(regex_integer_in_range, P)) 
            and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# Output the result
print(is_valid)
