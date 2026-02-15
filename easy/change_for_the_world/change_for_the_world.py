import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

money = 0

def checkup(bill):
    global money
    money = round(money, 2)
    i = 1
    while i*bill <= money: i += 1
    money -= (i-1)*bill
    return i-1

for _ in range(int(input())):
    text = input()
    print(text)
    money = float(text[1:])
    print(f'Quarters={checkup( 0.25 )}')
    print(f'Dimes={checkup( 0.1 )}')
    print(f'Nickels={checkup( 0.05 )}')
    print(f'Pennies={checkup( 0.01 )}')