# https://www.acmicpc.net/problem/10816
# 백준 10816 <숫자 카드 2>
# Silver 4

import sys
from bisect import bisect_left, bisect_right


def solution():
    n = int(sys.stdin.readline())
    cards = sorted(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    count = []

    for num in nums:
        count.append(bisect_right(cards, num) - bisect_left(cards, num))

    for c in count:
        print(c, end=' ')


solution()
