import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_UP, ROUND_DOWN, ROUND_HALF_EVEN

def dRound(value, option, places=0):
    value = Decimal(str(value))
    quantize_place = Decimal('1').scaleb(-places)
    
    if option == 'HU':
        result = value.quantize(quantize_place, rounding=ROUND_HALF_UP)
    elif option == 'HD':
        result = value.quantize(quantize_place, rounding=ROUND_HALF_DOWN)
    elif option == 'U':
        result = value.copy_abs().quantize(quantize_place, rounding=ROUND_UP)
        if value < 0:
            result = -result
    elif option == 'D':
        result = value.copy_abs().quantize(quantize_place, rounding=ROUND_DOWN)
        if value < 0:
            result = -result
    elif option == 'HE':
        result = value.quantize(quantize_place, rounding=ROUND_HALF_EVEN)
    elif option == 'HO':
        multiplied = value / quantize_place
        rounded = multiplied.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        remainder = multiplied - rounded
        if remainder == Decimal('0.5'):
            if int(rounded) % 2 == 0:
                if rounded > 0:
                    rounded += 1
                else:
                    rounded -= 1
        result = rounded * quantize_place
    return '{0:f}'.format(result.normalize())

for _ in range(int(input())):
    value, option, places = input().split()
    places = int(places)
    print(dRound(value, option, places))
