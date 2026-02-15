import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

for _ in range(int(input())):
    bank = 0
    for _ in range(int(input())):
        money = float(input())
        system_money = math.ceil(money)
        bank += (system_money-money)
        print(system_money)
    print(f'{bank:.2f}')