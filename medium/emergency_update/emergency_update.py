import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    O, N = map(int, input().split())
    old, new = {}, {}
    
    for _ in range(O):
        data = input().split(',')
        old[data[0]] = data[1:]

    for _ in range(N):
        data = input().split(',')
        new[data[0]] = data[1:]

    deleted = old.keys() - new.keys()
    created = new.keys() - old.keys()
    updated = new.keys() & old.keys()
    
    for name in sorted(set(list(old.keys()) + list(new.keys()))):
        if name in deleted:
            print(name, 'DELETED')
        elif name in created:
            print(name, 'CREATED')
        elif name in updated and old[name] != new[name]:
            print(name, 'UPDATED', end=' ')
            if old[name][0] != new[name][0] and old[name][1] != new[name][1]:
                print('BOTH')
            elif old[name][1] != new[name][1]:
                print('ADDRESS')
            else:
                print('PHONE NUMBER')