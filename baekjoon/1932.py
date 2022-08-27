# https://www.acmicpc.net/problem/1932
# 백준 1932 <정수 삼각형>
# Silver 2

import sys


def solution():
    n = int(sys.stdin.readline())
    graph = []
    dp = [[0] * (i + 1) for i in range(n)]
    for _ in range(n):
        nums = list(map(int, sys.stdin.readline().split()))
        graph.append(nums)
    dp[0][0] = graph[0][0]
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + graph[i][j]
            elif j > 0 and j < i:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + graph[i][j]
            else:
                dp[i][j] = dp[i - 1][j - 1] + graph[i][j]
    print(max(dp[n - 1]))


solution()
