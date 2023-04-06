# https://www.acmicpc.net/problem/1967
# 백준 1967 <트리의 지름>
# Gold 4

import sys
from collections import defaultdict, deque


def solution():
    n = int(sys.stdin.readline())
    edge = defaultdict(list)
    for i in range(n - 1):
        a, b, c = map(int, sys.stdin.readline().split())
        edge[a].append((b, c))
        edge[b].append((a, c))
    q = deque()
    visited = [False] * (n + 1)
    q.append((1, 0))
    visited[1] = True
    max_node = 0
    max_dist = 0
    while q:
        curr, dist = q.popleft()
        for next_node, next_dist in edge[curr]:
            if visited[next_node]:
                continue
            cost = dist + next_dist
            q.append((next_node, cost))
            visited[next_node] = True
            if max_dist < cost:
                max_node = next_node
                max_dist = cost

    q = deque()
    visited = [False] * (n + 1)
    q.append((max_node, 0))
    visited[max_node] = True
    max_dist = 0
    while q:
        curr, dist = q.popleft()
        for next_node, next_dist in edge[curr]:
            if visited[next_node]:
                continue
            cost = dist + next_dist
            q.append((next_node, cost))
            visited[next_node] = True
            if max_dist < cost:
                max_dist = cost
    print(max_dist)


solution()
