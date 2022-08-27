# https://www.acmicpc.net/problem/2512
# 백준 2512 <예산>
# Silver 3

import sys


def solution():
    n = int(sys.stdin.readline())
    req = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    start, end = 1, max(req)
    answer = 0

    if sum(req) <= m:
        print(max(req))
    else:
        while start <= end:
            budget = 0
            mid = (end + start) // 2
            for r in req:
                if r > mid:
                    budget += mid
                else:
                    budget += r
            if budget <= m:
                answer = mid
                start = mid + 1
            else:
                end = mid - 1
        print(answer)


solution()
