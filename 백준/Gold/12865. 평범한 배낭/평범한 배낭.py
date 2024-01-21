import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    items = [(0, 0)]
    for _ in range(n):
        weight, value = map(int, sys.stdin.readline().split())
        items.append((weight, value))  # 무게, 가치
    dp = [[0] * (k + 1) for _ in range(n + 1)]  # i: 물건, j: 무게
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if items[i][0] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j],
                               items[i][1] + dp[i - 1][j - items[i][0]])

    print(dp[n][k])


solution()