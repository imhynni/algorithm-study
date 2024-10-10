def solution(m, n, puddles):    
    puddles = {(y - 1, x - 1) for x, y in puddles}
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if (i , j) in puddles:
                continue
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= 1_000_000_007
    
    
    return dp[n - 1][m - 1]
