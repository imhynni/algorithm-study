# https://www.acmicpc.net/problem/1260
# 백준 1260 <DFS와 BFS>
# Silver 2

from collections import defaultdict
import sys


def dfs(graph, start):
    stack = [start]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += sorted(list(graph[node] - set(visited)), reverse=True)
    return visited


def bfs(graph, start):
    queue = [start]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += sorted(list(graph[node] - set(visited)))
    return visited


def solution():
    _, M, V = map(int, sys.stdin.readline().split())
    graph = defaultdict(set)

    for _ in range(M):
        n1, n2 = map(int, sys.stdin.readline().split())
        graph[n1].add(n2)
        graph[n2].add(n1)

    dfs_res = dfs(graph, V)
    bfs_res = bfs(graph, V)

    print(*dfs_res)
    print(*bfs_res)


solution()
