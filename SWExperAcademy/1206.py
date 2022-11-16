# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh
# SW Expert Academy 1206 <View>
# D3

import sys


def solution():
    T = 10
    input = sys.stdin.readline
    for test_case in range(1, T + 1):
        n = int(input())
        total_apartment = 0
        heights = [0, 0]
        heights.extend(map(int, input().split()))
        heights.extend([0, 0])

        for i in range(2, len(heights) - 2):
            if heights[i - 1] >= heights[i] or heights[i] <= heights[i + 1] \
                    or heights[i - 2] >= heights[i] or heights[i] <= heights[i + 2]:
                continue
            total_apartment += min(
                heights[i] - heights[i - 1], heights[i] - heights[i - 2], heights[i] - heights[i + 1], heights[i] - heights[i + 2])
        print("#{} {}".format(test_case, total_apartment))


def solution2():
    T = 10
    input = sys.stdin.readline
    for test_case in range(1, T + 1):
        n = int(input())
        total_apartment = 0
        heights = [0, 0]
        heights.extend(map(int, input().split()))
        heights.extend([0, 0])

        for i in range(2, len(heights) - 2):
            max_height = max(heights[i - 2:i] + heights[i + 1:i + 3])
            print(max_height)
            if heights[i] > max_height:
                total_apartment += heights[i] - max_height
        print('#{} {}'.format(test_case, total_apartment))


solution2()
