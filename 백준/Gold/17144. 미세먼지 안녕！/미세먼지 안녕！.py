import sys
from collections import defaultdict


def solution():
    directions_top = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    directions_bottom = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    input = sys.stdin.readline
    r, c, t = map(int, input().split())
    area = []
    purifiers = []
    for _ in range(r):
        area.append(list(map(int, input().split())))

    total_dust = 0
    for i in range(r):
        for j in range(c):
            if area[i][j] == -1:
                purifiers.append(i)
            elif area[i][j] > 0:
                total_dust += area[i][j]

    for _ in range(t):
        # 1. 미세먼지 확산
        diffusion = defaultdict(int)
        for x in range(r):
            for y in range(c):
                if area[x][y] > 0:
                    dust = area[x][y] // 5
                    for dx, dy in directions_top:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= r or ny < 0 or ny >= c or area[nx][ny] == -1:
                            continue
                        diffusion[(nx, ny)] += dust
                        area[x][y] -= dust
        for key, value in diffusion.items():
            a, b = key
            area[a][b] += value

        # 2. 공청기 작동
        for idx, purifier in enumerate(purifiers):
            x = purifier
            y = 1
            directions = directions_top if idx == 0 else directions_bottom
            prev_dust = area[x][y]
            area[x][y] = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                while nx >= 0 and nx < r and ny >= 0 and ny < c:
                    if ny == 0 and nx == purifier:
                        total_dust -= prev_dust
                        break
                    area[nx][ny], prev_dust = prev_dust, area[nx][ny]
                    x, y = nx, ny
                    nx, ny = x + dx, y + dy

    print(total_dust)


solution()
