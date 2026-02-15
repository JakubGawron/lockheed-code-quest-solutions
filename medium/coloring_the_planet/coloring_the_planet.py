import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

def find_rel_val(value, min, max):
    return (value - min) / (max - min)

def lerp(a, b, t):
    return (1 - t) * a + t * b

for _ in range(int(input())):
    N, L, H = map(int, input().split())
    control_points = [] 
    for _ in range(N):
        position, R, G, B = map(float, input().split())
        R, G, B = map(int, (R, G, B))
        control_points.append([position, R, G, B])
    temp = int(input())
    finded_position = find_rel_val(temp, L, H)
    for i in range(N - 1):
        if control_points[i][0] <= finded_position and control_points[i + 1][0] >= finded_position:
            control_points = [control_points[i], control_points[i + 1]]
            break
    ranges = find_rel_val(finded_position, control_points[0][0], control_points[1][0])
    output = [str(math.floor(lerp(control_points[0][i + 1], control_points[1][i + 1], ranges))) for i in range(3)]
    print(' '.join(output))