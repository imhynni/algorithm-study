# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYUu1hG6O44DFARs&contestProbId=AV5Psz16AYEDFAUq&probBoxId=AYUyLam6ojkDFARs&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=5
# SWEA 1974 <스도쿠 검증>
# D2

from collections import defaultdict


def solution():
    t = int(input())
    for tc in range(1, t + 1):
        sudoku = []
        for _ in range(9):
            sudoku.append(list(input().split()))

        answer = 1
        column_sets = defaultdict(set)
        grid_sets = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if len(set(sudoku[i])) < 9:
                    answer = 0
                    break
                column_sets[j].add(sudoku[i][j])
                grid_sets[(i // 3, j // 3)].add(sudoku[i][j])
            if answer == 0:
                break

        if answer == 1:
            for _, col_nums in column_sets.items():
                if len(col_nums) < 9:
                    answer = 0
                    break
            for _, grid_nums in grid_sets.items():
                if len(grid_nums) < 9:
                    answer = 0
                    break

        print(f'#{tc}', answer)


solution()
