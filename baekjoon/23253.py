import sys


def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    answer = "Yes"
    for _ in range(m):
        k = int(input())
        books = list(map(int, input().split()))
        for i in range(k - 1):
            if books[i] < books[i + 1]:
                answer = "No"
                break
    print(answer)


solution()
