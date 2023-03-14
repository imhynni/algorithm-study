# https://www.acmicpc.net/problem/16235
# 백준 16235 <나무 재테크>
# Gold 3

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    direction = [(-1, 0), (-1, 1), (0, 1),
                 (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    n, m, k = map(int, input().split())
    A = []
    area = [[5] * n for _ in range(n)]
    trees = [[deque() for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        A.append(list(map(int, input().split())))
    for _ in range(m):
        x, y, z = map(int, input().split())
        trees[x - 1][y - 1].append(z)
    for _ in range(k):
        # 봄
        for i in range(n):
            for j in range(n):
                death = 0
                temp_tree = deque()
                for age in trees[i][j]:
                    if age <= area[i][j]:
                        area[i][j] -= age
                        temp_tree.append(age + 1)
                    else:
                        death += age // 2
                        m -= 1
                trees[i][j] = temp_tree
                # 여름
                area[i][j] += death
        # 가을
        for x in range(n):
            for y in range(n):
                for tree in trees[x][y]:
                    if tree % 5 != 0:
                        continue
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        trees[nx][ny].appendleft(1)
                        m += 1
                # 겨울
                area[x][y] += A[x][y]
    print(m)


solution()

# m개의 나무, 같은 칸에 여러 개 심을 수도 있음, 나무 위치는 고정
# -- 봄
# 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
# 자기가 있는 칸의 양분만 먹을 수 있음
# 나무가 여러개면 어린 나무부터 양분 먹음
# 남은 양분이 자기 나이보다 적으면 못 먹고 걍 죽음
# -- 여름
# 봄에 죽은 나무가 양분이 됨
# 죽은 나무마다 나이를 2로 나눈 값(몫)이 해당 칸에 양분으로 추가됨
# -- 가을
# 나무가 번식함
# 나이가 5의 배수여야 번식 가능
# 인접 8칸에 나이가 1인 나무가 생김
# -- 겨울
# 입력으로 주어진 A[r][c] 만큼 칸에 양분이 추가됨
