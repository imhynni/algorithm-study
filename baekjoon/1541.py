# https://www.acmicpc.net/problem/1541
# 백준 1541 <잃어버린 괄호>
# Silver 2

str = input()
nums = str.split('-')
new_nums = []
for i in nums:
    sub_nums = list(map(int, i.split('+')))
    new_nums.append(sum(sub_nums))
answer = new_nums[0]
for i in range(1, len(new_nums)):
    answer -= new_nums[i]
print(answer)
