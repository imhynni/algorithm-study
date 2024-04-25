import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().split()))
    left, right = 0, 1
    odd, even = 0, 0
    for i in range(n):
        if s[i] % 2 == 0:
            left, right = i, i + 1
            even += 1
            break
    else:
        right = n
    answer = even
    while right < n:
        if s[right] % 2 == 0:
            even += 1
            answer = max(answer, even)
            right += 1
            continue
        odd += 1
        if odd > k:
            answer = max(answer, even)
            while left < n:
                if s[left] % 2 == 0:
                    even -= 1
                    left += 1
                else:
                    odd -= 1
                    left += 1
                    break
            if left >= n:
                break
        right += 1

    print(answer)


solution()