# https://www.acmicpc.net/problem/11723
# 백준 11723 <집합>
# Silver 5
import sys


def solution():
    m = int(sys.stdin.readline())
    S = 0
    for _ in range(m):
        command = sys.stdin.readline().rstrip().split()
        if len(command) == 1:
            if command[0] == 'all':
                S = (1 << 20) - 1
            elif command[0] == 'empty':
                S = 0
        else:
            calc = command[0]
            x = int(command[1]) - 1
            if calc == 'add':
                S |= (1 << x)
            elif calc == 'remove':
                S &= ~(1 << x)
            elif calc == 'check':
                if S & (1 << x):
                    print(1)
                else:
                    print(0)
            elif calc == 'toggle':
                S ^= (1 << x)


solution()
