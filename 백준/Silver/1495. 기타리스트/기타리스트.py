import sys
from collections import defaultdict


def solution():
    n, s, m = map(int, sys.stdin.readline().split())
    volumes = list(map(int, sys.stdin.readline().split()))
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][s] = True

    for i in range(1, n + 1):
        for j in range(m + 1):
            if dp[i - 1][j]:
                if j - volumes[i - 1] >= 0:
                    dp[i][j - volumes[i - 1]] = True
                if j + volumes[i - 1] <= m:
                    dp[i][j + volumes[i - 1]] = True

    answer = -1
    if True in dp[n]:
        for k in range(m, -1, -1):
            if dp[n][k]:
                answer = k
                break

    print(answer)


solution()