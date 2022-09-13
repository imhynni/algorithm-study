# https://www.acmicpc.net/problem/2961
# 백준 2961 <도영이가 만든 맛있는 음식>
# Silver 2
from itertools import combinations
import sys


def solution():
    n = int(sys.stdin.readline())
    ingredient = []
    diff = sys.maxsize
    comb = []

    for _ in range(n):
        s, b = map(int, sys.stdin.readline().split())
        ingredient.append((s, b))

    for i in range(1, n + 1):
        comb.append(combinations(ingredient, i))

    for c in comb:
        for ing in c:
            s, b = 1, 0
            for i in ing:
                s *= i[0]
                b += i[1]
            diff = min(diff, abs(s - b))
    print(diff)


solution()
