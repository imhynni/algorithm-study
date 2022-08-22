# https://www.acmicpc.net/problem/1431
# 백준 1431 <시리얼 번호>
# Silver 3

import sys
import re


def solution():
    n = int(sys.stdin.readline())
    serial = []
    s_sum = {}

    for _ in range(n):
        serial.append(sys.stdin.readline().rstrip())
    for s in serial:
        nums = list(map(int, re.findall('\d', s)))  # 숫자만 추출
        s_sum[s] = sum(nums)
    serial.sort(key=lambda x: (len(x), s_sum[x], x))

    for s in serial:
        print(s)


solution()
