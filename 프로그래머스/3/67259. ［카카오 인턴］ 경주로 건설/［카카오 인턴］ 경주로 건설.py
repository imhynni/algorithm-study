from heapq import heappush, heappop


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(board):
    answer = float('inf')
    n = len(board)
    cost = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    q = []
    heappush(q, (0, 0, -1, 0))
    cost[0][0] = [0, 0, 0, 0]
    while q:
        i, j, prev_d, c = heappop(q)
        if prev_d != -1 and cost[i][j][prev_d] < c:
            continue
        if c >= answer:
            continue
        cost[i][j][prev_d] = c
        if (i, j) == (n - 1, n - 1):
            answer = min(answer, c)
        for d in range(4):
            dx, dy = directions[d]
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue
            next_cost = 100
            if prev_d > -1:
                if abs(prev_d - d) == 2:
                    continue
                next_cost += c
                if d % 2 != prev_d % 2:
                    next_cost += 500
            heappush(q, (nx, ny, d, next_cost))
        

    return answer
