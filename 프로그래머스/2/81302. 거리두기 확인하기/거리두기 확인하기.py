def solution(places):
    answer = []
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n = 5
    for place in places:
        finish = False
        for i in range(n):
            for j in range(n):
                if place[i][j] != 'P':
                    continue
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                        continue
                    if place[nx][ny] == 'P':
                        answer.append(0)
                        finish = True
                        break
                    if place[nx][ny] == 'O':
                        for n_dx, n_dy in directions:
                            n_nx, n_ny = nx + n_dx, ny + n_dy
                            if n_nx < 0 or n_nx >= 5 or n_ny < 0 or n_ny >= 5:
                                continue
                            if (n_nx, n_ny) == (i, j):
                                continue
                            if place[n_nx][n_ny] == 'P':
                                answer.append(0)
                                finish = True
                                break
                    if finish:
                        break
                if finish:
                    break
            if finish:
                break
        if not finish:
            answer.append(1)
    
    return answer
