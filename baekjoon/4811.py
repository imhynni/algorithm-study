# https://www.acmicpc.net/problem/4811
# 백준 4811 <알약>
# Gold 5
import sys


def solution():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for w in range(1, n + 1):
            dp[w][0] = 1
        for w in range(1, n + 1):
            for h in range(1, n + 1):
                if h > w:
                    break
                dp[w][h] = dp[w - 1][h] + dp[w][h - 1]
        print(dp[n][n])


solution()
