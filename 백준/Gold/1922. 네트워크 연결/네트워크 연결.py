import sys


def find_set(parents, n):
    if parents[n] != n:
        parents[n] = find_set(parents, parents[n])
    return parents[n]


def union(parents, a, b):
    parent_a = find_set(parents, a)
    parent_b = find_set(parents, b)
    if parent_a == parent_b:
        return False
    if parent_a < parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b
    return True


def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(n + 1)]
    answer = 0
    count = 0
    for u, v, weight in edges:
        if union(parents, u, v):
            answer += weight
            count += 1
        if count == n - 1:
            break

    print(answer)


solution()
