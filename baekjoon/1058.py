# https://www.acmicpc.net/problem/1058
# 백준 1058 <친구>
# Silver 2
import sys


def solution():
    n = int(sys.stdin.readline())
    friend = []
    dist = [[sys.maxsize] * n for _ in range(n)]
    f_max = 0

    for _ in range(n):
        friend.append(list(sys.stdin.readline().rstrip()))
    for i in range(n):
        for j in range(n):
            if (friend[i][j] == 'Y'):
                dist[i][j] = 1
    for k in range(n):
        dist[k][k] = 0
        for i in range(n):
            count = 0
            for j in range(n):
                if i == j:
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                if dist[i][j] == 1 or dist[i][j] == 2:
                    count += 1
            f_max = max(f_max, count)
    print(f_max)


solution()
