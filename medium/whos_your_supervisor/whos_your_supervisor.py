import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    hierarchy = {}
    employees = set()

    for _ in range(int(input())):
        manager = input()
        employees.add(manager)

        for _ in range(int(input())):
            employee = input()
            hierarchy[employee] = manager
            employees.add(employee)

    for person in sorted(employees):
        chain = [person]
        current = person
        while current in hierarchy:
            current = hierarchy[current]
            chain.append(current)
        print('/'.join(chain))
