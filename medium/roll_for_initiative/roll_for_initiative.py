import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    C, P = map(int, input().split())
    class_abilities = {}
    for _ in range(C):
        name, abilities = input().split(maxsplit=1)
        class_abilities[name] = abilities.split()
    
    for _ in range(P):
        name, scores = input().split(maxsplit=1)
        scores = sorted(map(int, scores.split()), reverse=True)
        scores = dict(zip(class_abilities[name], scores))
        print(name)
        print('STR:', scores['STR'])
        print('DEX:', scores['DEX'])
        print('CON:', scores['CON'])
        print('INT:', scores['INT'])
        print('WIS:', scores['WIS'])
        print('CHA:', scores['CHA'])