import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    events = {}
    for _ in range(int(input())):
        id, name, session, event, is_team = input().split(',')
        is_day = session == 'Day'

        if is_team == 'true':
            if event not in events:
                events[event] = [0, 0]
            if is_day:
                events[event][0] += 1
            else:
                events[event][1] += 1
    
    print('\n'.join([event[0] + ',' + ','.join(map(str, event[1])) for event in sorted(events.items(), key=lambda k: k[0])]))