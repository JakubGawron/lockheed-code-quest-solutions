import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re
from collections import Counter

for _ in range(int(input())):
    line = input()
    characters_count = len(line)

    characters = Counter(line)
    words = characters.get(" ", 0) + 1

    print(line)
    print("-" * characters_count)
    print("CHARACTERS:", characters_count)
    print("WORDS:", words)
    for character, occurencies in characters.most_common():
        print(character + ": " + str(occurencies))
