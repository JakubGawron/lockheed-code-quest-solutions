import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re
from datetime import datetime, timedelta

format = '%m/%d/%Y %H:%M'
for _ in range(int(input())):
    date, diff = input().rsplit(maxsplit=1)
    date = datetime.strptime(date, format)
    date -= timedelta(hours=float(diff))
    print(date.strftime(format))