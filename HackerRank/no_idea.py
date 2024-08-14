# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input values
n, m = map(int, input().split())
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

# Initialize happiness
happiness = 0

# Calculate happiness based on the array elements
for item in array:
    if item in set_a:
        happiness += 1
    if item in set_b:
        happiness -= 1

# Output the final happiness
print(happiness)