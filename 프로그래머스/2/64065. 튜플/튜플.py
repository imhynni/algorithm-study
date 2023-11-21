import re


def solution(s):
    tuple_sets = s.split('},{')
    set_list = []
    for tuple_set in tuple_sets:
        tuple_set = re.sub(r'[{}]', '', tuple_set)
        set_list.append(list(map(int, tuple_set.split(','))))
    set_list.sort(key=len)
    
    answer = set_list[0]
    for numbers in set_list:
        for number in numbers:
            if number not in answer:
                answer.append(number)
                break

    
    return answer
