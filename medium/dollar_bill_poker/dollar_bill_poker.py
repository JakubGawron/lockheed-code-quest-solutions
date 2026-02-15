import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    serial = input()
    counts = [serial.count(str(i)) for i in range(1, 10)]
    print(serial , '= ', end='')

    if max(counts) >= 5:
        print('FIVE OF A KIND')

    elif 4 in counts:
        print('FOUR OF A KIND')

    elif (3 in counts and 2 in counts) or (counts.count(3) >= 2):
        print('FULL HOUSE')

    else:
        straight = 0
        for i in range(5):
            for j in range(i, i + 5):
                if counts[j] == 0: break
            else:
                straight = 1
        
        if straight:
            print('STRAIGHT')

        elif 3 in counts:
            print('THREE OF A KIND')

        elif counts.count(2) >= 2:
            print('TWO PAIR')

        elif 2 in counts:
            print('PAIR')

        else:
            print(max(list(serial)))