# https://www.acmicpc.net/problem/4948
# 백준 4948 <베르트랑 공준>
# Silver 3

import sys
import math


def solution():
    while True:
        n = int(sys.stdin.readline())
        n2 = 2 * n
        if n == 0:
            break
        is_prime = [True] * (n2 + 1)
        is_prime[0] = False
        is_prime[1] = False
        m = int(math.sqrt(n2))
        for i in range(2, m + 1):
            if is_prime[i] == True:
                j = 2
                while i * j <= n2:
                    is_prime[i * j] = False
                    j += 1
        print(is_prime[n + 1:].count(True))


solution()
