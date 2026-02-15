import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    songs = [tuple(input().split(' - ', maxsplit=1)) for _ in range(int(input()))]
    print('\n'.join([' - '.join(listing) for listing in sorted(songs, key=lambda k: ((k[1][4:] if k[1].startswith('The ') else k[1]).lower(), k[0].lower()))]))