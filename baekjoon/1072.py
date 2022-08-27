# https://www.acmicpc.net/problem/1072
# 백준 1072 <게임>
# Silver 3

import sys


def solution():
    x, y = map(int, sys.stdin.readline().split())
    z = y * 100 // x
    start = 1
    end = x
    answer = float('inf')
    if z >= 99:
        print(-1)
    else:
        while start <= end:
            mid = (end + start) // 2
            new_z = (y + mid) * 100 // (x + mid)
            if new_z > z:
                answer = min(mid, answer)
                end = mid - 1
            else:
                start = mid + 1
        print(answer)


solution()
