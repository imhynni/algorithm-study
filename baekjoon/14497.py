# https://www.acmicpc.net/problem/14497
# 백준 14497 <주난의 난>
# Gold 4
import sys
from collections import deque


def solution():
    n, m = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    classroom = []
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(n):
        classroom.append(list(sys.stdin.readline().rstrip()))

    count = 0
    finish = False
    q = deque()
    while not finish:
        count += 1
        q.append((x1, y1))
        friends = []
        visited = [[False] * m for _ in range(n)]
        while q and not finish:
            x, y = q.popleft()
            for d in direction:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < m:
                    if nx == x2 and ny == y2:
                        finish = True
                        break
                    if classroom[nx][ny] == '1':
                        friends.append((nx, ny))
                    elif classroom[nx][ny] == '0' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        for f in friends:
            classroom[f[0]][f[1]] = '0'
    print(count)


solution()
