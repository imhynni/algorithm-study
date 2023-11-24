import sys
from collections import defaultdict


def solution():
    input =  sys.stdin.readline
    n, m = map(int,input().split())
    heights = list(map(int, input().split()))
    edges = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
        
    for idx, h in enumerate(heights):
        heights[idx] = (h, idx)
    
    sorted_heights = sorted(heights, reverse=True)
    
    dp = [1] * n
    for height, i in sorted_heights:
        for edge in edges[i]:
            if heights[edge][0] > height:
                continue
            dp[edge] = max(dp[edge], dp[i] + 1)
        
    for count in dp:
        print(count)  


solution()