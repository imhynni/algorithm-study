def solution(n, k, cmd):
    answer = ['O'] * n
    stack = []
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    
    for command in cmd:
        if command == 'C':
            prev_i, next_i = table[k]
            answer[k] = 'X'
            stack.append([k, prev_i, next_i])
            k = next_i if next_i is not None else prev_i
            
            if prev_i is not None:
                table[prev_i][1] = next_i
            if next_i is not None:
                table[next_i][0] = prev_i
        elif command == 'Z':
            curr_i, prev_i, next_i = stack.pop()
            if prev_i is not None:
                table[prev_i][1] = curr_i
            if next_i is not None:
                table[next_i][0] = curr_i
            answer[curr_i] = 'O'
        else:
            c, x = command.split()
            x = int(x)
            for _ in range(x):
                k = table[k][0] if c == 'U' else table[k][1]


    return ''.join(answer)
