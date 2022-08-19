# https://www.acmicpc.net/problem/2606
# 백준 2606 <바이러스>
# Siver 3

import sys
from collections import deque


def solution():
    n = int(sys.stdin.readline())
    num_edges = int(sys.stdin.readline())
    matrix = [[0] * n for _ in range(n)]
    visited = [False] * n
    for _ in range(num_edges):
        i, j = map(int, sys.stdin.readline().split())
        matrix[i - 1][j - 1] = 1
        matrix[j - 1][i - 1] = 1
    queue = deque([0])
    while queue:
        computer = queue.popleft()
        if visited[computer] == False:
            visited[computer] = True
            for i in range(n):
                if matrix[computer][i] == 1 and visited[i] == False:
                    queue.append(i)
    print(visited.count(1) - 1)


solution()
