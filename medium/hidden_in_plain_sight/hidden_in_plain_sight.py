import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    X = int(input())
    hidden_text = ''
    for _ in range(X):
        word, i = input().split('|')
        hidden_text += word[int(i)]
    print(hidden_text)