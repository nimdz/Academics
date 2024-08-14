#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    a += 'z'
    b += 'z'
    i = j = 0
    res = ""
    while i < len(a) and j < len(b):
        if a[i:] < b[j:]:
            res += a[i]
            i += 1
        else:
            res += b[j]
            j += 1
    return res[:-1]
# Main code to handle input and output
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    t = int(data[0])
    index = 1
    
    results = []
    for _ in range(t):
        a = data[index]
        b = data[index + 1]
        index += 2
        results.append(morganAndString(a, b))
    
    for result in results:
        print(result)



