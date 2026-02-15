import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
import re

def simplify(str):
    return re.sub('[^a-z]', '', str.lower())

for _ in range(int(input)):
    greetings, response = input().split('|')
    greetings = simplify(greetings)
    response = simplify(response)
    if set(response).issubset(set(greetings)):
        print("That's my secret contact!")
    else:
        print("You're not a secret agent!")