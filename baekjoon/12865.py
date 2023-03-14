import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    item = [0]
    for _ in range(n):
        w, v = map(int, sys.stdin.readline().split())
        item.append((w, v))
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):  # 최대 무게
        for j in range(1, n + 1):  # 물건 번호
            weight = item[j][0]
            value = item[j][1]
            if weight > i:
                dp[i][j] = dp[i][j - 1]
                continue
            dp[i][j] = max(dp[i][j - 1], value + dp[i - weight][j - 1])
    print(dp[k][n])


solution()
