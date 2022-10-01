# https://www.acmicpc.net/problem/4485
# 백준 4485 <녹색 옷 입은 애가 젤다지?
# Gold 4
import heapq
import sys


def solution():
    input = sys.stdin.readline
    direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    number = 0

    while True:
        n = int(input())
        if n == 0:
            break
        number += 1
        area = []
        score = [[sys.maxsize] * n for _ in range(n)]

        for _ in range(n):
            area.append(list(map(int, input().split())))

        score[0][0] = area[0][0]
        q = []
        heapq.heappush(q, (score[0][0], (0, 0)))
        while q:
            dist, now = heapq.heappop(q)
            x, y = now[0], now[1]
            if score[x][y] < dist:
                continue
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    cost = dist + area[nx][ny]
                    if cost < score[nx][ny]:
                        score[nx][ny] = cost
                        heapq.heappush(q, (cost, (nx, ny)))

        print(f"Problem {number}: {score[n - 1][n - 1]}")


solution()
