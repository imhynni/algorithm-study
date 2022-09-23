# https://www.acmicpc.net/problem/2573
# 백준 2573 <빙산>
# Gold 4
from collections import deque
import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    iceberg = []
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(n):
        iceberg.append(list(map(int, sys.stdin.readline().split())))

    year = 0

    while True:
        iceberg_temp = [i[:] for i in iceberg]
        year += 1
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if iceberg[i][j] > 0:
                    for d in direction:
                        dx, dy = d[0], d[1]
                        if iceberg[i + dx][j + dy] == 0 and iceberg_temp[i][j] > 0:
                            iceberg_temp[i][j] -= 1

        q = deque()
        visited = [[False] * m for _ in range(n)]
        count = 0

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if iceberg_temp[i][j] > 0 and not visited[i][j]:
                    visited[i][j] = True
                    q.append((i, j))
                    count += 1
                    while q:
                        n_i, n_j = q.popleft()
                        for d in direction:
                            next_i, next_j = n_i + d[0], n_j + d[1]
                            if iceberg_temp[next_i][next_j] > 0 and not visited[next_i][next_j]:
                                q.append((next_i, next_j))
                                visited[next_i][next_j] = True
        if count > 1 or count == 0:
            break

        iceberg = iceberg_temp
    if count == 0:
        year = 0
    print(year)


solution()
