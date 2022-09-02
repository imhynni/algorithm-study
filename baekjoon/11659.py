# https://www.acmicpc.net/problem/11659
# 백준 11659 <구간 합 구하기 4>
# Silver 3

import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
s_sum = 0
result = [0]

for i in num:
    s_sum += i
    result.append(s_sum)
for m in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(result[j] - result[i - 1])