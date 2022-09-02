# https://www.acmicpc.net/problem/9012
# 백준 9012 <괄호>
# Silver 4

import sys


def solution():
    t = int(input())
    for _ in range(t):
        ps = sys.stdin.readline().rstrip()
        stack = []
        answer = 'YES'
        if ps[0] == ')':
            answer = 'NO'
        else:
            for i in range(len(ps)):
                if ps[i] == '(':
                    stack.append(ps[i])
                elif ps[i] == ')':
                    if stack:
                        stack.pop()
                    else:
                        answer = 'NO'
                        break
            if stack:
                answer = 'NO'
        print(answer)


solution()
