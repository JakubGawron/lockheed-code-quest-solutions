import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    D, W = map(int, input().split())

    dict_words = []
    for _ in range(D):
        dict_words.append(input())

    for _ in range(W):
        misspelled_word = input()

        best_match = ''
        HD = -1
        for dict_word in [word for word in dict_words if len(word) == len(misspelled_word)]:
            currentHD = 0
            for i, letter in enumerate(dict_word):
                if letter == misspelled_word[i]: currentHD += 1
            if currentHD > HD:
                HD = currentHD
                best_match = dict_word
        print(best_match)