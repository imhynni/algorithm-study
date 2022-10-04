# https://www.acmicpc.net/problem/20922
# 백준 20922 <겹치는 건 싫어>
# Silver 1
from collections import defaultdict
import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums_count = defaultdict(int)

    start, end = 0, 0
    nums_count[nums[start]] += 1
    answer = 0
    while end < n:
        if nums_count[nums[end]] > k:
            answer = max(answer, end - start)
            while True:
                nums_count[nums[start]] -= 1
                start += 1
                if nums_count[nums[end]] == k:
                    break
        else:
            if end == n - 1:
                answer = max(answer, end - start + 1)
                break
            end += 1
            nums_count[nums[end]] += 1
    print(answer)


solution()
