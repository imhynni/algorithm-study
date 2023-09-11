# https://www.acmicpc.net/problem/5427
# 백준 5427 <불>
# Gold 4

import sys
from collections import deque


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        w, h = map(int, input().split())
        area = []
        visited = [[False] * w for _ in range(h)]

        for _ in range(h):
            area.append(list(input().rstrip()))

        fires = []
        for i in range(h):
            for j in range(w):
                if area[i][j] == '@':
                    s_i, s_j = i, j
                if area[i][j] == '*':
                    fires.append((i, j))

        q = deque([(s_i, s_j)])
        visited[s_i][s_j] = True
        time = 0
        finish = False
        while q:
            temp_fires = []
            for x, y in fires:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= h or ny < 0 or ny >= w:
                        continue
                    if area[nx][ny] == '*' or area[nx][ny] == '#':
                        continue
                    area[nx][ny] = '*'
                    temp_fires.append((nx, ny))
            fires = temp_fires
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if x == 0 or x == h - 1 or y == 0 or y == w - 1:
                    finish = True
                    break
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= h or ny < 0 or ny >= w:
                        continue
                    if visited[nx][ny] or area[nx][ny] == '#' or area[nx][ny] == '*':
                        continue
                    q.append((nx, ny))
                    visited[nx][ny] = True
            time += 1
            if finish:
                break
        if finish:
            print(time)
        else:
            print('IMPOSSIBLE')


solution()
