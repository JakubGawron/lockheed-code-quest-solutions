import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    Y, X = map(int, input().split(','))
    panels, m, qm = map(int, input().split(','))
    
    heights = []
    for _ in range(Y):
        row = list(map(float, input().split(',')))
        row += [0.0] * (X - len(row))
        heights.extend(row)
 
    needed_panels, needed_m, needed_qm = Y * X, 0, 0

    for h in heights:
        if h == 0:
            needed_panels -= 1
            continue
        units = round(h * 4)
        needed_m += units // 4
        needed_qm += units % 4

    used_panels = min(panels, needed_panels)
    used_m = min(m, needed_m)
    used_qm = min(qm, needed_qm)

    missing_m = needed_m - used_m
    left_qm = qm - used_qm
    if left_qm != 0 and missing_m > 0:
        ad_qm = min(missing_m, left_qm // 4) * 4
        used_qm += ad_qm
        needed_m -= ad_qm // 4
        needed_qm += ad_qm
    
    remaining_panels = panels - needed_panels
    remaining_m = m - needed_m
    remaining_qm = qm - needed_qm
    print(f'{used_panels} ({remaining_panels}),{used_m} ({remaining_m}),{used_qm} ({remaining_qm})')