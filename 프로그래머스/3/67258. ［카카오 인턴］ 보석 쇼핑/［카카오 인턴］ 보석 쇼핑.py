from collections import Counter


def solution(gems):
    n = len(gems)
    k = len(set(gems))
    
    left, right = 0, k - 2
    answer = [1, n]
    count = Counter(gems[left:right + 1])
    
    while right < n - 1:
        right += 1
        count[gems[right]] += 1
        while len(count) == k:
            if right - left < answer[1] - answer[0]:
                answer[0], answer[1] = left + 1, right + 1
            count[gems[left]] -= 1
            if count[gems[left]] == 0:
                count.pop(gems[left])
            left += 1

    return answer
