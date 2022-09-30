# https://www.acmicpc.net/problem/16472
# 백준 16472 <고냥이>
# Gold 4
from collections import defaultdict
import sys


def solution():
    n = int(sys.stdin.readline())
    string = list(sys.stdin.readline().rstrip())
    nums_cnt = defaultdict(int)

    answer = 0
    start, end = 0, 1
    nums_cnt[string[start]] += 1
    nums_cnt[string[end]] += 1

    while True:
        if len(nums_cnt) <= n:
            answer = max(answer, end - start + 1)
            end += 1
            if end >= len(string):
                break
            nums_cnt[string[end]] += 1
        else:
            nums_cnt[string[start]] -= 1
            if nums_cnt[string[start]] == 0:
                del nums_cnt[string[start]]
            start += 1

    print(answer)


solution()
