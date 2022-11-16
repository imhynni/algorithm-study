# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# SW Expert Academy 1225 <암호 생성기>
# D3

from collections import deque


def solution():
    while True:
        try:
            test_case = int(input())
            numbers = deque(map(int, input().split()))

            finish = False
            while (not finish):
                for i in range(1, 6):
                    new_number = numbers.popleft() - i
                    if new_number <= 0:
                        numbers.append(0)
                        finish = True
                        break
                    numbers.append(new_number)
            print(f'#{test_case}', end=' ')
            print(*numbers)
        except:
            break


solution()
