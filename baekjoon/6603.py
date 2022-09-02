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
        c_list = list(combinations(s, 6))
        for c in c_list:
            print(' '.join(c))
        print()


solution()
