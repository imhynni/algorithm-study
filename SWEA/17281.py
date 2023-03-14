# https://www.acmicpc.net/problem/17281
# 백준 17281 <야구>
# Gold 4

import sys
from itertools import permutations

N = int(sys.stdin.readline())
innings = []
for _ in range(N):
    innings.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for order in permutations(range(1, 9)):
    order = list(order)
    new_order = order[:3] + [0] + order[3:]
    score = 0
    p = 0
    for inning in range(N):
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out < 3:
            result = innings[inning][new_order[p]]
            if result == 0:
                out += 1
            elif result == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif result == 2:
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif result == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            else:
                score += base1 + base2 + base3 + 1
                base1, base2, base3 = 0, 0, 0
            p = (p + 1) % 9
    answer = max(answer, score)


print(answer)

# 아이디어
# 8명 타순 정하기 -> 8! (사람 수로 말고 나오는 결과 종류 수로)
# 1이닝, 2이닝 결과 모두 같은 경우 같은 사람 취급
# 모든 경우 다 해보면서 최대 점수 갱신
#

# 9명으로 이루어진 두 팀
# 공격 수비 번갈아
# 총 N이닝 게임 진행
# 한 이닝에 3아웃 발생 => 이닝 종료, 공격 수비 바꿈
# 경기 시작 전에 타순을 정함, 경기 중 변경 불가
# 9번 타자까지 쳤는데 3아웃 안되면 이닝 끝나지 않고, 1번이 다시 타자로
# 타순은 이닝이 변경돼도 순서 유지
# 2이닝에 6번 타자가 마지막 -> 3이닝은 7번 타자부터
# 공격이란 : 투수가 던진 공을 타자가 치는 것
# 공격 팀 선수가 1, 2, 3루 거쳐서 홈에 도착하면 1점 득점
# 홈 도착 못하고 1, 2, 3에 있을 수도 있음 (루에 있는 애는 주자라고 함)
# 이닝이 시작될 때는 주자 없음
# 타자가 공을 쳐서 얻는 결과는 안타, 2루타, 3루타, 홈런, 아웃 중 하나
# - 안타 : 타자와 모든 주자가 1루 진루
# - 2루타 : 타자와 모든 주자가 2루 진루
# - 3루타 : 타자와 모든 주자가 3루 진루
# - 홈런 : 타자와 모든 주자가 홈까지 진루
# - 아웃 : 모든 주자 진루 못 함, 공격 팀에 아웃 하나 증가
#
# 아인타 감독이 타순을 정하려고 함
# 아인타 팀 선수는 총 9명
# 1번 선수를 4번 타자로 미리 결정
# 각 선수가 각 이닝에서 어떤 결과를 얻는지 미리 알고 있음
# 가장 많은 득점을 하는 타순, 그때의 득점은?
# 각 이닝에는 아웃이 적어도 한 명 존재
