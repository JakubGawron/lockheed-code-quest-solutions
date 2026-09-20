import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
import re

for _ in range(int(input())):
    line = re.sub(r"[^A-Za-z\s-]", "", input())
    words = re.split(r"[\s-]+", line)
    acronym = "".join(word[0].upper() for word in words if word)
    print(acronym)
