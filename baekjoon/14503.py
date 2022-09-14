# https://www.acmicpc.net/problem/14503
# 백준 14503 <로봇 청소기>
# Gold 5
import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    # 인덱스 : 현재 보고 있는 뱡향, (n, m, d) : 왼쪽으로 이동할 경우 변위와 방향
    left_direction = [(0, -1, 3), (-1, 0, 0), (0, 1, 1), (1, 0, 2)]
    back_direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    area = []
    count = 0
    finish = False

    for _ in range(n):
        area.append(list(map(int, sys.stdin.readline().split())))

    while True:
        already_clean = 0
        if area[r][c] == 0:
            # 현재 위치 청소하고
            area[r][c] = -1
            count += 1
            # 왼쪽 방향 탐색
            while True:
                (temp_r, temp_c, new_d) = left_direction[d]
                new_r, new_c = r + temp_r, c + temp_c
                # 왼쪽 아직 청소 안 했으면 이동
                if area[new_r][new_c] == 0:
                    # 현재 상태 갱신
                    r, c, d = new_r, new_c, new_d
                    break
                # 청소 돼있거나 벽일 경우
                else:
                    # 네 방향 모두 청소가 돼있다면
                    if already_clean == 4:
                        already_clean = 0
                        # 방향 유지한 채 후진
                        r, c, d = r + \
                            back_direction[d][0], c + back_direction[d][1], d
                        # 벽이라서 후진 못 하면 멈춤
                        if area[r][c] == 1:
                            finish = True
                            break
                        continue
                    already_clean += 1
                    # 왼쪽으로 회전만
                    d = left_direction[d][2]

        if finish:
            break
    print(count)


solution()
