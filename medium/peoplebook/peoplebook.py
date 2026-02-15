import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    N = int(input())
    persons = {person[0]: person[1:] for person in zip(*[array.split(',') for array in input()[2:-2].split('],[')])}
    for _ in range(N):
        name = input()
        person = persons[name]
        print(f'Name: {name}\nAge: {person[0]}\nInstagram: {person[1]}\nTwitter: {person[2]}\nPhone: {person[3]}\nEmail: {person[4]}')