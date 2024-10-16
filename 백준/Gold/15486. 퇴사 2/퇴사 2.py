import sys


def solution():
    input = sys.stdin.readline
    n = int(input())
    counsels = []
    for _ in range(n):
        t, p = map(int, input().split())
        counsels.append((t, p))
    dp = [0] * 1_500_001
    for i in range(n - 1, -1, -1):
        time, price = counsels[i]
        if i + time > n:
            dp[i] = dp[i + 1]
            continue
        dp[i] = max(dp[i + time] + price, dp[i + 1])

    print(dp[0])


solution()
