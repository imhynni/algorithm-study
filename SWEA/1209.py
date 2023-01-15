# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV13_BWKACUCFAYh&solveclubId=AYUu1hG6O44DFARs&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=5&probBoxId=AYUyLam6ojkDFARs
# SWEA 1209 <Sum>
# D3

def solution():
    for _ in range(10):
        tc = int(input())

        nums = []
        max_sum = 0
        for i in range(100):
            nums.append(list(map(int, input().split())))
            max_sum = max(max_sum, sum(nums[i]))

        for j in range(100):
            col_sum = 0
            for i in range(100):
                col_sum += nums[i][j]
            max_sum = max(max_sum, col_sum)

        diagonal_sum, diagonal_sum2 = 0, 0
        for i in range(100):
            diagonal_sum += nums[i][i]
            diagonal_sum2 += nums[i][99 - i]
        max_sum = max(max_sum, diagonal_sum, diagonal_sum2)

        print(f'#{tc} {max_sum}')


solution()
