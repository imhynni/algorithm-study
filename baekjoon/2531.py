# https://www.acmicpc.net/problem/2531
# 백준 2531 <회전 초밥>
# Silver 1

import sys


def solution():
    n, _, k, c = map(int, sys.stdin.readline().split())
    kind = set()
    chobab = []
    answer = 0
    for _ in range(n):
        chobab.append(int(sys.stdin.readline()))
    chobab *= 2
    for i in range(n):
        kind = set(chobab[i:i + k])
        kind.add(c)
        answer = max(answer, len(kind))
    print(answer)


solution()
