# https://www.acmicpc.net/problem/1431
# 백준 1431 <시리얼 번호>
# Silver 3

import sys
import re


def solution():
    n = int(sys.stdin.readline())
    serial = []
    for _ in range(n):
        serial.append(sys.stdin.readline().strip())
    serial.sort(key=len)
    for m in range(n - 1, 0, -1):  # n-1 .. 1
        for i in range(m):
            if len(serial[i]) == len(serial[i + 1]):
                l_num = list(map(int, re.findall(r'\d', serial[i])))
                r_num = list(map(int, re.findall(r'\d', serial[i + 1])))
                if sum(l_num) == sum(r_num):
                    serial[i:i+2] = sorted(serial[i:i+2])
                elif sum(l_num) > sum(r_num):
                    serial[i], serial[i + 1] = serial[i + 1], serial[i]
    for s in serial:
        print(s)


solution()
