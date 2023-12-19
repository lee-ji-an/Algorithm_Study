def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    row, col = -1, 0
    num = 1
    
    for i in range(n, 0, -3):
        for _ in range(i):
            row += 1
            answer[row][col] = num
            num += 1
        for _ in range(i-1):
            col += 1
            answer[row][col] = num
            num += 1
        for _ in range(i-2):
            row -= 1
            col -= 1
            answer[row][col] = num
            num += 1
    
    return [val for row in answer for val in row]

solution(6)