# https://www.acmicpc.net/problem/9935
# 백준 9935 <문자열 폭발>
# Gold 4
import sys


def solution():
    target_str = sys.stdin.readline().rstrip()
    explosion_str = list(sys.stdin.readline().rstrip())
    answer = []
    len_explosion_str = len(explosion_str)

    for s in target_str:
        answer.append(s)
        if len(answer) >= len_explosion_str:
            if answer[-len_explosion_str:] == explosion_str:
                answer[-len_explosion_str:] = []

    answer = ''.join(answer)
    if answer:
        print(answer)
    else:
        print('FRULA')


solution()
