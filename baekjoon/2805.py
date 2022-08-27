# https://www.acmicpc.net/problem/2805
# 백준 2805 <나무 자르기>
# Silver 2

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    height = list(map(int, sys.stdin.readline().split()))
    start, end = 0, max(height)
    answer = 0

    while start <= end:
        total_height = 0
        mid = (start + end) // 2
        for h in height:
            if h > mid:
                total_height += h - mid
        if total_height >= m:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    print(answer)


solution()
