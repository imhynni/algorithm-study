def solution(survey, choices):
    answer = ''
    types = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    count = dict()
    for t1, t2 in types:
        count[t1] = 0
        count[t2] = 0
        
    for i, choice in enumerate(choices):
        if choice < 4:
            count[survey[i][0]] += 4 - choice
        elif choice > 4:
            count[survey[i][1]] += choice - 4

    for t1, t2 in types:
        if count[t1] >= count[t2]:
            answer += t1
        else:
            answer += t2

    
    return answer
