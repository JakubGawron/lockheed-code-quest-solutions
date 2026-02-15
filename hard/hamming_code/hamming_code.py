import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def hamming_code(binary_number):
    bits, parity = [], 0
    p, i = 0, 1
    i = 1
    while binary_number:
        if not (i & (i - 1)):
            bits.append('P')
            p += 1
        else:
            bit = binary_number[0]
            if int(bit):
                if parity:
                    parity ^= i
                else:
                    parity = i
            bits.append(bit)
            binary_number = binary_number[1:]
        i += 1

    iterator = iter(bin(parity)[2:].zfill(p)[::-1])
    return ''.join(next(iterator) if bit == 'P' else bit for bit in bits)

for _ in range(int(input())):
    for _ in range(int(input())):
        print(hamming_code(input()))
        
