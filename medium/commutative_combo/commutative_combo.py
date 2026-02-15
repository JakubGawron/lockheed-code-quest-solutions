import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def parse_numbers(expr):
    return [int(num) for num in expr.split('+')]


def find_combos(
    num_list,
    found,
    flag,
    current_expr,
    curr_index,
    target_total,
    running_sum = 0,
):
    flag[curr_index] = True
    if running_sum > target_total:
        return
    
    if current_expr:
        current_expr += f'+{num_list[curr_index]}'
    else:
        current_expr = str(num_list[curr_index])
    if running_sum == target_total:
        found.add(current_expr)
        return
    for pos, number in enumerate(num_list):
        if not flag[pos]:
            find_combos(num_list, found, flag, current_expr, pos, target_total, running_sum + number)
            
            for k in range(pos + 1, len(num_list)):
                flag[k] = False


def generate_orderings(
    parts, used_part, orderings, built_expr
):
    for idx, part in enumerate(parts):
        if not used_part[idx]:
            saved_expr = built_expr
            used_part[idx] = True
            if built_expr:
                built_expr += f'+{part}'
            else:
                built_expr = part
            if False in used_part:
                generate_orderings(parts, used_part, orderings, built_expr)
            else:
                orderings.add(built_expr)
            built_expr = saved_expr
            used_part[idx] = False


def expand_permutations(combo_set):
    all_orderings = combo_set.copy()
    for combo_expr in combo_set:
        parts = combo_expr.split('+')
        generate_orderings(parts, [False] * len(parts), all_orderings, '')
    return all_orderings


for _ in range(int(input())):
    target_sum = int(input()[9:])
    candidate_numbers = sorted(list(map(int, input().split(','))), reverse=True)
    used_flags = [False] * len(candidate_numbers)
    combo_set: set[str] = set()
    for i, num in enumerate(candidate_numbers):
        find_combos(candidate_numbers, combo_set, used_flags, '', i, target_sum, num)
        for j in range(i + 1, len(used_flags)):
            used_flags[j] = False
    
    combo_set = expand_permutations(combo_set)
    
    final_list = sorted(list(combo_set), key=parse_numbers)
    for expr in final_list:
        print(expr)