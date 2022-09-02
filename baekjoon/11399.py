# https://www.acmicpc.net/problem/11399
# 백준 11399 <ATM>
# Silver 4

n = int(input())
p = list(map(int, input().split()))
answer = 0

p.sort()

for i in p:
    answer += i
    p[p.index(i)] = answer

print(sum(p))
