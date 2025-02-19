import sys


def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    items = []
    for _ in range(n):
        w, v = map(int, input().split())
        items.append((w, v))
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            weight, value = items[i - 1]
            if weight > j:
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = max(dp[i - 1][j], value + dp[i - 1][j - weight])
    print(dp[n][k])


solution()
