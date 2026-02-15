import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

values = 'DCBA'
for _ in range(int(input())):
    school = input()
    highest = [0, 0]
    student = ''
    for _ in range(int(input())):
        name, grades = input().split(':')
        grades = grades.split(',')
        gradeP, creditH = 0, 0
        for grade in grades:
            points = values.index(grade[0])+1
            credit = int(grade[1])
            gradeP += points*credit
            creditH += credit
        GPA = gradeP/creditH
        if highest[0] < GPA or (highest[0] == GPA and highest[1] < creditH):
            highest[0] = GPA
            highest[1] = creditH
            student = name
    print(school, '=', student)