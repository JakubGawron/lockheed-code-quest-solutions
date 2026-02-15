import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    word, index = input().split()
    index = int(index)
    print(word[:index]+word[index+1:])