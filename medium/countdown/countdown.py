import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re
from datetime import datetime

for _ in range(int(input())):
    start, end = input().split('|')
    start = datetime.strptime(start, "%m.%d.%Y %H:%M:%S")
    end = datetime.strptime(end, "%m.%d.%Y %H:%M:%S")
    numSeconds = (end - start).total_seconds()
    numMinutes = numSeconds / 60
    numSeconds = int(numSeconds % 60)
    numHours = numMinutes / 60
    numMinutes = int(numMinutes % 60)
    numDays = int(numHours / 24)
    numHours = int(numHours % 24)
    print('{:02d} Day{} {:02d} Hour{} {:02d} Minute{} {:02d} Second{}'.format(
        numDays, '' if numDays == 1 else 's',
        numHours, '' if numHours == 1 else 's',
        numMinutes, '' if numMinutes == 1 else 's',
        numSeconds, '' if numSeconds == 1 else 's'
    ))