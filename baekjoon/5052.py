# https://www.acmicpc.net/problem/5052
# 백준 5052 <전화번호 목록>
# Gold 4
import sys


def solution():
    readline = sys.stdin.readline
    t = int(readline())

    for _ in range(t):
        finish = False
        n = int(readline())
        phone_numbers_set = set()
        phone_numbers_list = []

        for i in range(n):
            phone_number = readline().rstrip()
            phone_numbers_set.add(phone_number)
            phone_numbers_list.append(phone_number)

        for phone in phone_numbers_list:
            len_phone = len(phone)
            for i in range(len_phone - 1):
                if phone[:i + 1] in phone_numbers_set:
                    finish = True
                    break
            if finish:
                print('NO')
                break
        else:
            print('YES')


solution()
