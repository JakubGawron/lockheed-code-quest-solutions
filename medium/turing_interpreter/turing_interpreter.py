import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    instructions = {}
    for _ in range(int(input())):
        instruction = input()[1:-1].split(', ') 
        instructions[''.join(instruction[:2])] = instruction[2:]
    tape = input().split()
    state = 'A'
    len_tape = len(tape)
    i = len_tape // 2

    for _ in range(int(input())):
        i %= len_tape
        key = state + tape[i]
        if key not in instructions:
            continue
        instruction = instructions[key]
        tape[i] = instruction[0]
        if instruction[1] == 'R':
            i += 1
        else:
            i -= 1
        state = instruction[2]
    
    print(' '.join(tape))