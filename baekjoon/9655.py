# https://www.acmicpc.net/problem/9655
# 백준 9655 <돌 게임>
# Silver 5

def solution():
    n = int(input())
    dp = ['WIN'] * (n + 1)

    for i in range(2, n + 1):
        if dp[i - 1] == 'WIN':
            dp[i] = 'LOSE'
        elif i - 3 > 0 and dp[i - 3] == 'WIN':
            dp[i] = 'LOSE'

    if dp[n] == 'WIN':
        print('SK')
    else:
        print('CY')


solution()
