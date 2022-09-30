# https://www.acmicpc.net/problem/1806
# 백준 1806 <부분합>
# Gold 4
import sys


def solution():
    n, s = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    sum_nums = [0] * (n + 1)

    for i in range(1, n + 1):
        sum_nums[i] = sum_nums[i - 1] + nums[i - 1]

    answer = sys.maxsize
    start, end = 1, 1
    while start <= end < n + 1:
        sub_sum = sum_nums[end] - sum_nums[start - 1]
        if sub_sum < s:
            end += 1
        elif sub_sum >= s:
            answer = min(answer, end - start + 1)
            start += 1
            if sub_sum == s:
                end += 1
    if answer == sys.maxsize:
        answer = 0

    print(answer)


solution()
