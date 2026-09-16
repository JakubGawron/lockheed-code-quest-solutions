import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
import re

for _ in range(int(input())):
    line = input()
    if re.search(
        r"('; .* --|\${.*}|\$\(.*\)|&& sudo|&& su -|;;|%s|%x|%n)", line
    ) or re.search("(' OR 1=1|<script)", line, re.IGNORECASE):
        print("REJECTED")
    else:
        print(line)
