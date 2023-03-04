# https://www.acmicpc.net/problem/17086
# 백준 17086 <아기 상어 2>
# Silver 2

import sys
from collections import deque

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]
n, m = map(int, sys.stdin.readline().split())
area = []
visited = [[False] * m for _ in range(n)]


def solution():
    for i in range(n):
        area.append(list(map(int, sys.stdin.readline().split())))
    answer = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] or area[i][j] == 1:
                continue
            answer = max(answer, bfs(i, j))
    print(answer)


def bfs(i, j):
    count = 0
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        size = len(q)
        count += 1
        for _ in range(size):
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if area[nx][ny] == 1:
                    return count
                if visited[nx][ny]:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = True


solution()
