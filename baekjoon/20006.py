# https://www.acmicpc.net/problem/20006
# 백준 20006 <랭킹전 대기열>
# Silver 2
import sys


def solution():
    p, m = map(int, sys.stdin.readline().split())
    players = dict()
    rooms = []

    for _ in range(p):
        l, n = sys.stdin.readline().split()
        players[n] = int(l)

    for pid, level in players.items():
        for room in rooms:
            if len(room) < m and abs(room[0][1] - level) <= 10:
                room.append((pid, level))
                break
        else:
            rooms.append([(pid, level)])

    for room in rooms:
        if len(room) == m:
            print('Started!')
        else:
            print('Waiting!')
        room.sort(key=lambda x: x[0])
        for player in room:
            print(player[1], player[0])


solution()
