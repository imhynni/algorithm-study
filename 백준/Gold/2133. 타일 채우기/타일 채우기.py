import sys


def solution():
    n = int(sys.stdin.readline())
    dp = [0] * 31
    dp[2] = 3
    dp[4] = 11
    for i in range(6, n + 1, 2):
        for j in range(i - 4, 1, -2):
            dp[i] += dp[j] * 2
        dp[i] += dp[i - 2] * 3 + 2

    print(dp[n])


solution()