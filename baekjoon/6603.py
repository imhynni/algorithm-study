# https://www.acmicpc.net/problem/6603
# 백준 6603 <로또>
# Silver 2

import sys
from itertools import combinations


def solution():
    while True:
        k, *s = sys.stdin.readline().rstrip().split()
        if k == '0':
            break
        for c in combinations(s, 6):
            print(*c)
        print()


solution()
