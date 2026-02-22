import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def get_rotations(bricks):
    return [
        [
            (min(a, b), max(a, b), h)
            for a, b, h in (
                (x, y, z),
                (z, x, y),
                (y, z, x)
            )
        ] 
        for x, y, z in bricks
    ]

def max_skyscraper_height(bricks, N):
    rotations = get_rotations(bricks)
    used = [0] * N

    def build(l_a, l_b):
        best = 0

        for i in range(N):
            if used[i]: continue

            for a, b, h in rotations[i]:
                if l_a == -1 or (a <= l_a and b <= l_b):
                    used[i] = 1
                    h += build(a, b)
                    best = max(best, h)
                    used[i] = 0

        return best
    
    return build(-1, -1)

for _ in range(int(input())):
    N = int(input())
    bricks = [list(map(int, input().split('x'))) for _ in range(N)]
    print(max_skyscraper_height(bricks, N))