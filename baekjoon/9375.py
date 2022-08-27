# https://www.acmicpc.net/problem/9375
# 백준 9375 <패션왕 신해빈>
# Silver 3

import sys
from collections import defaultdict


def solution():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        clothes = defaultdict(list)
        answer = 1
        for _ in range(n):
            name, c_type = sys.stdin.readline().rstrip().split()
            clothes[c_type].append(name)
        for c in clothes.values():
            answer *= (len(c) + 1)
        print(answer - 1)


solution()
