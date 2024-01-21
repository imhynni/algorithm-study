import sys


def solution():
    n = int(sys.stdin.readline())
    stairs = [0] * 301
    for i in range(n):
        stairs[i + 1] = int(sys.stdin.readline())

    dp = [0] * 301
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for j in range(3, n + 1):
        dp[j] = max(stairs[j] + stairs[j - 1] + dp[j - 3],
                    stairs[j] + dp[j - 2])

    print(dp[n])


solution()