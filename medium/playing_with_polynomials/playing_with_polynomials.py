import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    polynomials = [list(map(int, input().split())) for _ in range(2)]
    coefficients = [0] * (len(polynomials[0]) + len(polynomials[1]) - 1)
    for i, c1 in enumerate(polynomials[0]):
        for j, c2 in  enumerate(polynomials[1]):
            coefficients[i + j] += c1 * c2 

    output = ''
    for exponent, coefficient in enumerate(coefficients):
        if exponent == 0 and coefficient:
            output += str(coefficient)
        elif coefficient:
            if coefficient > 0:
                output += '+'
            else:
                output += '-'

            if abs(coefficient) != 1:
                output += str(abs(coefficient))
            output += 'x'
            if exponent != 1:
                output += '^' + str(exponent)

    output = output[1:] if output[0] == '+' else output                
    print(output)