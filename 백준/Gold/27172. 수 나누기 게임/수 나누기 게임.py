from math import sqrt
import sys


def solution():
    n = int(sys.stdin.readline())
    cards = dict()
    numbers = list(map(int, sys.stdin.readline().split()))
    for number in numbers:
        cards[number] = 0
    for number in numbers:
        for i in range(1, int(sqrt(number)) + 1):
            if number % i != 0:
                continue
            if i in cards:
                cards[i] += 1
                cards[number] -= 1
            if i != number // i and number // i in cards:
                cards[number // i] += 1
                cards[number] -= 1
    answer = []
    for j in numbers:
        answer.append(cards[j])
    print(*answer)


solution()