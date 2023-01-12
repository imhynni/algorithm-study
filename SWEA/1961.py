# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYUu1hG6O44DFARs&contestProbId=AV5Pq-OKAVYDFAUq&probBoxId=AYUyLam6ojkDFARs&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=5
# SWEA 1961 <숫자 배열 회전>
# D2

def solution():
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(input().split()))

        matrix_90 = [item[:] for item in matrix]
        for i in range(n):
            for j in range(n):
                matrix_90[i][j] = matrix[n - j - 1][i]

        matrix_180 = [item[:] for item in matrix_90]
        for i in range(n):
            for j in range(n):
                matrix_180[i][j] = matrix_90[n - j - 1][i]

        matrix_270 = [item[:] for item in matrix_180]
        for i in range(n):
            for j in range(n):
                matrix_270[i][j] = matrix_180[n - j - 1][i]

        print(f'#{tc}')
        for k in range(n):
            temp = []
            temp.append("".join(matrix_90[k]))
            temp.append("".join(matrix_180[k]))
            temp.append("".join(matrix_270[k]))
            print(" ".join(temp))


solution()
