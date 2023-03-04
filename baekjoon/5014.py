# https://www.acmicpc.net/problem/5014
# 백준 5014 <스타트링크>
# Silver 1

import sys
from collections import deque


def solution():
    f, s, g, u, d = map(int, sys.stdin.readline().split())
    visited = [False] * (f + 1)
    d = -d
    q = deque()
    q.append(s)
    cnt = 0
    answer = 'use the stairs'
    finish = False
    while not finish and q:
        size = len(q)
        for _ in range(size):
            curr = q.popleft()
            if curr == g:
                answer = cnt
                finish = True
                break
            for i in (u, d):
                next_floor = curr + i
                if next_floor < 1 or next_floor > f or visited[next_floor]:
                    continue
                q.append(next_floor)
                visited[next_floor] = True
        cnt += 1

    print(answer)


solution()
