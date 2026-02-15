import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
import re

for _ in range(int(input())):
    text = ' '.join(input() for _ in range(int(input())))
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])', text) if s.strip()]
    keyword = input()

    for sentence in sentences:
        words = sentence.split()
        for i, word in enumerate(words):
            clean_word = re.sub(r'[^a-z]', '', word.lower())
            if clean_word == keyword:
                start = max(0, i - 3)
                end = min(len(words), i + 6)
                context = words[start:end]
                context[i - start] = f'*{context[i - start]}*'
                result = ' '.join(context)
                if start > 0:
                    result = '...' + result
                if end < len(words):
                    result += '...'
                print(result)