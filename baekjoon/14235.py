# https://www.acmicpc.net/problem/14235
# 백준 14235 <크리스마스 선물>
# Silver 3
import sys
import heapq


def solution():
    n = int(sys.stdin.readline())
    presents = []

    for _ in range(n):
        a, *present = map(int, sys.stdin.readline().split())
        if a == 0:
            if presents:
                print(heapq.heappop(presents)[1])
            else:
                print(-1)
        else:
            for p in present:
                heapq.heappush(presents, (-p, p))


solution()
