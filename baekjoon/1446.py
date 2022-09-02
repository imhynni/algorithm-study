# https://www.acmicpc.net/problem/1446
# 백준 1446 <지름길>
# Silver 1
from collections import defaultdict
import sys


def solution():
    n, d = map(int, sys.stdin.readline().split())
    shortcut = defaultdict(list)
    short_path = []
    distance = [i for i in range(d + 1)]
    for _ in range(n):
        u, v, w = map(int, sys.stdin.readline().split())
        if v > d:
            continue
        shortcut[u].append((v, w))
        short_path.append(v)
    for i in range(d + 1):
        for p in short_path:  # 그 전에서 지금
            if p < i:
                distance[i] = min(distance[i], distance[p] + i - p)
        if i in shortcut:  # 지금부터 다음 길
            for s in shortcut[i]:
                end, dist = s
                distance[end] = min(distance[end], distance[i] + dist)
    print(distance[d])


solution()
