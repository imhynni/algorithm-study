# https://www.acmicpc.net/problem/14891
# 백준 14891 <톱니바퀴>
# Gold 5
from collections import deque
import sys


def solution():
    gear = [deque([0])]
    for _ in range(4):
        gear.append(deque(list(sys.stdin.readline().strip())))
    k = int(sys.stdin.readline())
    for _ in range(k):
        n, d = map(int, sys.stdin.readline().split())
        direction = [0, 0, 0, 0, 0]
        direction[n] = d
        for i in range(n, 1, -1):
            if gear[i - 1][2] == gear[i][6]:
                break
            d = -d
            direction[i - 1] = d
        d = direction[n]
        for j in range(n, 4):
            if gear[j + 1][6] == gear[j][2]:
                break
            d = -d
            direction[j + 1] = d
        for k in range(1, 5):
            gear[k].rotate(direction[k])
    score = 0
    for g in range(4):
        if gear[g + 1][0] == '1':
            score += pow(2, g)
    print(score)


solution()
