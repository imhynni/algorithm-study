# https://www.acmicpc.net/problem/2529
# 백준 2529 <부등호>
# Silver 1

import itertools
import sys


def solution():
    nums = list(range(10))
    k = int(sys.stdin.readline())
    signs = list(sys.stdin.readline().rstrip().split())
    answer = []
    answer2 = []

    # 순열 저장
    per = list(itertools.permutations(nums, k + 1))

    # 최소값은 앞에서부터 탐색, 최대값은 뒤에서부터 탐색
    # 최대값 구하기
    for i in range(len(per) - 1, 0, -1):
        if len(answer) == k + 1:
            break
        for j in range(k):
            if not answer:
                answer.append(per[i][j])
            if (signs[j] == '<' and per[i][j] > per[i][j + 1]) or (signs[j] == '>' and per[i][j] < per[i][j + 1]):
                answer = []
                break
            answer.append(per[i][j + 1])

    # 최소값 구하기
    for p in per:
        if len(answer2) == k + 1:
            break
        for j in range(k):
            if not answer2:
                answer2.append(p[j])
            if (signs[j] == '<' and p[j] > p[j + 1]) or (signs[j] == '>' and p[j] < p[j + 1]):
                answer2 = []
                break
            answer2.append(p[j + 1])

    answer = ''.join(str(s) for s in answer)
    print(answer)
    answer2 = ''.join(str(s) for s in answer2)
    print(answer2)


solution()
