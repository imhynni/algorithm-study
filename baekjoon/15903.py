# https://www.acmicpc.net/problem/15903
# 백준 15903 <카드 합체 놀이>
# Silver 1

import sys
from heapq import heapify, heappop, heappush


def solution():
    _, m = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
    # 리스트를 힙 형태로 변환
    heapify(cards)
    for _ in range(m):
        # 최소값, 그 다음 최소값 뽑기
        first, second = heappop(cards), heappop(cards)
        # 더한 값으로 덮어쓰기
        heappush(cards, first + second)
        heappush(cards, first + second)
    print(sum(cards))


solution()
