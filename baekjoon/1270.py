# https://www.acmicpc.net/problem/1270
# 백준 1270 <전쟁 - 땅따먹기>
# Silver 3

import sys
from collections import defaultdict


def solution():
    n = int(sys.stdin.readline())
    for _ in range(n):
        t, *nums = map(int, sys.stdin.readline().split())
        count = defaultdict(int)
        result = "SYJKGW"
        for num in nums:
            count[num] += 1
        for key, value in count.items():
            if value > t/2:
                result = key
                break
        print(result)


solution()
