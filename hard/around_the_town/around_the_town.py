import sys

input = lambda: sys.stdin.readline().rstrip()
import math

# import string
# import re
from decimal import ROUND_HALF_UP, Decimal


def halfUpRound(value, q=0, type="string"):
    rounded = Decimal(str(value)).quantize(
        Decimal(1).scaleb(-q), rounding=ROUND_HALF_UP
    )
    if rounded == Decimal(0):
        rounded = abs(rounded)
    if type == "string":
        return format(rounded, f".{q}f")
    return float(rounded)


def get_distance(A, B):
    x0, y0 = A
    x1, y1 = B
    return math.sqrt(math.pow(x0 - x1, 2) + math.pow(y0 - y1, 2))


for _ in range(int(input())):
    L, S = map(int, input().split())
    landmarks = [tuple(map(int, input().split())) for _ in range(L)]
    centroids = [tuple(map(int, input().split())) for _ in range(S)]

    change = 1
    while change:
        change = 0
        clusters = [[] for _ in range(S)]
        for landmark in landmarks:
            distances = [get_distance(landmark, centroid) for centroid in centroids]
            min_distance = min(distances)
            candidates = [
                i for i, distance in enumerate(distances) if distance == min_distance
            ]
            closest = min(candidates, key=lambda k: (centroids[k][0], centroids[k][1]))
            clusters[closest].append(landmark)

        for i, cluster in enumerate(clusters):
            if cluster:
                cluster_len = len(cluster)
                x = sum(point[0] for point in cluster) / cluster_len
                y = sum(point[1] for point in cluster) / cluster_len
                if centroids[i] != (x, y):
                    centroids[i] = (x, y)
                    change = 1

    for centroid in centroids:
        print(" ".join(halfUpRound(cordinate, 1) for cordinate in centroid))
