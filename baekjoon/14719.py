# https://www.acmicpc.net/problem/14719
# 백준 14719 <빗물>
# Gold 5
import sys


def solution():
    h, w = map(int, sys.stdin.readline().split())
    heights = list(map(int, sys.stdin.readline().split()))
    max_h = heights[0]
    start = 0

    answer = 0
    rain = 0
    for i in range(1, w):
        if i == w - 1 and heights[i] < max_h:
            rain -= (max_h - heights[i]) * (i - start - 1)
            answer += rain
        if max_h > heights[i]:
            rain += max_h - heights[i]
        else:
            answer += rain
            rain = 0
            start = i
            max_h = max(max_h, heights[i])
    print(answer)


def solution2():
    h, w = map(int, sys.stdin.readline().split())
    heights = list(map(int, sys.stdin.readline().split()))
    max_h = max(heights)

    answer = 0
    for i in range(1, w - 1):
        if heights[i] == max_h:
            continue
        max_left = max(heights[:i])
        max_right = max(heights[i + 1:])
        target = min(max_left, max_right)
        if target > heights[i]:
            answer += target - heights[i]
    print(answer)


solution()

# solution()
