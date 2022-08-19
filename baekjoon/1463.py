# https://www.acmicpc.net/problem/1463
# 백준 1463 <1로 만들기>
# Silver 3

import sys


def solution():
    n = int(sys.stdin.readline())
    count = [0] * (n + 1)

    for i in range(2, n + 1):
        temp = []
        if i % 3 == 0:
            temp.append(count[i // 3])
        if i % 2 == 0:
            temp.append(count[i // 2])
        temp.append(count[i - 1])
        count[i] = min(temp) + 1
    print(count[n])


solution()
