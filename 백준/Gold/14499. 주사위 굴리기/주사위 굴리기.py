import sys


def roll_dice(direction, dice):
    if direction == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif direction == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif direction == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif direction == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    else:
        return


def solution():
    directions = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
    n, m, x, y, _ = map(int, sys.stdin.readline().split())
    area = []
    for _ in range(n):
        area.append(list(map(int, sys.stdin.readline().split())))
    movement = list(map(int, sys.stdin.readline().split()))
    dice = [0, 0, 0, 0, 0, 0]
    for command in movement:
        dx, dy = directions[command]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        roll_dice(command, dice)
        x, y = nx, ny
        if area[x][y] == 0:
            area[x][y] = dice[5]
        else:
            dice[5] = area[x][y]
            area[x][y] = 0
        print(dice[0])


solution()