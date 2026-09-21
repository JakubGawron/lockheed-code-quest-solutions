import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

for _ in range(int(input())):
    line = input()
    stack = []
    current_num = 0
    current_str = ""

    for char in line:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "(":
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ")":
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += char

    print(current_str)
