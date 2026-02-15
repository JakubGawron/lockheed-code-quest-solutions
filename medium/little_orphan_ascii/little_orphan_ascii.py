import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    W, T, P = map(int, input().split())

    Work_Order = {}
    Work_Task = {}
    Part = {}
    for _ in range(W):
        id, title, date = input().split(',')
        Work_Order[int(id)] = {'title': title, 'date': date}

    for _ in range(T):
        id, id_work_order, id_part, person_name = input().split(',')
        Work_Task[int(id)] = {'id_work_order': int(id_work_order), 'id_part': int(id_part), 'person_name': person_name}

    for _ in range(P):
        id, part_name, serial = input().split(',')
        Part[int(id)] = {'part_name': part_name, 'serial': serial}

    for id in sorted(Work_Task.keys()):
        show_msg, a, b = False, '', ''
        data = Work_Task[id]

        if data['id_work_order'] not in Work_Order.keys():
            show_msg = True
            a = 'MISSING WORK_ORDER ' + str(data['id_work_order'])

        if data['id_part'] not in Part.keys():
            show_msg = True
            b = 'MISSING PART ' + str(data['id_part'])
            if a: a += ' '
        
        if show_msg:
            print(id, a + b)