# https://www.acmicpc.net/problem/20056
# 백준 20056 <마법사 상어와 파이어볼>
# Gold 4

from collections import defaultdict
import sys


def solution():
    input = sys.stdin.readline
    direction = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                 (1, 0), (1, -1), (0, -1), (-1, -1)]
    N, M, K = map(int, input().split())
    fireball = defaultdict(list)
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())  # 위치, 질량, 속력, 방향
        fireball[(r - 1, c - 1)].append((m, s, d))
    for _ in range(K):
        temp_move = []  # 모든 파이어볼이 이동한 후 한번에 갱신해주기 위해 저장해둘 리스트
        for x, y in fireball.keys():
            while fireball[(x, y)]:
                m, s, d = fireball[(x, y)].pop()
                dx, dy = direction[d]
                nx, ny = (x + dx * s) % N, (y + dy * s) % N
                temp_move.append((nx, ny, m, s, d))
        # 이동한 파이어볼들 위치 갱신
        for x, y, m, s, d in temp_move:
            fireball[(x, y)].append((m, s, d))
        # 파이어볼이 2개 이상 있는 위치 처리
        for x, y in fireball.keys():
            if len(fireball[(x, y)]) < 2:
                continue
            mass_sum = 0
            speed_sum = 0
            size = len(fireball[(x, y)])
            direction_check = fireball[(x, y)][-1][2] % 2
            while fireball[(x, y)]:
                m, s, d = fireball[(x, y)].pop()
                mass_sum += m
                speed_sum += s
                if direction_check != d % 2:
                    direction_check = -1
            new_m = mass_sum // 5
            if new_m == 0:
                continue
            new_s = speed_sum // size
            new_d = [0, 2, 4, 6] if direction_check != -1 else [1, 3, 5, 7]
            for d in new_d:
                fireball[(x, y)].append((new_m, new_s, d))
    answer = 0
    for fireballs in fireball.values():
        for m, _, _ in fireballs:
            answer += m
    print(answer)


solution()

# 1. 파이어볼 M개
# 2. 파이어볼 위치, 질량, 방향, 속력
# 3. 방향은 상하좌우대각선 모두 포함
# 4. 이동 명령
# 4-1. 모든 파이어볼이 자신의 방향으로 속력만큼 이동
# 4-2. 이동 끝나고 같은 칸에 2개 이상의 파이어볼이 있으면
# 4-2-1. 같은 칸에 있는 파이어볼 모두 하나로 합쳐짐
# 4-2-2. 파이어볼은 4개의 파이어볼로 나눠짐
# 4-2-3. 나눠진 파이어볼 질량 = 질량 합 / 5
# 4-2-4. 나눠진 파이어볼 속력 = 속력 합 / 파이어볼 개수
# 4-2-5. 방향은 모두 홀수이거나 짝수이면 0, 2, 4, 6 이 되고, 아니면 1, 3, 5, 7
# 4-2-6. 질량 0인 파이어볼은 소멸되어 없어진다.
# -> K번 이동을 한 후 남아있는 파이어볼의 질량 합
