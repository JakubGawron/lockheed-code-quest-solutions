import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    counted = []
    numbers = list(map(int, input().split()))
    lenght = len(numbers)
    counter = 0

    response = 'FALSE'
    for num in numbers:
        if num in counted:
            continue

        counted.append(num)

        n = numbers.count(num)
        if n == 3:
            response = 'TRUE'
            break

        counter += n
        if counter == lenght:
            break

    print(response)