import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def rpn(infix):
    operators = {
        '(': 4,
        ')': 4,
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
    }
    stack = []
    postfix = []
    for symbol in infix.split():
        if symbol not in operators:
            postfix.append(symbol)
        elif symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and (
                operators[symbol] < operators[stack[-1]] or
                (operators[symbol] == operators[stack[-1]] and symbol != '^')
            ):
                postfix.append(stack.pop())
            stack.append(symbol)
    while stack: postfix.append(stack.pop())
    return ' '.join(postfix)

for _ in range(int(input())):
    for _ in range(int(input())):
        print(rpn(input()))