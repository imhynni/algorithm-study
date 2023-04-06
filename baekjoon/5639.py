# https://www.acmicpc.net/problem/5639
# 백준 5639 <이진 검색 트리>
# Gold 5

import sys
sys.setrecursionlimit(10**6)
pre = []


def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(pre[start])


def solution():
    while True:
        try:
            num = int(sys.stdin.readline())
            pre.append(num)
        except:
            break
    postorder(0, len(pre) - 1)


solution()

# 첫번째 원소 = 루트
# 그 뒤 보면서 나보다 큰 거 나오는 순간 찾기
#
