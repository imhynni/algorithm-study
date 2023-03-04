# https://www.acmicpc.net/problem/15685
# 백준 15686 <드래곤 커브>
# Gold 4

import sys


def solution():
    direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    n = int(sys.stdin.readline())
    area = [[0] * 101 for _ in range(101)]
    for _ in range(n):
        y, x, d, g = map(int, sys.stdin.readline().split())
        area[x][y] = 1
        dx, dy = direction[d]
        nx, ny = x + dx, y + dy
        area[nx][ny] = 1
        x, y = nx, ny
        curve = [d]
        for i in range(g):
            size = pow(2, i)
            for j in range(size - 1, -1, -1):
                next_d = (curve[j] + 1) % 4
                dx, dy = direction[next_d]
                nx, ny = x + dx, y + dy
                area[nx][ny] = 1
                x, y = nx, ny
                curve.append(next_d)

    answer = 0
    for i in range(100):
        for j in range(100):
            if area[i][j] == 1 and area[i][j + 1] == 1 and area[i + 1][j] == 1 and area[i + 1][j + 1] == 1:
                answer += 1
    print(answer)


solution()
