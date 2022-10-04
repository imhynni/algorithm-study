# https://www.acmicpc.net/problem/1138
# 백준 1138 <한 줄로 서기>
# Silver 2
import sys


def solution():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    lines = []
    for i in range(n, 0, -1):
        lines.insert(heights[i - 1], i)
    print(*lines)


solution()
