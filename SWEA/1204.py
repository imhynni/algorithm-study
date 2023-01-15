# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYUu1hG6O44DFARs&contestProbId=AV13zo1KAAACFAYh&probBoxId=AYUyLam6ojkDFARs&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=5
# SWEA 1204 <최빈수 구하기>
# D2

from collections import defaultdict


def solution():
    t = int(input())
    for _ in range(t):
        tc = int(input())
        scores = list(map(int, input().split()))
        score_count = defaultdict(int)

        for score in scores:
            score_count[score] += 1

        print(f'#{tc} {max(score_count, key=score_count.get)}')


solution()
