# https://www.acmicpc.net/problem/14502
# 백준 14502 <연구소>
# Gold 4
import sys
from itertools import combinations
from collections import deque


def solution():
    input = sys.stdin.readline
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    EMPTY = 0
    WALL = 1
    VIRUS = 2

    n, m = map(int, input().split())
    area = []
    empty = []
    virus = []

    for _ in range(n):
        area.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if area[i][j] == EMPTY:
                empty.append((i, j))
            elif area[i][j] == VIRUS:
                virus.append((i, j))

    walls_combi = list(combinations(empty, 3))

    answer = 0
    for combi in walls_combi:
        safety = len(empty) - 3
        new_area = [item[:] for item in area]
        for wall_x, wall_y in combi:
            new_area[wall_x][wall_y] = WALL
        for virus_x, virus_y in virus:
            q = deque([(virus_x, virus_y)])
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if new_area[nx][ny] == EMPTY:
                            new_area[nx][ny] = VIRUS
                            safety -= 1
                            q.append((nx, ny))
        answer = max(answer, safety)

    print(answer)


solution()
