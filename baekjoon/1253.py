# https://www.acmicpc.net/problem/1253
# 백준 1253 <좋다>
# Gold 4
import sys


def solution():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    A.sort()

    count = 0
    for i in range(N):
        temp_A = A[:i] + A[i+1:]  # A[i] 제외한 리스트
        start, end = 0, N - 2
        while start < end:
            sum_A = temp_A[start] + temp_A[end]
            if A[i] == sum_A:
                count += 1
                break
            if A[i] > sum_A:
                start += 1
            else:
                end -= 1
    print(count)


solution()
