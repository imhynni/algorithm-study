import sys


def solution():
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    dp = [1] * n
    answer = 1

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                answer = max(answer, dp[i])

    print(answer)


solution()