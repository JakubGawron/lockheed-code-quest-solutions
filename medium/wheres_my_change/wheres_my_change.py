import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

bills = [10000, 5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1]

for _ in range(int(input())):
    withdraw = int(round(float(input()) * 100))
    output = ''

    for bill in bills:
        amount = withdraw // bill
        output += str(amount)
        withdraw -= bill * amount

    print(output)
