# https://www.acmicpc.net/problem/16234
# 백준 16234 <인구 이동>
# Gold 5
import sys
from collections import deque


def solution():
    n, l, r = map(int, sys.stdin.readline().split())
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    area = []
    for _ in range(n):
        area.append(list(map(int, sys.stdin.readline().split())))

    days = 0
    while True:
        flag = False
        visited = set()
        for i in range(n):
            for j in range(n):
                if (i, j) not in visited:
                    visited.add((i, j))
                    union = [(i, j)]
                    count = area[i][j]  # 연합 총 인구수
                    q = deque([(i, j)])
                    while q:
                        x, y = q.pop()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                                if l <= abs(area[x][y] - area[nx][ny]) <= r:
                                    count += area[nx][ny]
                                    visited.add((nx, ny))
                                    union.append((nx, ny))
                                    q.append((nx, ny))
                    if len(union) > 1:
                        flag = True
                        for ux, uy in union:
                            area[ux][uy] = count // len(union)
        if not flag:
            break
        days += 1

    print(days)


solution()
