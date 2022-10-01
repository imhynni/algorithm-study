# https://www.acmicpc.net/problem/1238
# 백준 1238 <파티>
# Gold 3
from collections import defaultdict
import heapq
import sys


def dijkstra(graph, start, distance):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for k, v in graph[now].items():
            cost = dist + v
            if cost < distance[k]:
                distance[k] = cost
                heapq.heappush(q, (cost, k))


def solution():
    input = sys.stdin.readline
    n, m, x = map(int, input().split())
    graph = defaultdict(dict)
    come_and_go = [0] * (n + 1)

    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a][b] = t

    for i in range(1, n + 1):
        distance = {node: sys.maxsize for node in range(1, n + 1)}
        dijkstra(graph, i, distance)
        if i != x:
            come_and_go[i] += distance[x]  # 가는 거리
        else:
            for j in range(1, n + 1):
                come_and_go[j] += distance[j]  # 오는 거리

    print(max(come_and_go))


solution()
