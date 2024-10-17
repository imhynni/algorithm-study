import sys
from collections import defaultdict
import heapq


def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))  # 비용, 노드
        if a == b:
            continue
        graph[b].append((c, a))
    visited = set()
    queue = []
    heapq.heappush(queue, (0, next(iter(graph))))
    answer = 0
    while queue:
        cost, node = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        answer += cost
        for adj_cost, adj_node in graph[node]:
            if adj_node not in visited:
                heapq.heappush(queue, (adj_cost, adj_node))
    print(answer)


solution()
