# https://www.acmicpc.net/problem/15686
# 백준 15686 <치킨 배달>
# Gold 5
from itertools import combinations
import sys


def calc_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def solution():
    n, m = map(int, sys.stdin.readline().split())
    town = []
    home = []
    chicken = []
    home_chicken = dict()  # 집 - 치킨집 거리 모두 저장 ((r1, c1), (r2, c2)) : d
    chicken_comb = []
    min_chicken_distance = sys.maxsize

    for _ in range(n):
        town.append(list(sys.stdin.readline().rstrip().split()))

    for i in range(n):
        for j in range(n):
            if town[i][j] == '1':
                home.append((i + 1, j + 1))
            elif town[i][j] == '2':
                chicken.append((i + 1, j + 1))

    for (r1, c1) in home:
        for (r2, c2) in chicken:
            home_chicken[(r1, c1), (r2, c2)] = calc_distance(r1, c1, r2, c2)

    chicken_comb = combinations(chicken, m)

    for comb in chicken_comb:
        town_chicken_distance = 0
        for (r1, c1) in home:
            chicken_distance = sys.maxsize
            for (r2, c2) in comb:
                chicken_distance = min(
                    chicken_distance, home_chicken[(r1, c1), (r2, c2)])
            town_chicken_distance += chicken_distance
        min_chicken_distance = min(min_chicken_distance, town_chicken_distance)

    print(min_chicken_distance)


solution()
