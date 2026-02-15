import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    N = int(input())
    primes = []
    numbers = list(range(2, N + 1))
    i = 0
    while i < len(numbers) - 1:
        prime = numbers[i]
        composite = set(range(prime * 2, N + 1, prime))
        composite_len = len([num for num in numbers if num in composite])
        numbers = [num for num in numbers if num not in composite]
        if composite_len: print(f'Prime {prime} Composite Set Size: {composite_len}')
        i += 1
    print('{' + ','.join(map(str, numbers)) + '}')