# https://www.acmicpc.net/problem/18126
# 백준 18126 <너구리 구구>
# Silver 2

import sys
from collections import defaultdict, deque


def solution():
    n = int(sys.stdin.readline())
    room = defaultdict(list)
    for i in range(n - 1):
        a, b, c = map(int, sys.stdin.readline().split())
        room[a].append((b, c))
        room[b].append((a, c))
    distance = [0] * (n + 1)
    q = deque()
    q.append(1)
    while q:
        curr = q.popleft()
        for adj in room[curr]:
            if distance[adj[0]] > 0:
                continue
            distance[adj[0]] = distance[curr] + adj[1]
            q.append(adj[0])
    print(max(distance))


solution()
