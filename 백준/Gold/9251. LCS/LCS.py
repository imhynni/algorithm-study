import sys


def solution():
    str_a = sys.stdin.readline().rstrip()
    str_b = sys.stdin.readline().rstrip()
    
    LCS = [[0] * (len(str_b) + 1) for _ in range(len(str_a) + 1)]
    for i in range(len(str_a) + 1):
        for j in range(len(str_b) + 1):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            elif str_a[i - 1] == str_b[j - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            else:
                LCS[i][j] = max(LCS[i][j - 1], LCS[i - 1][j])
    
    print(LCS[len(str_a)][len(str_b)])


solution()