import heapq
from collections import deque


def solution(stones, k):
    answer = 0
    left, right = 1, 200_000_000
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for stone in stones:
            if mid > stone:
                count += 1
            else:
                count = 0
            if count >= k:
                right = mid - 1
                break
        if count < k:
            left = mid + 1
            answer = max(answer, mid)

    
    return answer
