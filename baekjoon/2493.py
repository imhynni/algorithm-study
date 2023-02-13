# https://www.acmicpc.net/problem/2493
# 백준 2493 <탑>
# Gold 5
import sys


def solution():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    stack = []
    answer = [0] * n
    for i in range(n - 1, 0, -1):
        stack.append((i, heights[i]))
        while stack and stack[-1][1] <= heights[i - 1]:
            index, _ = stack.pop()
            answer[index] = i  # i - 1 + 1
    print(*answer)


def solution2():
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    stack = []
    answer = [0] * n
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] < heights[i]:
            answer[stack.pop()] = i + 1
        stack.append(i)
    print(*answer)


# solution()
solution2()
