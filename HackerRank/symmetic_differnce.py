# Read input
num_english = int(input().strip())
english_subs = set(map(int, input().strip().split()))

num_french = int(input().strip())
french_subs = set(map(int, input().strip().split()))

# Compute symmetric difference
unique_subs = english_subs.symmetric_difference(french_subs)

# Output the result
print(len(unique_subs))
