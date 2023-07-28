# https://www.acmicpc.net/problem/2628
# 백준 2628 <종이자르기>
# Silver 5

import sys


def solution():
    c, r = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    rows = [0, r]
    cols = [0, c]

    for _ in range(n):
        d, num = map(int, sys.stdin.readline().split())
        if d == 0:
            rows.append(num)
        else:
            cols.append(num)

    rows.sort(reverse=True)
    cols.sort(reverse=True)

    max_row = 0
    max_col = 0

    for i in range(len(rows) - 1):
        max_row = max(max_row, rows[i] - rows[i + 1])

    for j in range(len(cols) - 1):
        max_col = max(max_col, cols[j] - cols[j + 1])

    print(max_row * max_col)


solution()
