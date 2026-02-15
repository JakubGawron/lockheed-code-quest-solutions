import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
import re
from collections import defaultdict

from decimal import Decimal, ROUND_HALF_UP
def halfUpRound(value, q = 0, type = 'string'):
    rounded = Decimal(str(value)).quantize(Decimal('1').scaleb(-q), rounding=ROUND_HALF_UP)
    if rounded == Decimal('0'):
        rounded = abs(rounded)
    if type == 'string':
        return format(rounded, f'.{q}f')
    return float(rounded)

for _ in range(int(input())):
    digraphs, trigraphs = defaultdict(int), defaultdict(int)
    digraphs_len, trigraphs_len = 0, 0
    for _ in range(int(input())):
        text = re.sub('[^A-Z ]', '', input().upper())
        for term in re.findall('(?=([A-Z]{2}))', text):
            digraphs[term] += 1
            digraphs_len += 1
        for term in re.findall('(?=([A-Z]{3}))', text):
            trigraphs[term] += 1
            trigraphs_len += 1

    for term, occurence in sorted(digraphs.items(), key=lambda k: k[0]):
        print(f'{term}: {halfUpRound(occurence/digraphs_len*100, 3)}%')

    for term, occurence in sorted(trigraphs.items(), key=lambda k: k[0]):
        print(f'{term}: {halfUpRound(occurence/trigraphs_len*100, 3)}%')