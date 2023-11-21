import re
import sys
sys.setrecursionlimit(10**6)


def permutations(k, result, source, output):
    if len(result) == k:
        output.append(result)
    for i in range(len(source)):
        permutations(k, result + [source[i]], source[:i] + source[i + 1:], output)

        
def calc(a, o, b):
    if o == '+':
        return a + b
    if o == '-':
        return a - b
    if o == '*':
        return a * b
        

def solution(expression):
    answer = 0
    
    operand = ['+', '-', '*']
    permutation = []
    permutations(3, [], operand, permutation)
    numbers = re.findall(r'(\d+|\D)', expression)
    numbers = list(map(lambda x: int(x) if x.isdigit() or x.isdigit() and x[0] == '-' else x, numbers))
    
    for perm in permutation:
        copy_numbers = numbers[:]
        for o in perm:
            n = len(copy_numbers)
            i = 1
            while i < n:
                if copy_numbers[i] == o:
                    copy_numbers[i - 1] = calc(copy_numbers[i - 1], o, copy_numbers[i + 1])
                    copy_numbers = copy_numbers[:i] + copy_numbers[i + 2:]
                    n -= 2
                else:
                    i += 2
                    
        answer = max(answer, abs(copy_numbers[0]))
    
    return answer
