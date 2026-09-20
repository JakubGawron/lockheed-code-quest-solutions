import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
import string

# import re

for _ in range(int(input())):
    letter = input()[-2]
    if letter in string.ascii_letters:
        print(letter)
        continue
    print("No Letter Found")
