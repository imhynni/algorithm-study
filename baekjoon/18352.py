# https://www.acmicpc.net/problem/18352
# 백준 18352 <특정 거리의 도시 찾기>
# Silver 2

import sys
import heapq
from collections import defaultdict


def solution():
    input = sys.stdin.readline
    n, m, k, x = map(int, input().split())
    graph = defaultdict(list)
    distance = [sys.maxsize] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    distance[x] = 0
    q = []
    heapq.heappush(q, (0, x))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for g in graph[now]:
            cost = dist + 1
            if cost < distance[g]:
                distance[g] = cost
                heapq.heappush(q, (cost, g))

    answer = []
    for i in range(1, n + 1):
        if distance[i] == k:
            heapq.heappush(answer, i)
    if answer:
        while answer:
            print(heapq.heappop(answer))
    else:
        print(-1)


solution()
