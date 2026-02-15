import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
import re

for _ in range(int(input())):
    text = input()
    print(re.sub('[^a-zA-Z0-9 ]', '', text))