# https://www.acmicpc.net/problem/10282
# 백준 10282 <해킹>
# Gold 4
import sys
from collections import defaultdict
import heapq


def solution():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, d, c = map(int, input().split())
        computers = defaultdict(list)
        distance = [sys.maxsize] * (n + 1)

        for _ in range(d):
            a, b, s = map(int, input().split())
            computers[b].append((a, s))

        count = set()
        q = []
        heapq.heappush(q, (0, c))
        while q:
            dist, now = heapq.heappop(q)
            count.add(now)
            if distance[now] < dist:
                continue
            for com, t in computers[now]:
                cost = dist + t
                if cost < distance[com]:
                    distance[com] = cost
                    heapq.heappush(q, (cost, com))

        time = 0
        for d in distance:
            if d != sys.maxsize:
                time = max(time, d)

        print(len(count), time)


solution()
