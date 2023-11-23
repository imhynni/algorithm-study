from collections import defaultdict
import math


def dfs(match_id, idx, n, selected_id, answer):
    if idx == n:
        if selected_id not in answer:
            answer.append(selected_id)
        return
    for id in match_id[idx]:
        if id in selected_id:
            continue
        copy_selected_id = selected_id.copy()
        copy_selected_id.add(id)
        dfs(match_id, idx + 1, n, copy_selected_id, answer) 


def solution(user_id, banned_id):
    answer = []
    match_id = defaultdict(list)
    n = len(banned_id)
    
    for i, b_id in enumerate(banned_id):
        for u_id in user_id:
            if len(b_id) != len(u_id):
                continue
            for j, k in zip(b_id, u_id):
                if j == '*':
                    continue
                if j != k:
                    break
            else:
                match_id[i].append(u_id)
    
    dfs(match_id, 0, n, set(), answer)
    
    return len(answer)

# 밴 리스트의 아이디마다 매칭되는 애들 저장
# 탐색하면서 중복되지 않게 선택되는 경우 카운트