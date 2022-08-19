# https://www.acmicpc.net/problem/1012
# 백준 1012 <유기농 배추>
# Silver 2
import sys
from collections import deque


def solution():
    t = int(sys.stdin.readline())
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for _ in range(t):
        answer = 0
        col, row, num = map(int, sys.stdin.readline().split())
        field = [[0] * col for _ in range(row)]
        visited = [[False] * col for _ in range(row)]
        for _ in range(num):
            j, i = map(int, sys.stdin.readline().split())
            field[i][j] = 1
        for r in range(row):
            for c in range(col):
                if field[r][c] == 1 and visited[r][c] == False:
                    visited[r][c] = True
                    answer += 1
                    queue = deque([(r, c)])
                    while queue:
                        x, y = queue.popleft()
                        for i in range(len(dx)):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] == False:
                                if field[nx][ny] == 1:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
        print(answer)


solution()
