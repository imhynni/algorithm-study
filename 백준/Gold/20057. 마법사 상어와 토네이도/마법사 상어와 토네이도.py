import sys


direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
sand_ratio_0 = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0],
]


def rotate_90(matrix):
    return list(map(list, zip(*matrix)))[::-1]


def solution():
    n = int(sys.stdin.readline())
    area = []
    sand_ratio_90 = rotate_90(sand_ratio_0)
    sand_ratio_180 = rotate_90(sand_ratio_90)
    sand_ratio_270 = rotate_90(sand_ratio_180)
    sand_ratio = [sand_ratio_0, sand_ratio_90,
                  sand_ratio_180, sand_ratio_270]

    for _ in range(n):
        area.append(list(map(int, sys.stdin.readline().split())))

    x, y = n // 2, n // 2
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    d = 0
    answer = 0
    while True:
        dx, dy = direction[d]
        ratio = sand_ratio[d]
        nx, ny = x + dx, y + dy
        if visited[nx][ny]:
            d = d - 1 if d - 1 >= 0 else 3
            continue
        visited[nx][ny] = True
        total_sand = area[nx][ny]
        remain_sand = total_sand
        for i in range(5):
            for j in range(5):
                if ratio[i][j] == 0:
                    continue
                curr_sand = int(total_sand * ratio[i][j])
                if 0 <= nx + i - 2 < n and 0 <= ny + j - 2 < n:
                    area[nx + i - 2][ny + j - 2] += curr_sand
                    remain_sand -= curr_sand
                else:
                    answer += curr_sand
                    remain_sand -= curr_sand
        if 0 <= nx + dx < n and 0 <= ny + dy < n:
            area[nx + dx][ny + dy] += remain_sand
        else:
            answer += remain_sand
        area[nx][ny] = 0
        if nx == 0 and ny == 0:
            break
        x, y = nx, ny
        d = (d + 1) % 4

    print(answer)


solution()