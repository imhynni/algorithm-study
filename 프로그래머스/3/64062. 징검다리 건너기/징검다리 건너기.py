import heapq

def solution(stones, k):
    n = len(stones)
    q = []
    
    if n < k:
        return max(stones)
    
    for i in range(k):
        heapq.heappush(q, (-stones[i], i))
    answer = -q[0][0]
    
    for i in range(1, n - k + 1):
        while q and q[0][1] < i:
            heapq.heappop(q)
        heapq.heappush(q, (-stones[i + k - 1], i + k - 1))
        answer = min(answer, -q[0][0])
    
    
    return answer
