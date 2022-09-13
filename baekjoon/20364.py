# https://www.acmicpc.net/problem/20364
# 백준 20364 <부동산 다툼>
# Silver 2
import sys


def solution():
    _, q = map(int, sys.stdin.readline().split())
    want = []
    visited = set()

    for _ in range(q):
        want.append(int(sys.stdin.readline()))

    for w in want:
        temp = w
        answer = 0
        while True:
            if w == 0:
                break
            if w in visited:
                answer = w
            w = w // 2
        if answer == 0:
            visited.add(temp)
        print(answer)


solution()
