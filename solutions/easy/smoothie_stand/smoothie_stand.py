import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

smoothies = {
    "strawberry swirl": {"strawberry", "blueberry"},
    "banana burst": {"banana", "kiwi", "orange"},
    "tropical tango": {"kiwi", "orange", "mango", "blueberry"},
    "mango medley": {"mango", "strawberry", "blueberry", "banana"},
}

for _ in range(int(input())):
    ingredients = set(input().split("|"))

    if smoothies[input()].issubset(ingredients):
        print("YES")
        continue

    print("NO")
