import sys
from collections import defaultdict
from heapq import heappop, heappush

edge = defaultdict(list)

def dijkstra(n, start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        dist, curr = heappop(q)
        if dist > distance[curr]:
            continue
        for new_dist, new_node in edge[curr]:
            cost = dist + new_dist
            if cost < distance[new_node]:
                distance[new_node] = cost
                heappush(q, (cost, new_node))
    return distance


def solution():
    input = sys.stdin.readline
    n, e = map(int, input().split())
    for _ in range(e):
        a, b, c = map(int, input().split())
        edge[a].append((c, b)) # 거리, 정점
        edge[b].append((c, a))
    x, y = map(int, input().split())

    start_s = dijkstra(n, 1)
    start_x = dijkstra(n, x)
    start_y = dijkstra(n, y)

    # 1 -> x -> y -> n
    x_to_y = start_s[x] + start_x[y] + start_y[n]
    # 1 -> y -> x -> n
    y_to_x = start_s[y] + start_y[x] + start_x[n]

    answer = min(x_to_y, y_to_x)
    if answer == float('inf'):
        answer = -1
    print(answer)


solution()