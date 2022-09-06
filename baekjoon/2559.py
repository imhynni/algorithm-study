# https://www.acmicpc.net/problem/2559
# 백준 2559 <수열>
# Silver 3

import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    temp = list(map(int, sys.stdin.readline().split()))
    answer = float('-inf')

    for i in range(1, len(temp)):
        temp[i] += temp[i - 1]
    for j in range(k - 1, len(temp)):
        if j - k >= 0:
            answer = max(answer, temp[j] - temp[j - k])
        else:
            answer = temp[j]
    print(answer)


solution()
