# https://www.acmicpc.net/problem/17142
# 백준 17142 <연구소 3>
# Gold 3
import sys
from itertools import combinations
from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    n, m = map(int, sys.stdin.readline().split())
    area = []
    for _ in range(n):
        area.append(list(map(int, sys.stdin.readline().split())))
    count = 0
    virus = []
    for i in range(n):
        for j in range(n):
            if area[i][j] == 0:
                count += 1
            elif area[i][j] == 2:
                virus.append((i, j))
    answer = sys.maxsize
    temp_area = [a[:] for a in area]
    if count == 0:
        answer = 0
    else:
        for comb in combinations(range(len(virus)), m):
            temp_count = count
            q = deque()
            for c in comb:
                x, y = virus[c]
                area[x][y] = 9  # 활성 바이러스 방문 표시
                q.append((x, y))
            time = 0
            while q:
                size = len(q)
                for _ in range(size):
                    x, y = q.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if area[nx][ny] == 1 or area[nx][ny] == 9:
                            continue
                        if area[nx][ny] == 0:
                            count -= 1
                        area[nx][ny] = 9
                        q.append((nx, ny))
                time += 1
                if count == 0:
                    break
            if count == 0:
                answer = min(answer, time)
            count = temp_count
            area = [a[:] for a in temp_area]

    if answer == sys.maxsize:
        answer = -1

    print(answer)


solution()
