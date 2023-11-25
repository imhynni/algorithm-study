import sys


def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    numbers = []
    for _ in range(n):
        numbers.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if i > 0:
                numbers[i][j] += numbers[i - 1][j]
            if j > 0:
                numbers[i][j] += numbers[i][j - 1]
            if i > 0 and j > 0:
                numbers[i][j] -= numbers[i - 1][j - 1]
                
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        answer = numbers[x2 - 1][y2 - 1]
        if x1 > 1:
            answer -= numbers[x1 - 2][y2 - 1]
        if y1 > 1:
            answer -= numbers[x2 - 1][y1 - 2]
        if x1 > 1 and y1 > 1:
            answer += numbers[x1 - 2][y1 - 2]
        print(answer)
        
        
solution()