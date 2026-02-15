import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    N = int(input())
    stream = input()

    i = 0
    while i <= N - 3:
        token_start = stream[i:i + 3]
        token_end = token_start[::-1]
        
        if len(set(token_start)) == 3 and token_end in stream[i + 3:]:
            i += 3
            message = ''

            while i < N:
                if i <= N - 3 and stream[i:i + 3] == token_end:
                    i += 3
                    break
            
                message += stream[i]
                if stream[i] in token_start:
                    if i + 1 < N and stream[i] == stream[i + 1]:
                        i += 2
                    else:
                        i += 1
                else:
                    i += 1

            print(message)

        else:
            i += 1