import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
import re
import string

for _ in range(int(input())):
    keyword = input()
    plaintext = re.sub(r"[^a-z]", "", input()).upper()
    keyword = keyword + plaintext
    keyword = repeated = (keyword * (len(plaintext) // len(keyword) + 1))[
        : len(plaintext)
    ]

    ciphertext = ""
    for p, k in zip(plaintext, keyword):
        p_index = string.ascii_uppercase.index(p)
        k_index = string.ascii_uppercase.index(k)
        index = (p_index + k_index) % 26
        ciphertext += string.ascii_uppercase[index]

    print(ciphertext)
