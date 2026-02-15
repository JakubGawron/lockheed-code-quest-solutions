import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

def printOutReport(path, wrong):
    if len(wrong) == 0:
        print(path, 'ALL GOOD')
    else:
        print(path + '\n' + '\n'.join([name + ': WRONG PERM: ' + ', '.join(perm) for name, perm in wrong.items()]))

for _ in range(int(input())):
    type, u, g, o, N = input().split()
    type = 'd' if type == 'D' else '-'
    N = int(N)

    path, wrong, first = '', {}, 1
    for _ in range(N):
        data = input().split()
        if len(data) == 1:
            if first: first = 0
            else: printOutReport(path, wrong)
            wrong = {}
            path = data[0]
        else:
            ftype = data[0][0]
            uperm = data[0][1:4]
            gperm = data[0][4:7]
            operm = data[0][7:10]
            name = data[-1]
            if type == ftype:
                if u != uperm:
                    wrong.setdefault(name, []).append('Owner')
                if g != gperm:
                    wrong.setdefault(name, []).append('Group')
                if o != operm:
                    wrong.setdefault(name, []).append('Other')
    printOutReport(path, wrong)
    