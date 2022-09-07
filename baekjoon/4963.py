# https://www.acmicpc.net/problem/4963
# 백준 4963 <섬의 개수>
# Silver 2
from collections import deque
import sys


def solution():
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0),
                 (1, 1), (-1, -1), (1, -1), (-1, 1)]
    while True:
        w, h = map(int, sys.stdin.readline().split())
        visited = [[False] * w for _ in range(h)]
        count = 0
        if w == 0 and h == 0:
            break
        island_map = [[] * w for _ in range(h)]
        for i in range(h):
            island_map[i] = list(map(int, sys.stdin.readline().split()))
        for i in range(h):
            for j in range(w):
                if not visited[i][j] and island_map[i][j] == 1:
                    visited[i][j] = True
                    count += 1
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        for d in direction:
                            next_i, next_j = x + d[0], y + d[1]
                            if 0 <= next_i < h and 0 <= next_j < w and island_map[next_i][next_j] == 1 and not visited[next_i][next_j]:
                                visited[next_i][next_j] = True
                                q.append((next_i, next_j))
        print(count)

# visited 사용하지 않은 코드


def solution2():
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0),
                 (1, 1), (-1, -1), (1, -1), (-1, 1)]
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == 0 and h == 0:
            break
        land = []
        count = 0
        for _ in range(h):
            land.append(list(sys.stdin.readline().rstrip().split()))
        for i in range(h):
            for j in range(w):
                if land[i][j] == '1':
                    land[i][j] = '0'
                    count += 1
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        for d in direction:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == '1':
                                land[nx][ny] = '0'
                                q.append((nx, ny))
        print(count)


# solution()
solution2()
