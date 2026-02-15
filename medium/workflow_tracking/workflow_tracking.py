import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

requests = {
    '': {'C': 'New'},
    'New': {'S': 'Draft'},
    'Draft': {'S': 'Draft', 'B': 'Preliminary Review'},
    'Preliminary Review': {'S': 'Preliminary Review', 'X': 'Rejected', 'A': 'Final Review', 'R': 'Waiting Preliminary'},
    'Waiting Preliminary': {'I': 'Preliminary Review'},
    'Final Review': {'S': 'Final Review', 'X': 'Rejected', 'A': 'Approved', 'R': 'Waiting Final'},
    'Waiting Final': {'I': 'Final Review'},
    'Rejected': {'N': 'Customer Notified'},
    'Approved': {'N': 'Customer Notified'},
    'Customer Notified': {}
}

for _ in range(int(input())):
    state = ''
    id, commands = input().split(maxsplit=1)
    steps = []
    for command in commands.split():
        new_state = requests[state].get(command)
        if new_state:
            state = new_state
            steps.append(state)
        else:
            steps.append('Invalid Command')
    print(id, '>'.join(steps))