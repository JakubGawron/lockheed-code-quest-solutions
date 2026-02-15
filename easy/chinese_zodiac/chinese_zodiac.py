import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

for _ in range(int(input())):
    year = int(input())
    aspect = 'Yang' if year % 2 == 0 else 'Yin'
    element = ['Wood', 'Fire', 'Earth', 'Metal', 'Water'][math.floor((year-4)%10/2)]
    animal = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig'][(year-4)%12]
    print(year, aspect, element, animal)