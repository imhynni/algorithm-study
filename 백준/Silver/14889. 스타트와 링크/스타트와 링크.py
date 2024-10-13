import sys


answer = float('inf')


def make_team(n, r, start, scores, team_start):
    global answer
    if r == n // 2:
        score_start = 0
        score_link = 0
        for j in range(n - 1):
            for k in range(j + 1, n):
                if team_start[j] and team_start[k]:
                    score_start += scores[j][k] + scores[k][j]
                elif not team_start[j] and not team_start[k]:
                    score_link += scores[j][k] + scores[k][j]
        answer = min(answer, abs(score_start - score_link))
        return
    for i in range(start, n):
        team_start[i] = True
        make_team(n, r + 1, i + 1, scores, team_start)
        team_start[i] = False


def solution():
    n = int(sys.stdin.readline())
    scores = []
    for _ in range(n):
        scores.append(list(map(int, sys.stdin.readline().split())))

    team_start = [False] * n
    team_start[0] = True
    make_team(n, 1, 1, scores, team_start)
    print(answer)


solution()