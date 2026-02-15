import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re
#import math
#import string

input = lambda: input()

for _ in range(int(input())):
    for _ in range(int(input())):
        letters = [word[0] for word in input().upper().split()]
        letters.append(letters[1])
        letters.remove(letters[1])
        print(''.join(letters))