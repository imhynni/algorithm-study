import sys
from collections import deque

visited = {(0, 0)}
queue = deque([(0, 0)])


def pour(a, b):
    if (a, b) in visited:
        return
    queue.append((a, b))
    visited.add((a, b))


def solution():
    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    answer = []
    while queue:
        a_water, b_water = queue.popleft()
        c_water = c - (a_water + b_water)

        if a_water == 0:
            answer.append(c_water)

        # A -> B
        pour_amount = min(a_water, b - b_water)
        pour(a_water - pour_amount, b_water + pour_amount)
        # A -> C
        pour_amount = min(a_water, c - c_water)
        pour(a_water - pour_amount, b_water)
        # B -> A
        pour_amount = min(b_water, a - a_water)
        pour(a_water + pour_amount, b_water - pour_amount)
        # B -> C
        pour_amount = min(b_water, c - c_water)
        pour(a_water, b_water - pour_amount)
        # C -> A
        pour_amount = min(c_water, a - a_water)
        pour(a_water + pour_amount, b_water)
        # C -> B
        pour_amount = min(c_water, b - b_water)
        pour(a_water, b_water + pour_amount)

    answer = sorted(answer)
    for i in answer:
        print(i, end=' ')


solution()