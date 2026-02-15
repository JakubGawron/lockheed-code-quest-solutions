import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    C, T = map(int, input().split(','))
    tasks = []
    for _ in range(T):
        task = input().split(',') 
        tasks.append([task[0]] + list(map(int, task[1:])))
    tasks = sorted(tasks, key=lambda k: -k[1])

    for i in range(1, C + 1):
        task = next((task for task in tasks if task[2] <= i), ['Wait', 0, 0, 0])
        if task[3] == 0: pass
        elif task[3] == 1: tasks.remove(task)
        else: task[3] -= 1
        print(str(i) + ',' + task[0])