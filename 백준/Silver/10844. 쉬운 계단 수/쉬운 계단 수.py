import sys


def solution():
    n = int(sys.stdin.readline())
    dp = [[0] * 10 for _ in range(n + 1)]

    for k in range(1, 10):
        dp[1][k] = 1

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][1]
        dp[i][9] = dp[i - 1][8]
        for j in range(1, 9):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

    print(sum(dp[n]) % 1_000_000_000)


solution()