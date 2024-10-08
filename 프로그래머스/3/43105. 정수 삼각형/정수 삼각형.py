def solution(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(i + 1):
            left = triangle[i + 1][j]
            right = triangle[i + 1][j + 1]
            triangle[i][j] += max(left, right)

    
    return triangle[0][0]
