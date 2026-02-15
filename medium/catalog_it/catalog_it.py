import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

catalog = {}
nodes = {}
for _ in range(int(input())):
    name, category = input().split(',')
    nodes[name] = nodes.get(name, {})
    if category == "None":
        catalog[name] = nodes[name]
    else:
        nodes[category] = nodes.get(category, {})
        nodes[category][name] = nodes[name]

def sort(dictio):
    return {key: sort(val) for key, val in sorted(dictio.items())}

def show(dictio, deep = 0):
    for key, val in dictio.items():
        print('-' * deep + key)
        show(val, deep + 1)

show(sort(catalog))