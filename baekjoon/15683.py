# https://www.acmicpc.net/problem/15683
# 백준 15683 <감시>
# Gold 4

import sys

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rotation = {1: [1], 2: [1, 3], 3: [0, 1],
            4: [0, 1, 3], 5: [0, 1, 2, 3]}
n, m = map(int, sys.stdin.readline().split())
area = []
cctv = []
cctv_dir = []
answer = sys.maxsize
size = 0  # 5번 cctv는 회전할 필요 없으니까 빼기 위해 세줌


def solution():
    count = 0
    for _ in range(n):
        area.append(list(map(int, sys.stdin.readline().split())))
    for i in range(n):
        for j in range(m):
            if 0 < area[i][j] < 6:
                cctv.append((area[i][j], i, j))
                if area[i][j] != 5:
                    global size
                    size += 1
            if area[i][j] == 0:
                count += 1
    global cctv_dir
    cctv_dir = [-1] * len(cctv)
    permutation(0, count)
    print(answer)


def permutation(depth, count):
    if depth == size:
        new_area = [row[:] for row in area]
        temp_count = watch(count, new_area)
        global answer
        answer = min(answer, temp_count)
        return
    for i in range(4):
        cctv_dir[depth] = i
        permutation(depth + 1, count)


def watch(count, area):
    i = 0
    for t, x, y in cctv:
        for r in rotation[t]:
            # 회전한 후의 방향 인덱스
            d = (r + cctv_dir[i]) % 4 if t != 5 else r
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            while -1 < nx < n and -1 < ny < m and area[nx][ny] != 6:
                if area[nx][ny] == 0:
                    area[nx][ny] = '#'
                    count -= 1
                nx += dx
                ny += dy
        if t != 5:
            i += 1
    return count


solution()

# 1. cctv 위치는 고정
# 2. cctv 마다 방향 바꿀 수 있음 (상하좌우)
# 2-1. 방향 선택은 중복순열
# 3. 벽은 못 뚫고, cctv는 뚫을 수 있음
# 4. 감시 못하는 칸의 최소 크기가 되도록 방향 설정
# 5. 최소 크기 출력
# cctv 회전 정보 저장 방법
# 딕셔너리로 cctv 종류를 키, 감시 방향을 값으로 저장
# 중복 순열로 뽑은 회전 방향에 따라 +, % 연산으로 딕셔너리에서 가져온 방향 바꿔줌
