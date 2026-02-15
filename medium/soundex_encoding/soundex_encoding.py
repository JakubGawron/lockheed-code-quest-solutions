import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
import re
import re

def soundex(name):
    groups = {
        '1': 'bfpv',
        '2': 'cgjkqsxz',
        '3': 'dt',
        '4': 'l',
        '5': 'mn',
        '6': 'r'
    }
    vowels = 'aeiouy'
    wild = 'hw'
    name = name.lower()

    changed = True
    while changed:
        changed = False
        i = 0
        new = list(name)

        while i < len(new) - 1:
            c1 = new[i]
            c2 = new[i + 1]

            group = None
            for g in groups.values():
                if c1 in g:
                    group = g
                    break

            if group and (c2 in group or c2 in wild):
                new.pop(i + 1)
                changed = True
            else:
                i += 1

        name = ''.join(new)

    first = name[0].upper()
    name = re.sub(f'[{vowels}{wild}]', '', name[1:])

    code = name
    for num, letters in groups.items():
        code = re.sub(f'[{letters}]', num, code)
    code = re.sub(r'[a-z]', '0', code)

    return first + (code + '000')[:3]


for _ in range(int(input())):
    soundexes = {}
    for _ in range(int(input())):
        sd = soundex(input())
        if sd not in soundexes:
            soundexes[sd] = 1
        else:
            soundexes[sd] += 1

    print('OUTPUT')
    print('\n'.join(f'{sd} {soundexes[sd]}' for sd in sorted(soundexes)))
