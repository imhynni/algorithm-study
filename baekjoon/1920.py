# https://www.acmicpc.net/problem/1920
# 백준 1920 <수 찾기>
# Silver 4

import sys


def solution():
    sys.stdin.readline()
    a = set(map(int, sys.stdin.readline().split()))
    sys.stdin.readline()
    nums = list(map(int, sys.stdin.readline().split()))

    for num in nums:
        print(1) if num in a else print(0)


solution()
