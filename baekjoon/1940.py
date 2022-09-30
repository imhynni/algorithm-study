# https://www.acmicpc.net/problem/1940
# 백준 1940 <주몽>
# Silver 4
import sys


def solution():
    readline = sys.stdin.readline
    N = int(readline())
    M = int(readline())
    ingredients = list(map(int, readline().split()))
    ingredients.sort()

    start, end = 0, N - 1
    count = 0
    while start < end:
        ingredients_sum = ingredients[start] + ingredients[end]
        if ingredients_sum < M:
            start += 1
        elif ingredients_sum > M:
            end -= 1
        else:
            count += 1
            start += 1
            end -= 1

    print(count)


solution()
