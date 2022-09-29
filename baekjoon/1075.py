# https://www.acmicpc.net/problem/1057
# 백준 <토너먼트>
# Silver 3
import sys
import math


def solution():
    _, kjm, lhs = map(int, sys.stdin.readline().split())

    rounds = 1
    while True:
        if abs(kjm - lhs) == 1 and max(kjm, lhs) % 2 == 0:
            break
        kjm = math.ceil(kjm / 2)
        lhs = math.ceil(lhs / 2)
        rounds += 1

    print(rounds)


solution()
