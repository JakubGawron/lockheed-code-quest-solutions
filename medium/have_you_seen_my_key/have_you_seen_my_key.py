import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def getPairs(string):
    return [string[i:i+2] for i in range(0, 128, 2)]

def decodeCipher(ciphertext, key):
    return [chr(int(pair[0], 16) ^ int(pair[1], 16)) for pair in zip(ciphertext, key)]

for _ in range(int(input())):
    X = int(input())
    ciphertext = getPairs(input())
    for _ in range(X):
        key = getPairs(input())
        plaintext = decodeCipher(ciphertext, key)
        print('[' + ''.join(plaintext) + ']') 