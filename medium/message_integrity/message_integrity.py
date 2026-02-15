import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

P3 = [1, 0, 1, 1]
e = len(P3)
def checkIntegrity(data_chunk):
    if 1 not in data_chunk:
        return True
        
    i = data_chunk.index(1)
    if i > 7:
        return False
    data_chunk[i:i + e] = [a ^ b for a, b in zip(data_chunk[i:i + e], P3)]
    return checkIntegrity(data_chunk)

for _ in range(int(input())):
    data_chunk = list(map(int, input()))
    if checkIntegrity(data_chunk):
        print('ok')
    else:
        print('corrupt')

