# https://www.acmicpc.net/problem/7795
# 백준 7795 <먹을 것인가 먹힐 것인가>
# Silver 3
import sys
import bisect


def solution():
    readline = sys.stdin.readline
    T = int(readline())

    for _ in range(T):
        n, _ = map(int, readline().split())
        A = list(map(int, readline().split()))
        B = list(map(int, readline().split()))
        A.sort()

        count = 0
        for target in B:
            start, end = 0, n - 1
            while start <= end:
                mid = (start + end) // 2
                if A[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            count += n - start
        print(count)


def solution2():
    readline = sys.stdin.readline
    T = int(readline())

    for _ in range(T):
        n, _ = map(int, readline().split())
        A = list(map(int, readline().split()))
        B = list(map(int, readline().split()))
        A.sort()

        count = 0
        for target in B:
            index = bisect.bisect_right(A, target)
            count += n - index

        print(count)


solution2()
