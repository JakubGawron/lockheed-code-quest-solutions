import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    dict = {}
    for _ in range(int(input())):
        ip, mac = input().split()
        if ip not in dict:
            dict[ip] = [tuple(map(int, ip.split('.'))), set()]
        dict[ip][1].add(mac)
    print('\n'.join([f'{ip} {len(details[1])}' for ip, details in sorted(dict.items(), key=lambda k: k[-1][0])]))