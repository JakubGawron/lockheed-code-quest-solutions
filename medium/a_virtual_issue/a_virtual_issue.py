import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    Frame0, Frame1, Frame2, QualityLevel = map(float, input().split())
    QualityLevel = int(QualityLevel)
    targetFrameTime = 1000/90
    LowThreshold = targetFrameTime * 0.7
    ExtrapolateThreshold = targetFrameTime * 0.85
    HighThreshold = targetFrameTime * 0.9
    if Frame2 > HighThreshold:
        QualityLevel -= 2
    elif Frame2 > ExtrapolateThreshold:
        QualityLevel -= 2
    elif Frame0 < LowThreshold and Frame1 < LowThreshold and Frame2 < LowThreshold:
        QualityLevel += 1

    print(min(10, max(1, QualityLevel)))