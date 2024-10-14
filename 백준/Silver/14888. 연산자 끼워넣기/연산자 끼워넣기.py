import sys


min_answer = float('inf')
max_answer = float('-inf')


def backtracking(n, nums, operators, result):
    global min_answer, max_answer
    if len(result) == n - 1:
        total = nums[0]
        for j in range(n - 1):
            operator = result[j]
            if operator == 0:
                total += nums[j + 1]
            elif operator == 1:
                total -= nums[j + 1]
            elif operator == 2:
                total *= nums[j + 1]
            elif operator == 3:
                if total < 0:
                    total = -(-total // nums[j + 1])
                else:
                    total //= nums[j + 1]
        min_answer = min(min_answer, total)
        max_answer = max(max_answer, total)
        return

    for i in range(len(operators)):
        if operators[i] > 0:
            result.append(i)
            operators[i] -= 1
            backtracking(n, nums, operators, result)
            result.pop()
            operators[i] += 1


def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    backtracking(n, nums, operators, [])
    print(max_answer)
    print(min_answer)


solution()
