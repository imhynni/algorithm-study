# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
# SW Expert Academy 1859 <백만장자 프로젝트>
# D2

import sys


def solution():
    input = sys.stdin.readline
    T = int(input())

    for i in range(T):
        n = int(input())
        price = list(map(int, input().split()))
        max_price = price[-1]
        profit = 0
        for j in range(n - 2, -1, -1):
            if price[j] < max_price:
                profit += max_price - price[j]
            else:
                max_price = price[j]

        print("#{} {}".format(i + 1, profit))


solution()
