import sys


def solution():
    n, m, r = map(int, sys.stdin.readline().split())
    items = list(map(int, sys.stdin.readline().split()))
    distance = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for _ in range(r):
        a, b, l = map(int, sys.stdin.readline().split())
        distance[a][b] = l
        distance[b][a] = l

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    distance[i][j] = 0
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])

    max_item = 0
    for node in range(1, n + 1):
        count = 0
        for i, d in enumerate(distance[node]):
            if d <= m:
                count += items[i - 1]
        max_item = max(max_item, count)

    print(max_item)


solution()
