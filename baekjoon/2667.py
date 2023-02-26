# https://www.acmicpc.net/problem/2667
# 백준 2667 <단지번호붙이기>
# Silver 1
from collections import deque
import sys


def solution():
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    n = int(sys.stdin.readline())
    apt_complex = []
    complex_cnt = 0
    house_cnt = []
    for i in range(n):
        apt_complex.append(list(sys.stdin.readline().rstrip()))
    for i in range(n):
        for j in range(n):
            if apt_complex[i][j] == '1':
                apt_complex[i][j] = '0'
                complex_cnt += 1
                house_cnt.append(1)
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for d in direction:
                        next_i, next_j = x + d[0], y + d[1]
                        if 0 <= next_i < n and 0 <= next_j < n and apt_complex[next_i][next_j] == '1':
                            apt_complex[next_i][next_j] = '0'
                            house_cnt[complex_cnt - 1] += 1
                            q.append((next_i, next_j))
    house_cnt = sorted(house_cnt)
    print(complex_cnt)
    for c in house_cnt:
        print(c)


solution()

#
