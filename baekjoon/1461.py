# https://www.acmicpc.net/problem/1461
# 백준 1461 <도서관>
# Gold 5

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    location = list(map(int, sys.stdin.readline().split()))
    left = []
    right = []
    for loc in location:
        if loc < 0:
            left.append(loc)
            continue
        right.append(loc)
    left.sort()
    right.sort(reverse=True)

    answer = 0
    for i in range(0, len(left), m):
        answer += -left[i] * 2
    for i in range(0, len(right), m):
        answer += right[i] * 2
    if not left:
        max_dist = right[0]
    elif not right:
        max_dist = -left[0]
    else:
        max_dist = max(-left[0], right[0])
    answer -= max_dist

    print(answer)


solution()
