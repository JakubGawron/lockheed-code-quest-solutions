import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
import re

for _ in range(int(input())):
    input = input()
    if re.search("('; .* --|\${.*}|\$\(.*\)|&& sudo|&& su -|;;|%s|%x|%n)", input) or re.search("(' OR 1=1|<script)", input, re.IGNORECASE):
        print('REJECTED')
    else:
        print(input)