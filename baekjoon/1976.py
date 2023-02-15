# https://www.acmicpc.net/problem/1976
# 백준 1976 <여행 가자>
# Gold 4

import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    n = int(input())
    _ = int(input())
    matrix = []
    visited = [False] * n
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    plan = list(map(int, input().split()))

    q = deque()
    q.append(plan[0] - 1)
    visited[plan[0] - 1] = True
    while q:
        city = q.popleft()
        for i in range(n):
            if matrix[city][i] and not visited[i]:
                q.append(i)
                visited[i] = True

    answer = "YES"
    for c in plan:
        if not visited[c - 1]:
            answer = "NO"
    print(answer)


solution()
