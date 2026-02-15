import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

encode_dict = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K', 'F': 'J', 'G': 'W', 'H': 'L', 'I': 'C', 'J': 'V', 'K': 'K', 'L': 'A', 'M': 'F', 'N': 'K', 'O': 'A', 'P': 'D', 'Q': 'L', 'R': 'T', 'S': 'B', 'T': 'P', 'U': 'N', 'V': 'V', 'W': 'B', 'X': 'X', 'Y': 'J', 'Z': 'Z'}

for _ in range(int(input())):
    print(''.join([encode_dict[char] for char in input()]))