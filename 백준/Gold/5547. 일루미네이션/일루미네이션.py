import sys
from collections import deque


def solution():
    directions = [[(-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)],
                  [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]]
    w, h = map(int, sys.stdin.readline().split())
    area = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
    for i in range(1, h + 1):
        area[i][1: w + 1] = map(int, input().split())
    visited = [[False for _ in range(w + 2)] for _ in range(h + 2)]
    q = deque([(0, 0)])
    visited[0][0] = True
    answer = 0
    while q:
        x, y = q.popleft()
        for dx, dy in directions[x % 2]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if area[nx][ny] == 1:
                    answer += 1
                    continue
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    print(answer)


solution()