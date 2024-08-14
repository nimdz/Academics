class EvenStream:
    def __init__(self):
        self.current = 0
        
    def get_next(self):
        result = self.current
        self.current += 2
        return result

class OddStream:
    def __init__(self):
        self.current = 1
        
    def get_next(self):
        result = self.current
        self.current += 2
        return result

def print_from_stream(n, stream=None):
    # Use EvenStream as default if no stream is provided
    if stream is None:
        stream = EvenStream()
    
    for _ in range(n):
        print(stream.get_next())

# Read input
import sys
input = sys.stdin.read
data = input().strip().split('\n')

# First line contains the number of queries
num_queries = int(data[0].strip())

# Process each query
for i in range(1, num_queries + 1):
    stream_name, n = data[i].strip().split()
    n = int(n)
    
    if stream_name == 'even':
        print_from_stream(n)
    elif stream_name == 'odd':
        print_from_stream(n, OddStream())
