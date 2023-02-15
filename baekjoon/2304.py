# https://www.acmicpc.net/problem/2304
# 백준 2304 <창고 다각형>
# Silver 2

import sys


def solution():
    n = int(sys.stdin.readline())
    heights = []
    for _ in range(n):
        i, h = map(int, sys.stdin.readline().split())
        heights.append((i, h))
    heights = sorted(heights)
    max_idx = heights.index(max(heights, key=lambda x: x[1]))
    answer = heights[max_idx][1]
    curr_max = heights[0]

    # max 이전
    for i in range(1, max_idx + 1):
        l, h = heights[i]
        if h < curr_max[1]:
            continue
        answer += (l - curr_max[0]) * curr_max[1]
        curr_max = (l, h)
    # max 이후
    curr_max = heights[n - 1]
    for j in range(n - 2, max_idx - 1, -1):
        l, h = heights[j]
        if h < curr_max[1]:
            continue
        answer += (curr_max[0] - l) * curr_max[1]
        curr_max = (l, h)

    print(answer)


solution()
