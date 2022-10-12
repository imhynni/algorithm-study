# https://www.acmicpc.net/problem/11501
# 백준 11501 <주식>
# Silver 2
import sys


def solution():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        price = list(map(int, input().split()))
        max_price = price[-1]
        buy = []
        answer = 0
        for i in range(n - 2, -1, -1):
            if price[i] > max_price:
                while buy:
                    answer += max_price - buy.pop()
                max_price = price[i]
            if price[i] < max_price:
                buy.append(price[i])
        while buy:
            answer += max_price - buy.pop()
        print(answer)


solution()
