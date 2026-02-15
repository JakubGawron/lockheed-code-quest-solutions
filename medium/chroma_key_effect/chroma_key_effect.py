import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

for _ in range(int(input())):
    Cr, Cg, Cb, T, Fr, Fg, Fb, Br, Bg, Bb = map(int, input().split())
    distance = math.sqrt((Cr-Fr)**2+(Cg-Fg)**2+(Cb-Fb)**2)
    if distance <= T:
        print(Br, Bg, Bb)
    else:
        print(Fr, Fg, Fb)