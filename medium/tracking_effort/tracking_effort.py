import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re
from collections import defaultdict

for _ in range(int(input())):
    tasks = defaultdict(int)
    input()
    last_name = last_minutes = None

    while last_name != 'End Day':
        name, time = input().split('|')
        minutes = int(time[:2]) * 60 + int(time[2:])
        if last_minutes: 
            tasks[last_name] += minutes - last_minutes
        last_name, last_minutes = name, minutes

    print('\n'.join(f'{name}-{minutes // 60}.{int(minutes % 60 / 6)}' for name, minutes in sorted(tasks.items())))