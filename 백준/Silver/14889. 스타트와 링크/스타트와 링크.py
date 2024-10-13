import sys
from itertools import combinations


def total_score(team, score):
    total = 0
    for i, j in combinations(team, 2):
        total += score[i][j] + score[j][i]
    return total


def solution():
    n = int(sys.stdin.readline())
    score = []
    for _ in range(n):
        score.append(list(map(int, sys.stdin.readline().split())))

    answer = float("inf")
    for team_1 in combinations(range(n), n // 2):
        team_2 = [x for x in range(n) if x not in team_1]
        if team_2[0] < team_1[0]:
            break
        score_1 = total_score(team_1, score)
        score_2 = total_score(team_2, score)
        answer = min(answer, abs(score_1 - score_2))

    print(answer)


solution()