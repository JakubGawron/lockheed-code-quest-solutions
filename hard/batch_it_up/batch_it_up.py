import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re
import xml.etree.ElementTree as xml

for _ in range(int(input())):
    N = int(input())
    data, line = '', ''
    while '</parts>' not in line:
        line = input()
        data += line

    root = xml.fromstring(data)
    c = 1
    for i, part in enumerate(root.findall('part')):
        if i % N == 0:
            print(c)
            c += 1
        info = [
            part.get('number'),
            part.get('serial'),
            part.get('name')
        ]
        if not info[0]:
            info = [
                part.find('number').text,
                part.find('serial').text,
                part.find('name').text
            ]
        elif not info[1]:
            info[1] = part.text
        print(','.join(info))