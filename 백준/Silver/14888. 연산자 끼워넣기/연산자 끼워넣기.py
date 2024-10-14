import sys


min_answer = float('inf')
max_answer = float('-inf')


def backtracking(n, nums, operators, count, total):
    global min_answer, max_answer
    if count == n - 1:
        min_answer = min(min_answer, total)
        max_answer = max(max_answer, total)
        return

    for i in range(len(operators)):
        if operators[i] > 0:
            operators[i] -= 1
            temp_total = total
            if i == 0:
                temp_total += nums[count + 1]
            elif i == 1:
                temp_total -= nums[count + 1]
            elif i == 2:
                temp_total *= nums[count + 1]
            elif i == 3:
                if temp_total < 0:
                    temp_total = -(-temp_total // nums[count + 1])
                else:
                    temp_total //= nums[count + 1]
            backtracking(n, nums, operators, count + 1, temp_total)
            operators[i] += 1


def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    backtracking(n, nums, operators, 0, nums[0])
    print(max_answer)
    print(min_answer)


solution()
