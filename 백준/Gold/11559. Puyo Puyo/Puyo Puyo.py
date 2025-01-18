import sys
from collections import deque

N = 12
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
field = []


def pop_puyo():
    visited = [[False] * (N // 2) for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N // 2):
            if field[i][j] == '.':
                continue
            q = deque()
            q.append((i, j))
            puyo = [(i, j)]
            visited[i][j] = True
            count = 1
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= (N // 2):
                        continue
                    if visited[nx][ny]:
                        continue
                    if field[nx][ny] == field[x][y]:
                        puyo.append((nx, ny))
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        count += 1
            if count > 3:
                flag = True
                for px, py in puyo:
                    field[px][py] = '.'
    return flag


def down_puyo():
    for j in range(N // 2):
        blank_x, blank_y = -2, -2
        for i in range(N - 1, -1, -1):
            if blank_x == -2 and field[i][j] == '.':
                blank_x, blank_y = i, j
                continue
            if blank_x != -2 and field[i][j] != '.':
                field[blank_x][blank_y] = field[i][j]
                field[i][j] = '.'
                blank_x -= 1


def solution():
    for _ in range(N):
        field.append(list(sys.stdin.readline().strip()))
    answer = 0
    while True:
        if not pop_puyo():
            break
        answer += 1
        down_puyo()
    print(answer)


solution()
