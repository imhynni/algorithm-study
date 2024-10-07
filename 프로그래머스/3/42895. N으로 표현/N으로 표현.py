def concat_numbers(num, count):
    result = 0
    for i in range(count):
        result += num * 10 ** i
    return result


def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(concat_numbers(N, i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    if a - b >= 0:
                        dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        if number in dp[i]:
            answer = i
            break
    else:
        answer = -1
    
    
    return answer
