# https://www.acmicpc.net/problem/2470
# 백준 2470 <두 용액>
# Gold 5
import sys


def solution():
    n = int(sys.stdin.readline())
    sol = list(map(int, sys.stdin.readline().split()))
    sol.sort()

    answer = sys.maxsize
    start, end = 0, n - 1
    while start < end:
        sol_mix = sol[start] + sol[end]
        if abs(sol_mix) < answer:
            answer = abs(sol_mix)
            s, e = start, end
        if sol_mix < 0:
            start += 1
        else:
            end -= 1

    print(sol[s], sol[e])


solution()
