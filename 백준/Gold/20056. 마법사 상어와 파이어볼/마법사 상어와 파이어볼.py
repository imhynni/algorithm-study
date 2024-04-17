import sys
from collections import defaultdict


class Fireball:
    def __init__(self, m, s, d):
        self.mass = m
        self.speed = s
        self.direction = d


def solution():
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]
    n, m, k = map(int, sys.stdin.readline().split())
    area = defaultdict(list)
    for _ in range(m):
        r, c, mass, speed, direction = map(int, sys.stdin.readline().split())
        area[(r - 1, c - 1)].append(Fireball(mass, speed, direction))
    for _ in range(k):
        area_temp = defaultdict(list)
        for key, fireballs in area.items():
            x, y = key
            for fireball in fireballs:
                dx, dy = directions[fireball.direction]
                s = fireball.speed
                nx, ny = (x + dx * s) % n, (y + dy * s) % n
                area_temp[(nx, ny)].append(fireball)
        for key, fireballs in area_temp.items():
            if len(fireballs) < 2:
                continue
            new_mass = sum(fireball.mass for fireball in fireballs) // 5
            new_speed = sum(
                fireball.speed for fireball in fireballs) // len(fireballs)
            flag = fireballs[0].direction % 2
            d = 0
            for fireball in fireballs:
                if fireball.direction % 2 != flag:
                    d = 1
                    break
            area_temp[key] = []
            if new_mass == 0:
                continue
            for i in range(0, 7, 2):
                area_temp[key].append(
                    Fireball(new_mass, new_speed, i + d))
        area = area_temp

    answer = sum(sum(fireball.mass for fireball in fireballs)
                 for fireballs in area.values())
    print(answer)


solution()