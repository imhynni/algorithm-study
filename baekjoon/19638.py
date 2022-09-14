# https://www.acmicpc.net/problem/19638
# 백준 19638 <센티와 마법의 뿅망치>
# Silver 1

import heapq
import sys


def solution():
    n, h, t = map(int, sys.stdin.readline().split())
    giants = []
    count = 0
    heapq.heapify(giants)

    for _ in range(n):
        height = int(sys.stdin.readline())
        heapq.heappush(giants, -height)

    for _ in range(t):
        if -giants[0] < h or -giants[0] == 1:
            break
        else:
            count += 1
            g_height = heapq.heappop(giants)
            heapq.heappush(giants, -(-g_height // 2))
    g = -giants[0]
    if g < h:
        print('YES')
        print(count)
    else:
        print('NO')
        print(g)


solution()
