import sys
import math


def solution():
    n, m = map(int, sys.stdin.readline().split())
    jewels = []
    max_cnt = 0
    for _ in range(m):
        cnt = int(sys.stdin.readline())
        jewels.append(cnt)
        max_cnt = max(max_cnt, cnt)

    answer = max_cnt
    start, end = 1, max_cnt
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for jewel in jewels:
            count += math.ceil(jewel / mid)
        if count <= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    print(answer)


solution()