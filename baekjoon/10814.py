# https://www.acmicpc.net/problem/10814
# 백준 10814 <나이순 정렬>
# Silver 5

import sys


def solution():
    input = sys.stdin.readline
    n = int(input())
    members = []
    for i in range(n):
        age, name = input().split()
        members.append((i, int(age), name))

    members.sort(key=lambda x: (x[1], x[0]))

    for member in members:
        print(member[1], member[2])


solution()


# 특정 키 기준으로 정렬하기, 다중 조건 정렬
# sorted(), sort()
# https://infinitt.tistory.com/122
