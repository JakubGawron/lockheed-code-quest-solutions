import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
import string
import re

for _ in range(int(input())):
    numbers = re.findall(r'\d+', input())
    print([string.ascii_lowercase[int(number) - 1] for number in numbers])