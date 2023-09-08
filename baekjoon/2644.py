# https://www.acmicpc.net/problem/2644
# 백준 2644 <촌수계산>
# Silver 2
import sys
from collections import defaultdict, deque


def solution():
    input = sys.stdin.readline
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    adj = defaultdict(list)
    for i in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    visited = [False] * (n + 1)
    q = deque([a])
    visited[a] = True
    count = 0
    answer = -1
    finish = False
    while q:
        size = len(q)
        for _ in range(size):
            curr = q.popleft()
            if curr == b:
                answer = count
                finish = True
                break
            for node in adj[curr]:
                if visited[node]:
                    continue
                q.append(node)
                visited[node] = True
        if finish:
            break
        count += 1
    print(answer)


solution()
