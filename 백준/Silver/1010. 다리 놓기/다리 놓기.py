import sys
import math


def solution():
    T = int(sys.stdin.readline())
    for _ in range(T):
        k, n = map(int, sys.stdin.readline().split())
        print(math.comb(n, k))


solution()
