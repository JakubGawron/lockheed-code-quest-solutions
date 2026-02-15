import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    channel1 = map(float, input().split())
    channel2 = list(map(float, input().split()))

    multipaction = []
    for i, power in enumerate(channel1):
        if 0.6 <= power <= 0.85 and 0.6 <= channel2[i] <= 0.85:
            multipaction.append(str(i))

    if multipaction:
        if len(multipaction) != 1:
            indexes = ' '.join(multipaction)
            print(f'{len(multipaction)} multipaction events were detected at time indices: {indexes}.')
        else:
            print(f'A multipaction event was detected at time index {multipaction[0]}.')
    else:
        print('No multipaction events detected.')