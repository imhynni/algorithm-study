# https://www.acmicpc.net/problem/1015
# 백준 1015 <수열 정렬>
# Silver 4


import sys


def solution():
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    P = [0] * n
    B = sorted(A)
    for i in range(n):
        P[i] = B.index(A[i])
        B[P[i]] = -1
    print(' '.join(map(str, P)))


solution()
